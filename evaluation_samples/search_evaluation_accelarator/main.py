from evaluation import evaluation_chain
from embedding.openai import openai_embedding
from data_loader.ai_search import aisearch_loader
from metrics.rougel import rougel_evaluator
from config import config

if __name__ == "__main__":

    _config = config()

    eval_chain = evaluation_chain()
    # generate embeddigns and save that as json file for the data that needs to go to the index
    eval_chain.add_evaluation_step(openai_embedding(_config))

    # load the generated embeddings to ai search index
    eval_chain.add_evaluation_step(aisearch_loader(_config))

    # use the eva dataset that we have to calcualte rougel score
    eval_chain.add_evaluation_step(rougel_evaluator(_config))

    eval_chain.execute()