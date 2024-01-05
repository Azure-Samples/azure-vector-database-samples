# Vector Database Samples in Azure

As the need for customers to build copilots over their data grows, Vector Databases are becoming crucial in the architecture of production-grade copilot applications. This repository is a collection of samples that demonstrates how to use different vector database tools in Azure to store and query embeddings from text, documents and images.

The samples focus on -

- Working with text, documents and images
- Ingesting embeddings and constructing complex queries
- IaC scripts to spin up vector storage in Azure
- Common best practices

***What this repository is not*** - This repository doesn't offer any guidance on how to build LLM apps (for example RAG pattern). Please check the following repositories for LLM app development guidance.

- [End-to-End Retrieval Augmented Generation (RAG) Pattern with OpenAI](https://github.com/microsoft/rag-openai)
- [RAG Experiment Accelerator](https://github.com/microsoft/rag-experiment-accelerator)

## Repository Structure

- [Code Samples](#code-sample)
  - [Azure AI Search](./code_sample/azure_ai_search/README.md)
  - [Azure Database for PostgreSQL](./code_sample/azure_postgresql/README.md)
  - [Azure Cache for Redis](./code_sample/azure_redis_cache/README.md)
  - [Azure CosmosDb for PostgreSQL](./code_sample/azure_cosmosdb_postgresql/README.md)
- [Evaluation Sample](./evaluation/README.md)
- [Best Practices](./best_practices/README.md)

## Code Sample

The samples are consistent across different vector database technologies to ensure they are easy to follow and facilitate the comparison of different options.

The *common* folder has sample code to generate embeddings. These embeddings are later used in the technology specific samples for ingestion and vector search.

- generate_embeddings.ipynb

  Notebook to generate embeddings from simple text, documents and images

Each technology specific sample folder follows the following structure.

- _infrastructure_ folder

  Sample bicep script to spin up the particular vector database in Azure.
- *[technology_name]*_data_pipeline.ipynb

  Notebook to create table with vector field, implement index (HNSW etc.) and ingest the embeddings.

- *[technology_name]*_vector_query.ipynb

  Notebook to demonstrate vector search examples, like simple vector search, including metadata filtering, Cross column vector search, hybrid search,recall measurement etc.

## Run the Code Locally

- To run the code locally, install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) in Visual Studio Code. Please check [Jupyter Notebooks in VS Code
](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to understand how to use this extension.

- The samples uses conda to manage python dependencies. Each sample comes with a conda environment (yml) file. Use the following command to create the conda environment.

    `conda env create -f environment.yml`

  Please check [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) how to use conda with VS Code.
