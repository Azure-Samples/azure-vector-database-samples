# Azure Cache for Redis Samples

This folder includes the notebooks and infra code to demonstrate vector search capabilities for text, documents and images using Azure Redis Cache.

## Resources Deployment

For IAC scripts to deploy Azure resources, please check **[infra folder](./infra/)**. The script will deploy Azure Cache for Redis.

To deploy the infra resources, follow below steps-

1) Navigate to **[infra folder](./infra/)**
2) Fill out the parameters values in `params` section according to your environment.
3) To deploy, run the following command- `az deployment group create --resource-group resource_group_name --template-file azure_redis_cache.bicep`

 NOTE:  **For using Azure Cache for Redis as Vector DB, you need to enable the `Redis Search` module in Azure Redis config. This option is only available for Redis Enterprise Versions. You can enable this option while provisioning the Azure Redis under `Modules` option of `Advanced` section.**

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.
