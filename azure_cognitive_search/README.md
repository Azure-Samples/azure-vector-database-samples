# Azure Cognitive Search Samples

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using Azure Cognitive Search. There are two ways to use Azure Cognitive Search - REST API or Python SDK.

## Resources Deployment

- Azure Cognitive Search

  *Create resource*

  Vector search feature can only be used with Azure Cognitive Search. Azure Cognitive Search can  be deployed from the Azure Portal.

  For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure Cognitive Search Service. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

  `az deployment group create --resource-group resource_group_name --template-file cognitive_search.bicep`

- Azure OpenAI

  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Prerequisites

- Create a conda environment to include all necessary python dependencies.
  - For REST endpoint samples - [cognitive_search_rest_conda.yml](./rest_endpoint_sample/cognitive_search_rest_conda.yml)
  - For Python SDK samples - [cognitive_search_sdk_conda.yml](./python_sdk_sample/cognitive_search_sdk_conda.yml)
- Create a *.env* file from the *.env-template* and populate it with all necessary keys.
- Run the [common > generate_embeddings.ipynb](../common/generate_embeddings.ipynb) notebook to generate the embeddings from the source dataset before running the samples.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

### Using REST Endpoint

- [cognitive_search_rest_ingestion.ipynb](./rest_endpoint_sample/cognitive_search_rest_ingestion.ipynb)
- [cognitive_search_rest_query.ipynb](./rest_endpoint_sample/cognitive_search_rest_query.ipynb)

### Using Python SDK

- [cognitive_search_sdk_ingestion.ipynb](./python_sdk_sample/cognitive_search_sdk_ingestion.ipynb)
- [cognitive_search_sdk_query.ipynb](./python_sdk_sample/cognitive_search_sdk_query.ipynb)