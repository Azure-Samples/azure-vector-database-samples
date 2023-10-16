# Azure PostgreSQL Samples

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using PostgreSQL.

## Resources Deployment

For IAC scripts to deploy Azure resources, please check **[infra folder](./infra/)**. The script will deploy Azure Database for PostgreSQL flexible server.

To deploy the infra resources, follow below steps-

1) Navigate to **[infra folder](./infra/)**
2) Fill out the parameters values in `params` section according to your environment.
3) To deploy, run the following command- `az deployment group create --resource-group resource_group_name --template-file postgres.bicep`

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

  NOTE: For using Azure Postgres as Vector DB, you need to enable the Vector option in Postgres config.
  
  You can enable this option via- **Navigate to `Server Parameters`, under `azure.extensions` and select the `Vector` parameter.**

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