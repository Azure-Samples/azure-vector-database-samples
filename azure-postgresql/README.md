# Azure PostgreSQL Samples

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using PostgreSQL.

## Resources Deployment

For IAC scripts to deploy Azure resources, please check this repository - [Virtual Network Integration Recipes
](https://github.com/Azure-Samples/virtual-network-integration-recipes)

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.
- Azure Computer Vision
- Azure Database for PostgreSQL flexible server

## Prerequisites

- Create a conda environment to include all necessary python dependencies.
  - [postgresql_conda.yml](./postgresql_conda.yml)
- Create a *.env* file from the *.env-template* and populate it with all necessary keys.
- Run the [common > generate_embeddings.ipynb](../common/generate_embeddings.ipynb) notebook to generate the embeddings from the source dataset before running the samples.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

- [postgresql_ingestion.ipynb](./postgresql_ingestion.ipynb)
- [postgresql_vector_query.ipynb](./postgresql_vector_query.ipynb)

## Reference

- [pgvector github repository](https://github.com/pgvector/pgvector)