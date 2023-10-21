# Azure PostgreSQL Samples

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using PostgreSQL.

## Resources Deployment

- Azure Database for PostgreSQL

  Vector search in PostgreSQL is supported via the [pgvector](https://github.com/pgvector/pgvector) extension. To enable this extension via Azure Portal, navigate to `Server Parameters`, under `azure.extensions` and select the `VECTOR` parameter.

  To deploy the Azure Database for PostgreSQL via IAC script -  
  1) Navigate to **[infrastructure](./infrastructure/)** folder
  2) Fill out the parameters values in `params` section according to your environment
  3) To deploy, run the following command- `az deployment group create --resource-group resource_group_name --template-file postgres.bicep`

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

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