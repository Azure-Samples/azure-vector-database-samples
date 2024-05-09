from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration
)
import time

class aisearch_loader(evaluation_step):
    def execute(self):
        index_client = SearchIndexClient(self._config.ais_endpoint, AzureKeyCredential(self._config.ais_key))
        index_client.delete_index(self._config.index_name)
        time.sleep(5)

        vector_search = VectorSearch(
            profiles=[
                VectorSearchProfile(
                    name="hnsw_profile", algorithm_configuration_name="hnsw-algorithms-config"
                )
            ],
            algorithms=[HnswAlgorithmConfiguration(name="hnsw-algorithms-config")],
        )

        fields = [
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SearchableField(name="chunk_content", type=SearchFieldDataType.String),
            SearchField(name="chunk_content_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), searchable=True, vector_search_dimensions=1536, vector_search_profile_name="hnsw_profile"),
            SearchableField(name="source_doc", type=SearchFieldDataType.String)   
        ]

        index = SearchIndex(
            name=self._config.index_name,
            fields=fields,
            vector_search=vector_search
            )
        index_client = SearchIndexClient(self._config.ais_endpoint, AzureKeyCredential(self._config.ais_key))
        index = index_client.create_index(index)
    
        doc_df = pd.read_json(self._config.embedding_dataset_path)

        batch_size = 10
        total_records = doc_df.shape[0]
        fields = doc_df.columns.to_numpy()
        doc_df['id'] = doc_df['id'].astype(str)

        records = []

        for index, row in doc_df.iterrows():
            record = {}
            for field in fields:
                    record[field] = row[field]

            records.append(
                record
            )

            if index % batch_size == 0 or (index+1 == total_records):
                search_client = SearchClient(self._config.ais_endpoint, self._config.index_name, AzureKeyCredential(self._config.ais_key))
                result = search_client.upload_documents(documents=records)
                records = []

