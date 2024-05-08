import json
import os
import pandas as pd

class ai_search:
    def __init__(self, eval_dataset):
        self.eval_dataset = eval_dataset

# generate embeddings
    def generate_embeddings(self):
        config_file = os.path.join(os.getcwd(), 'evaluation_samples\search_evaluation_accelarator\data', self.eval_dataset)
        df = pd.read_csv(config_file)
        
        self.df = df

    # create index
    def create_index():
        print('create')

    # load data
    def load_data():
        print('create')

