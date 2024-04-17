# Vector Search in Azure Databricks

Databricks Vector Search is a serverless similarity search engine, built into the Databricks Intelligence Platform.

With Databricks Vector Search, you can create auto-updating vector search indexes, from Delta tables managed by Unity Catalog.

Theses optimized indexes include both the embedded data and its metadata. They can be queried using REST API to identify most similar vectors and the associated documents.

Databricks Vector Search uses the Hierarchical Navigable Small World (HNSW) algorithm for its approximate nearest neighbor searches and the L2 distance distance metric to measure embedding vector similarity.

You can create and manage Vector Search components, like a vector search endpoint and vector search indices, using any of the following methods:

- UI
- Python SDK
- REST APIs

This folder includes the notebooks to demonstrate [Azure Databricks Vector Search](https://learn.microsoft.com/en-us/azure/databricks/generative-ai/create-query-vector-search) capabilities for text, documents and images using the REST API and Python SDK.

## Requirements:

- Unity Catalog enabled workspace.
- Serverless compute enabled.
- Source tables with Change Data Feed enabled.
- Personal access tokens enabled.(Not Recommended for production workloads)
- CREATE TABLE privileges on catalog schema(s) to create indexes.
- Unity Catalog privileges for the Users querying the vector search endpoint(if not the owners of Vector Search Index):
  1. USE CATALOG on the catalog that contains the vector search index.
  2. USE SCHEMA on the schema that contains the vector search index.
  3. SELECT on the vector search index.

## Run the Code locally 

For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Databricks environment. In the bicep script, fill out the parameters values in `params` section according to your environment.

1. Using the Azure CLI, login to your Azure account with the command `az login`.
2. Choose the account using command `az account set --subscription "<subscription ID or name>"`
3. Create a resource group 'az group create --name hema_test --location eastus'
4. Deploy the Databricks environment `az deployment group create --resource-group resource_group_name --template-file databricks.bicep`

az deployment group create --resource-group hema_test --template-file C:\github\azure-vector-database-samples-1\code_samples\azure_databricks\infrastructure\databricks.bicep

code_samples\azure_databricks\infrastructure\databricks.bicep



Y
go to `accounts.azuredatabricks.net/data`, then `Create metastore`
1. The samples uses 
Deploy the Databricks Environment
You would need Azure Global admin privelidge to create a Metastore in the databricks environment
go to `accounts.azuredatabricks.net/data`, then `Create metastore`


  



## Run the Code in azure Databricks Environment

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