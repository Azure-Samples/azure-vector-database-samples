import yaml, os
from dotenv import load_dotenv

class config():
    aoai_endpoint: str
    aoai_api_version: str
    aoai_key: str
    aoai_embedding_model: str
    dataset_path: str
    embedding_dataset_path: str
    pre_chunked_dataset_path: str
    ais_endpoint: str
    ais_api_version: str
    ais_key: str
    index_name: str

    def read_config(self, config_file):
        config_file = os.path.join(os.getcwd(), 'evaluation_samples\search_evaluation_accelarator\config', config_file)

        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    
    def __init__(self):
        load_dotenv()

        self.aoai_endpoint  = os.getenv("AOAI_ENDPOINT")
        self.aoai_api_version  = os.getenv("AOAI_API_VERSION")
        self.aoai_key  = os.getenv("AOAI_KEY")
        self.aoai_embedding_model  = os.getenv("AOAI_EMBEDDING_MODEL")
        self.ais_endpoint  = os.getenv("AIS_ENDPOINT")
        self.ais_api_version  = os.getenv("AIS_API_VERSION")
        self.ais_key  = os.getenv("AIS_KEY")

        config_file = 'exp1_config.yml'
        exp_config = self.read_config(config_file)
        self.dataset_path = exp_config['embedding'][0]['dataset_path']
        self.embedding_dataset_path = exp_config['embedding'][1]['embedding_dataset_path']
        self.pre_chunked_dataset_path = exp_config['embedding'][2]['pre_chunked_dataset_path']
        self.index_name = exp_config['data_load'][0]['index_name']

