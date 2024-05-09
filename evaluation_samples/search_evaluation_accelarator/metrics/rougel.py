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
from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv
from config import config
import pandas as pd
import json
from openai import AzureOpenAI
from azure.search.documents.models import VectorizedQuery
from rouge_score import rouge_scorer

class rougel_evaluator(evaluation_step):
    def __init__(self, config):
        super().__init__(config)

    def execute(self):
        eval_df = pd.read_csv(self._config.eval_dataset)
        eval_output_df = pd.DataFrame(columns=['chunk_content_id', 'rougel_score'])

        for index, row in eval_df.iterrows():
            question = row['question']
            expected_answer = row['answer']
            expected_source = row['source']

            aoai_client = AzureOpenAI(
                api_key=self._config.aoai_key,
                api_version=self._config.aoai_api_version,
                azure_endpoint=self._config.aoai_endpoint
            )
            query_vector = aoai_client.embeddings.create(input = [question], model=self._config.aoai_embedding_model).data[0].embedding

            search_client = SearchClient(self._config.ais_endpoint, self._config.index_name, AzureKeyCredential(self._config.ais_key))
            raw_vector_query = VectorizedQuery(vector=query_vector, k_nearest_neighbors=1, fields="chunk_content_vector")

            results = search_client.search(  
                search_text=None,  
                vector_queries= [raw_vector_query],
                select=["chunk_content", "source_doc"],
            )  

            for result in results:
                returned_answer = result['chunk_content']
                returned_source = result['source_doc']

            _rouge_scorer = rouge_scorer.RougeScorer(rouge_types=["rougeL"], use_stemmer=True)

            rougeL_recall = _rouge_scorer.score(target=expected_answer, prediction=returned_answer)["rougeL"].recall
            max_rougeL_recall = -1
            max_rougeL_recall = rougeL_recall if rougeL_recall > max_rougeL_recall else max_rougeL_recall

            new_row = {'chunk_content_id': index, 'rougel_score': max_rougeL_recall}
            eval_output_df = pd.concat([eval_output_df, pd.DataFrame([new_row])], ignore_index=True)

        eval_output_df.to_csv(self._config.eval_output, index=False)
