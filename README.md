# Azure Vector Database Samples 

As the need for customers to build copilots over their data grows, Vector Databases are becoming crucial in the architecture of production-grade copilot applications. This repository is a collection of samples that demonstrates how to use different vector database tools in Azure to store and query embeddings from text, documents and images.

The samples focus on -

- Working with text, documents and images
- Ingesting embeddings and constructing complex queries
- IaC scripts to spin up vector storage in Azure
- Common best practices

***What this repository is not*** - This repository doesn't offer any guidance on how to build LLM apps (for example RAG pattern). Please check the following repositories for LLM app development guidance.

- [LLMOps with Prompt flow (preview)](https://github.com/microsoft/llmops-promptflow-template)
- [Chat with your data - Solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator)

## Repository Structure

- [Code Sampless](./code_samples/README.md)
  - [Azure AI Search](./code_samples/azure_ai_search/README.md)
  - [Azure Database for PostgreSQL](./code_samples/azure_postgresql/README.md)
  - [Azure Cache for Redis](./code_samples/azure_redis_cache/README.md)
  - [Azure CosmosDb for PostgreSQL](./code_samples/azure_cosmosdb_postgresql/README.md)
  - [Azure Cosmos DB for MongoDB vCore](./code_samples/azure_cosmosdb_mongo/README.md)
- [Evaluation Samples](./evaluation_samples/README.md)
- [Best Practices](./best_practices/README.md)

## Run the Code Locally

- To run the code locally, install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) in Visual Studio Code. Please check [Jupyter Notebooks in VS Code
](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to understand how to use this extension.

- The samples uses conda to manage python dependencies. Each sample comes with a conda environment (yml) file. Use the following command to create the conda environment.

    `conda env create -f environment.yml`

  Please check [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) how to use conda with VS Code.
