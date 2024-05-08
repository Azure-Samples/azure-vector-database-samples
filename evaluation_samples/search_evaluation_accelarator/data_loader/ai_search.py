from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv

class aisearch_loader(evaluation_step):
    def execute(self) -> str:
        print("aisearch_loader")
        print(self.config)
        # super().handle_request(request)