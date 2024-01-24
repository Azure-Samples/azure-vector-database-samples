# Cosmos Mongo vCore Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Azure Cosmos DB for MongoDB vCore](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/vector-search) for text, documents and images.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses venv to manage virtual environments. Create a venv environment using the provided `requirements.txt` file to include all necessary python dependencies.

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

- [mongo_data_pipeline.ipynb](./rest_endpoint_sample/mongo_data_pipeline.ipynb)
- [mongo_rest_query.ipynb](./rest_endpoint_sample/mongo_vector_queries.ipynb)
