from typing import Any
from evaluation import evaluation_step
import os
from dotenv import load_dotenv

class openai_embedding(evaluation_step):
    def execute(self) -> str:
        print("openai_embedding")
        print(self.config)
        # super().handle_request(request)