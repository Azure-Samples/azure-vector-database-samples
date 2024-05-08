from typing import Any
from handler import Handler, AbstractHandler

class embedding_generation_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"embedding_generation_executor {request}")
        return super().handle(request)