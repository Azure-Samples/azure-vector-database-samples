# Azure CosmosDb Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure CosmosDb NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/) for text and documents

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [azure_cosmosdb_nosql_conda.yml](./azure_cosmosdb_nosql_conda.yml) file to include all necessary python dependencies.

      `conda env create -f cosmostest azure_cosmosdb_nosql_conda.yml`

      

      **Alternatively**

      a. You could install the [requirements.txt](./requirements.txt) in your environment **instead** the yml.

          `pip install -r /path/to/requirements.txt`

      b. Or run the pip install libraries from the ingestion sample script- [azure_cosmos_ingestion.ipynb](./cosmos_ingestion.ipynb).



2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)


## Resources Deployment

- Azure CosmosDb 

  *Create resource*

    Augment the Azure Cosmos DB data with semantic and vector search capabilities of Azure AI Search.. 

    For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure CosmosDb. In the bicep script, **fill out the parameters** values according to your environment, and run the following command. 
    Note: It will deploy an empty Cosmos Db No SQL, containers will be created in the ingestion step.

   `az deployment group create --resource-group resource_group_name --template-file azure_cosmosdb_nosql.bicep`
  
  

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

  Please note, for the semantic Search you need to enable the Service: [Semantic](https://learn.microsoft.com/en-us/azure/search/semantic-how-to-enable-disable?tabs=enable-portal)
  
  **In summary:** You will need to have an Open AI Service created with the Model deployed from it( for example:text-embedding-ada-002), and also a Cognitive Search Service created with the Semantic Search enable.

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
  - [Create a Service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)
  - [Vector Store](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-create-index?tabs=config-2023-11-01%2Crest-2023-11-01%2Cpush%2Cportal-check-index)
  - [Deploy Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#embeddings-models)
