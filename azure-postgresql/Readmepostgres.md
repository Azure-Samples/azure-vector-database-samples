### Before Start:



[Azure Cognitive Search](https://docs.microsoft.com/azure/search/) is a search-as-a-service cloud solution that gives developers APIs and tools for adding a rich search experience over private, heterogeneous content in web, mobile, and enterprise applications.

The following scripts leverage PostgreSQL, as a vector database to store and query [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings?ref=timescale.com). 



#### Requisite

##### Postgres

1) You need a Postgres Azure SQL Database. Follow the documentation and provide the guidance:

[Quickstart: Create server - Azure portal - Azure Database for PostgreSQL - Flexible Server | Microsoft Learn](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal)

 

2. Deploy a database:

 [How to enable and use pgvector - Azure Database for PostgreSQL - Flexible Server | Microsoft Learn](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector)

Create database:


![image](https://github.com/Azure-Samples/azure-vector-database-samples/assets/62876278/37172928-7b22-4fcf-9abc-270367f0377b)



If the Postgres version is higher than 14. The script provided will follow a different configuration.

![image](https://github.com/Azure-Samples/azure-vector-database-samples/assets/62876278/4c53b466-7ca6-437e-8325-9bff3470f6a5)


Add extension, only for versions below 14: https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-extensions





#### OpenAI

1. You need to have access to Open AI. Follow the docs to proceed with the request:

[What is Azure OpenAI Service? - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

 [Request Access to Azure OpenAI Service (microsoft.com)](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu)

 

2. You need to deploy OpenAI embeddings

[Azure OpenAI Service embeddings tutorial - Azure OpenAI | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/embeddings?tabs=command-line)



Setup the OS environment variables:

Docs for more information: [Connect using API keys - Azure Cognitive Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-security-api-keys?tabs=portal-use%2Cportal-find%2Cportal-query)



Example

```
setx AZURE_OPENAI_ENDPOINT "https://<nameoftheservicedeployed>.openai.azure.com/"

setx AZURE_OPENAI_API_KEY "KeysandEndpoints - Copy here Key 1 OR 2"

 
```



3. Deploy the Cognitive Search Service

[Create a search service in the portal - Azure Cognitive Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)

 

Setup the OS environment variables:



Example


```
setx AZURE_SEARCH_ADMIN_KEY "Copy here Cognitive search -> keys"
```

The latest not  the least set up the version. use the latest version not in preview for production workloads

[Azure OpenAI Service REST API reference - Azure OpenAI | Microsoft Learn](https://learn.microsoft.com/en-US/azure/ai-services/openai/reference)

Example:

```
setx AZURE_OPENAI_API_VERSION "2023-05-15"
```

4. Deploy the model:

This script uses the: text-embedding-ada-002 and you will need to  create it at https://oai.azure.com/
![image](https://github.com/Azure-Samples/azure-vector-database-samples/assets/62876278/12733b74-3b71-43b8-9869-4c9bf4fa7686)




Please look at the docs for more details about this scenario:

[Azure OpenAI Service embeddings tutorial - Azure OpenAI | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/embeddings?tabs=command-line)https://github.com/Azure/cognitive-search-vector-pr/tree/main/demo-python/data)
