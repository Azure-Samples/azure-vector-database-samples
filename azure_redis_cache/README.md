# Azure Cache for Redis Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/) for text, documents and images.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [redis_cache_conda.yml](./redis_cache_conda.yml) file to include all necessary python dependencies.

      `conda env create -f redis_cache_conda.yml`

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)

## Resources Deployment

- Azure Cache for Redis

  For using Azure Cache for Redis as Vector DB, `RediSearch` module needs to be enabled - [Use Redis modules with Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-redis-modules). This option is currently available only for Redis Enterprise Versions.

  Azure Cache for Redis can be deployed using the [Azure Portal](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/quickstart-create-redis) or [bicep/arm/terraform templates](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-redis-cache-bicep-provision). From network security perspective, you can use [private endpoint](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-private-link) to secure inbound and outbound connectivity.

  For IAC deployment, **[infrastructure](./infrastructure/)** folder has a bicep script to deploy the Azure Cache for Redis. In the bicep script, fill out the parameters values in `params` section according to your environment, and run the following command.

  `az deployment group create --resource-group resource_group_name --template-file azure_redis_cache.bicep`

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.
- Azure Computer Vision

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

- [redis_data_pipeline.ipynb](./redis_data_pipeline.ipynb)
- [redis_vector_query.ipynb](./redis_vector_query.ipynb)