# from __future__ import annotations
import yaml, os
from embedding.openai import embedding_generation_executor
from data_loader.ai_search import embedding_loading_executor
from search.ai_search import vector_search_executor

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
