from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv

class vector_search(evaluation_step):
    def execute(self) -> str:
        print("vector_search")
        print(self.config)
        # super().handle_request(request)