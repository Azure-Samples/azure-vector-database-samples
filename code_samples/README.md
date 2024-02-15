# Code Samples

This section provides product specific code samples on how to ingest and efficiently query a vector database. The samples are consistent across different vector database products to ensure they are easy to follow and facilitate the comparison of different options.

## Product Samples
- [Azure AI Search](./azure_ai_search/README.md)
- [Azure Database for PostgreSQL](azure_postgresql/README.md)
- [Azure Cache for Redis](./azure_redis_cache/README.md)
- [Azure CosmosDb for PostgreSQL](./azure_cosmosdb_postgresql/README.md)
- [Fabric Real-Time Analytics(Kusto)](./fabric_kusto/README.md)

## Folder Structure

- data folder

  The *data* folder has the text, doc and images which are used in the sample notebooks. This folder also has the generated embeddings from the original data.

- common folder

  The *common* folder has sample code to generate embeddings. These embeddings are later used in the product specific samples for ingestion and vector search.

    - [generate_embeddings.ipynb](./common/generate_embeddings.ipynb)

      Notebook to generate embeddings from simple text, documents and images

- product specific folder

    Each product specific sample folder follows the following structure.

    - _infrastructure_ folder

    Sample bicep script to spin up the particular vector database in Azure.
    - *[product_name]*_data_pipeline.ipynb

    Notebook to create table with vector field, implement index (HNSW etc.) and ingest the embeddings.

    - *[product_name]*_vector_query.ipynb

    Notebook to demonstrate vector search examples, like simple vector search, including metadata filtering, Cross column vector search, hybrid search,recall measurement etc.
