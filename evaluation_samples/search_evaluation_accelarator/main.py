from evaluation import evaluation_chain
from embedding.openai import openai_embedding
from data_loader.ai_search import aisearch_loader
from search.aisearch import vector_search
from config import config

if __name__ == "__main__":

    _config = config()
    eval_chain = evaluation_chain()
    eval_chain.add_evaluation_step(openai_embedding(_config))
    # eval_chain.add_evaluation_step(aisearch_loader(_config))
    # eval_chain.add_evaluation_step(vector_search(_config))

    eval_chain.execute()