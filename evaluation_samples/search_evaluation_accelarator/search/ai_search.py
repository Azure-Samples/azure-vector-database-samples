from typing import Any
from handler import Handler, AbstractHandler

class vector_search_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"vector_search_executor {request}")
        return super().handle(request)