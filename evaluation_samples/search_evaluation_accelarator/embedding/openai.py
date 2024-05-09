from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv
from config import config
import pandas as pd
import json
from openai import AzureOpenAI
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tqdm import tqdm

class openai_embedding(evaluation_step):
    def __init__(self, config: config):
        super().__init__(config)

    def execute(self):
        documents = self.load_documents()
        chunks = self.split_documents(documents)
        records = self.generate_embeddings(chunks)
        self.save_embeddings(records)

    def load_documents(self) -> Any:
        GLOB = "*.md"
        loader = DirectoryLoader(self._config.pre_chunked_dataset_path, glob=GLOB, loader_cls=UnstructuredMarkdownLoader)
        return loader.load()

    def split_documents(self, documents: Any) -> Any:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
        )
        return text_splitter.split_documents(documents)

    def generate_embeddings(self, chunks: Any) -> list[dict]:
        aoai_client = AzureOpenAI(
            api_key=self._config.aoai_key,
            api_version=self._config.aoai_api_version,
            azure_endpoint=self._config.aoai_endpoint
        )

        records = []
        for i, chunk in enumerate(tqdm(chunks)):
            chunk_content = chunk.page_content
            chunk_content_vector = aoai_client.embeddings.create(input=[chunk_content], model=self._config.aoai_embedding_model).data[0].embedding
            records.append({
                "id": str(i),
                "chunk_content": chunk_content,
                "chunk_content_vector": chunk_content_vector,
                "source_doc": os.path.basename(chunk.metadata['source'])
            })
        return records

    def save_embeddings(self, records: list[dict]) -> None:
        with open(self._config.embedding_dataset_path, "w") as f:
            json.dump(records, f)