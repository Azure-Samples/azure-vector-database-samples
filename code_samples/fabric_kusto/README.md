# Fabric Real-Time Analytics(Kusto) Samples

This folder includes the notebooks to demonstrate vector search capabilities of [Fabric Real-Time Analytics(Kusto)](https://learn.microsoft.com/en-us/fabric/real-time-analytics/overview) for text, documents and images.

## Run the Code Locally

Follow the steps to run the code locally.

1. The samples uses Conda to manage virtual environments. Create a conda environment using the [fabric_kusto_conda.yml](./fabric_kusto_conda.yml) file to include all necessary python dependencies.

      `conda env create -f fabric_kusto_conda.yml`

2. Create a *.env* file from the *.env-template* and populate it with all necessary keys.

3. Finally, follow the instructions mentioned here to run the code locally using VS Code - [Run the Code Locally](../README.md#run-the-code-locally)

## Resources Deployment

- Fabric Kusto endpoint  
  As a SaaS service, Kusto in Fabric does not support IaC. But you can easily create en Kusto endpoint(KQL database) by Fabric UI following the instructions to create a KQL database - [Fabric/Create a KQL database](https://learn.microsoft.com/en-us/fabric/real-time-analytics/create-database?source=recommendations)

  *[Optional]* If you want to authenticate with client-secret way, you also need to enable settings in Fabric with admin permission to allow service principle to access Fabric workspace. To do so, follow the instructions [here](https://learn.microsoft.com/en-us/fabric/admin/metadata-scanning-enable-read-only-apis).

- Azure OpenAI
  
  Azure OpenAI Service resource can be deployed using [Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal), [Azure CLI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=cli) or [Azure PowerShell](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=ps). Again, [private endpoints](https://learn.microsoft.com/azure/ai-services/cognitive-services-virtual-networks?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=portal#use-private-endpoints) can be used for Azure AI services resources to allow clients on a virtual network to securely access data over Azure Private Link.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample

## Sample Notebooks

- [fabric_kusto_data_pipeline.ipynb](./fabric_kusto_data_pipeline.ipynb)
- [fabric_kusto_vector_query.ipynb](./fabric_kusto_vector_query.ipynb)

## Reference

- [Fabric Real-Time Analytics/end-to-end tutorial](https://learn.microsoft.com/en-us/fabric/real-time-analytics/tutorial-introduction)
- [Fabric Real-Time Analytics/Compare with Azure Data Explorer](https://learn.microsoft.com/en-us/fabric/real-time-analytics/realtime-analytics-compare)