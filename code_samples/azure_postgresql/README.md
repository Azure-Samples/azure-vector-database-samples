# Azure Database for PostgreSQL Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/) for text, documents and images.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [postgresql_conda.yml](./postgresql_conda.yml) file to include all necessary python dependencies.

      `conda env create -f postgresql_conda.yml`

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)

## Resources Deployment

- Azure Database for PostgreSQL

  For PostgreSQL, vector search feature can only be used with Flexible Server.

  *Create resource*

    Vector search feature can only be used with Flexible Server. PostgreSQL Flexible Server can  be deployed from the Azure Portal.

    For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the PostgreSQL Flexible Server. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

   `az deployment group create --resource-group resource_group_name --template-file postgres.bicep`
  
  *Enable extension*

    Vector search in PostgreSQL is supported via the [pgvector](https://github.com/pgvector/pgvector) extension. To add it to allowlist via Azure Portal, navigate to `Server Parameters`, under `azure.extensions` and select the `VECTOR` parameter. 
    
     Extension details - [how to use PostgreSQL extensions](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-extensions#how-to-use-postgresql-extensions). Check if it's correctly added by running `SHOW azure.extensions;`.

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

- [postgresql_data_pipeline.ipynb](./postgresql_data_pipeline.ipynb)
- [postgresql_vector_query.ipynb](./postgresql_vector_query.ipynb)

## Reference

- [Official repository - pgvector](https://github.com/pgvector/pgvector)