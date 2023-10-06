# Vector Database Samples in Azure

As the need for customers to build copilots over their data grows, Vector Databases are becoming crucial in the architecture of production-grade copilot applications. This repository is a collection of samples that demonstrates how to use different vector database tools in Azure to store and query embeddings from text, documents and images.

The samples focus on -

- Working with text, documents and images
- Ingesting embeddings and constructing complex queries
- IAC scripts to spin up vector storage in Azure
- Common scaling and troubleshooting challenges

***What this repository is not*** - This repository doesn't offer any guidance on how to build LLM apps (for example RAG pattern). Please check the following repositories for LLM app development guidance.

- [End-to-End Retrieval Augmented Generation (RAG) Pattern with OpenAI](https://github.com/microsoft/rag-openai)

## Code Samples

- [Azure Cognitive Search](./azure_cognitive_search/README.md)
- [Azure Redis Cache](./azure_redis_cache/README.md)
- [Azure PostgreSQL](azure-postgresql/README.md)

## Run the Code Locally

To run the code locally, install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) in Visual Studio Code. Please check [Jupyter Notebooks in VS Code
](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to understand how to use this extension.