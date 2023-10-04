# Vector Database Samples in Azure

As the need for customers to build copilots over their data grows, Vector Databases are becoming crucial in the architecture of production-grade copilot applications. This repository is a collection of samples that demonstrates how to use different vector database tools in Azure to interact with embeddings from text, documents and images.

The samples focus on -

- Working with text, documents and images
- IAC code to spin up vector storage in Azure
- Ingesting embeddings and constructing complex queries
- Common scaling and troubleshooting challenges

***What this repository is not*** - This repository doesn't offer any guidance on how to build LLM apps (for example RAG pattern).

## Sample Code

- [Azure Cognitive Search](./azure_cognitive_search/README.md)
- [Azure Redis Cache](azure_redis_cache/)
- [Azure PostgreSQL](azure-postgresql/)

## Run the Code Locally

To run the code locally, install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) in Visual Studio Code.