# Azure CosmosDb Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure CosmosDb NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/) for text and documents

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [azure_cosmosdb_nosql_conda.yml](./azure_cosmosdb_nosql_conda.yml) file to include all necessary python dependencies.

      `conda env create -f azure_cosmosdb_nosql_conda.yml`

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)

## Resources Deployment

- Azure CosmosDb 

  *Create resource*

    Augment the Azure Cosmos DB data with semantic and vector search capabilities of Azure AI Search.. 

    For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure CosmosDb. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

   `az deployment group create --resource-group resource_group_name --template-file azure_cosmosdb_nosql.bicep`
  
  

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample

- [docs](../data/docs/) - for document search sample

  

## Sample Notebooks

- [azure_cosmos_ingestion.ipynb](./cosmos_ingestion.ipynb)
- [azure_cosmos_vector_query.ipynb](./cosmosdb_vector_query.ipynb)

## Reference

- [Vector database - Azure Cosmos DB | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-database#implement-vector-database-functionalities-using-our-nosql-api-and-ai-search)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
  - [Retrieval Augmented Generation (RAG) in Azure AI Search](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
  - [Vector search overview](https://learn.microsoft.com/azure/search/vector-search-overview)
  - [Hybrid search overview](https://learn.microsoft.com/azure/search/hybrid-search-overview)
  - [Create a vector index](https://learn.microsoft.com/azure/search/vector-search-how-to-create-index)
  - [Query a vector index](https://learn.microsoft.com/azure/search/vector-search-how-to-query)
  - [Vector search algorithms](https://learn.microsoft.com/azure/search/vector-search-ranking)