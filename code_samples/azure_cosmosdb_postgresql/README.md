# Azure CosmosDb for PostgreSQL Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure CosmosDb for PostgreSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/introduction) for text, documents and images.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [azure_cosmosdb_postgresql_conda.yml](./azure_cosmosdb_postgresql_conda.yml) file to include all necessary python dependencies.

      `conda env create -f azure_cosmosdb_postgresql_conda.yml`

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)

## Resources Deployment

- Azure CosmosDb for PostgreSQL

  *Create resource*

    Vector search feature can be used with Azure CosmosDb for PostgreSQL. Azure CosmosDb for PostgreSQL can be deployed from the Azure Portal.

    For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure CosmosDb for PostgreSQL. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

   `az deployment group create --resource-group resource_group_name --template-file azure_cosmosdb_postgresql.bicep`
  
  *Enable extension*

    Vector search in CosmosDb for PostgreSQL is supported via the [pgvector](https://github.com/pgvector/pgvector) extension. And for the Azure Cosmos DB for PostgreSQL Cluster (PostgreSQL version 12 - 16) the pgvector extension is enabled by default.
    
     Extension details - [how to use Azure CosmosDb PostgreSQL extensions](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/reference-extensions).

    PostgreSQL extensions must be installed in your database before you can use them.

     ```sql
     -- list the standard PostgreSQL extensions that are supported on Azure Cosmos DB for PostgreSQL.
     SELECT * FROM pg_available_extensions;

     -- install vector extension
     SELECT create_extension('vector');

     -- To remove an extension installed this way, use drop_extension().
     SELECT create_extension('vector');
     ```

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

- [azure_cosmosdb_postgresql_data_pipeline.ipynb](./azure_cosmosdb_postgresql_data_pipeline.ipynb)
- [azure_cosmosdb_postgresql_vector_query.ipynb](./azure_cosmosdb_postgresql_vector_query.ipynb)

## Reference

- [Official repository - pgvector](https://github.com/pgvector/pgvector)