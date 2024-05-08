import yaml, os
from evaluation import evaluation_chain
from embedding.openai import openai_embedding
from data_loader.ai_search import aisearch_loader
from search.aisearch import vector_search

def read_config(config_file):
    config_file = os.path.join(os.getcwd(), 'evaluation_samples\search_evaluation_accelarator\config', config_file)

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    config_file = 'exp1_config.yml'
    config = read_config(config_file)

    eval_chain = evaluation_chain()
    eval_chain.add_evaluation_step(openai_embedding(config))
    eval_chain.add_evaluation_step(aisearch_loader(config))
    eval_chain.add_evaluation_step(vector_search(config))

    eval_chain.execute()