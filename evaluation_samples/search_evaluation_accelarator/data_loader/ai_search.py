from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient

class aisearch_loader(evaluation_step):
    def execute(self) -> str:
        print("aisearch_loader")
        print(self.config)
        # super().handle_request(request)