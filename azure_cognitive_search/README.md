# Azure Cognitive Search

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using Azure Cognitive Search. There are two ways to use Azure Cognitive Search, REST API and Python SDK.

## Prerequisites

- Azure resources
  - Azure Cognitive Search
  - Azure OpenAI
  - Azure Computer Vision
- Create a conda environment to include all necessary python dependencies.
  - For REST endpoint samples - [cognitive_search_rest_conda.yml](./rest_endpoint_sample/cognitive_search_rest_conda.yml)
  - For Python SDK samples - [cognitive_search_sdk_conda.yml](./python_sdk_sample/cognitive_search_sdk_conda.yml)
- Create a *.env* file from the *.env-template* and populate it with all necessary keys.
- Run the [common > generate_embeddings.ipynb](../common/generate_embeddings.ipynb) notebook to generate the embeddings from the source dataset before running the samples.

## Resources Deployment Instructions

Azure Cognitive Search can be deployed using the [Azure Portal](https://docs.microsoft.com/azure/search/search-create-service-portal) or [bicep/arm/terraform templates](https://learn.microsoft.com/azure/templates/Microsoft.Search/searchServices?pivots=deployment-language-bicep#identity). From network security perspective, you can use [private endpoint](https://learn.microsoft.com/azure/search/service-create-private-endpoint) and [shared private link](https://learn.microsoft.com/azure/search/search-indexer-howto-access-private?tabs=portal-create) to secure inbound and outbound connectivity.

Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

### Using REST Endpoint

- [cognitive_search_rest_text.ipynb](./rest_endpoint_sample/cognitive_search_rest_text.ipynb)
- [cognitive_search_rest_doc.ipynb](./rest_endpoint_sample/cognitive_search_rest_doc.ipynb)
- [cognitive_search_rest_image.ipynb](./rest_endpoint_sample/cognitive_search_rest_image.ipynb)

### Using Python SDK

- [cognitive_search_sdk_text.ipynb](./rest_endpoint_sample/cognitive_search_sdk_text.ipynb)
- [cognitive_search_sdk_doc.ipynb](./rest_endpoint_sample/cognitive_search_sdk_doc.ipynb)
- [cognitive_search_sdk_image.ipynb](./rest_endpoint_sample/cognitive_search_sdk_image.ipynb)