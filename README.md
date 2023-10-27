# Vector Database Samples in Azure

As the need for customers to build copilots over their data grows, Vector Databases are becoming crucial in the architecture of production-grade copilot applications. This repository is a collection of samples that demonstrates how to use different vector database tools in Azure to store and query embeddings from text, documents and images.

The samples focus on -

- Working with text, documents and images
- Ingesting embeddings and constructing complex queries
- IAC scripts to spin up vector storage in Azure
- Common scaling and troubleshooting challenges

***What this repository is not*** - This repository doesn't offer any guidance on how to build LLM apps (for example RAG pattern). Please check the following repositories for LLM app development guidance.

- [End-to-End Retrieval Augmented Generation (RAG) Pattern with OpenAI](https://github.com/microsoft/rag-openai)
- [RAG Experiment Accelerator](https://github.com/microsoft/rag-experiment-accelerator)

## Code Structure

The samples are consistent across different vector database technologies to ensure they are easy to follow and facilitate the comparison of different options.

The *common* folder has sample code to generate embeddings. These embeddings are later used in the tech specfic samples for ingestion and vector search.

- generate_embeddings.ipynb
    - create text embeddings
    - create document embeddings (including chunking)
    - create image embeddings

Each technology ample follows the following structure.

- *technology_name*.bicep
- *[technology_name]*_ingestion.ipynb
    - create table/index with vector field
    - implement index
    - ingestion of text, document and image embeddings
    - incremental ingestion
- *[technology_name]*_vector_query.ipynb
    - Simple vector search
    - Metadata filtering with vector search 
    - Cross column vector search
    - Hybrid search 
    - Document search 
    - Image search 
    - Recall measurement

## Code Samples

- [Azure Cognitive Search](./azure_cognitive_search/README.md)
- [Azure PostgreSQL](azure_postgresql/README.md)
- [Azure Redis Cache](./azure_redis_cache/README.md)

## Run the Code Locally

- To run the code locally, install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) in Visual Studio Code. Please check [Jupyter Notebooks in VS Code
](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to understand how to use this extension.

- The samples uses conda to manage python dependencies. Please check [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) how to use conda with VS Code.
