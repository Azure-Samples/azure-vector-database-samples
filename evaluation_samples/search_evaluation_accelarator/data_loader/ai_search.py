from typing import Any
from handler import Handler, AbstractHandler

class embedding_loading_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"embedding_loading_executor {request}")
        return super().handle(request)