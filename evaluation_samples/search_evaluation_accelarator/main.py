from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import yaml
import importlib
import os

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class embedding_generation_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"embedding_generation_executor {request}")
        return super().handle(request)
    
class embedding_loading_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"embedding_loading_executor {request}")
        return super().handle(request)
    
class vector_search_executor(AbstractHandler):
    def handle(self, request: Any) -> str:
        print(f"vector_search_executor {request}")
        return super().handle(request)

def read_config(config_file):
    config_file = os.path.join(os.getcwd(), 'evaluation_samples\search_evaluation_accelarator\config', config_file)

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    config_file = 'exp1_config.yml'
    config = read_config(config_file)

    data_loader_module = config['data_loader'][0]['module']
    eval_dataset = config['data_loader'][1]['eval_dataset']

    embedding_generation_executor = embedding_generation_executor()
    embedding_loading_executor = embedding_loading_executor()
    vector_search_executor = vector_search_executor()

    embedding_generation_executor.\
        set_next(embedding_loading_executor).\
        set_next(vector_search_executor)

    embedding_generation_executor.handle(config)
