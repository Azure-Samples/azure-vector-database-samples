# Azure AI Search Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) for text, documents and images using the REST API and Python SDK.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the provided yml file to include all necessary python dependencies.

    - For REST endpoint samples - [ai_search_rest_conda.yml](./rest_endpoint_sample/ai_search_rest_conda.yml)

      `conda env create -f ai_search_rest_conda.yml`

    - For Python SDK samples - [ai_search_sdk_conda.yml](./python_sdk_sample/ai_search_sdk_conda.yml)
  
      `conda env create -f ai_search_sdk_conda.yml`

      _azure-search-documents_ is installed from the wheel package ([azure_search_documents-11.4.0b12-py3-none-any.whl](./python_sdk_sample/whl/azure_search_documents-11.4.0b12-py3-none-any.whl)) directly to use the latest version of the library.

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../../README.md#run-the-code-locally)

## Resources Deployment

The code requires two Azure services - Azure AI Search and Azure OpenAI. 

- Azure AI Search

  - Deploy from Portal

  Azure Cognitive Search can be deployed using the [Azure Portal](https://docs.microsoft.com/azure/search/search-create-service-portal) or [bicep/arm/terraform templates](https://learn.microsoft.com/azure/templates/Microsoft.Search/searchServices?pivots=deployment-language-bicep#identity). From network security perspective, you can use [private endpoint](https://learn.microsoft.com/azure/search/service-create-private-endpoint) and [shared private link](https://learn.microsoft.com/azure/search/search-indexer-howto-access-private?tabs=portal-create) to secure inbound and outbound connectivity.

  - IAC Deployment
  
  For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure Cognitive Search Service. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

  `az deployment group create --resource-group resource_group_name --template-file cognitive_search.bicep`

- Azure OpenAI

  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

### Using REST Endpoint

- [ai_search_rest_data_pipeline.ipynb](./rest_endpoint_sample/ai_search_rest_data_pipeline.ipynb)
- [ai_search_rest_query.ipynb](./rest_endpoint_sample/ai_search_rest_query.ipynb)

### Using Python SDK

- [ai_search_sdk_data_pipeline.ipynb](./python_sdk_sample/ai_search_sdk_data_pipeline.ipynb)
- [ai_search_sdk_query.ipynb](./python_sdk_sample/ai_search_sdk_query.ipynb)

## Reference

- [Create a vector query in Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-query)
- [Azure AI Search REST API reference](https://learn.microsoft.com/en-us/rest/api/searchservice/?view=rest-searchservice-2023-11-01)
- [Vector search samples - Azure AI Search](https://github.com/Azure/azure-search-vector-samples)