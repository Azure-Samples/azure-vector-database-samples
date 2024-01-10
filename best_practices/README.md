# Vector Database Best Practices

Vector databases are becoming an essential component of generative AI applications by enabling efficient information retrieval. For the applications to be successful, the information retrieval has to be accurate, fast, and commercially viable.

- Accuracy: If the query returns wrong or incomplete information, the application will fail to provide meanigful answer.
- Latency: Many copilot or chatbot style applications require real-time conversational experience. The system has to be fast enough to cater to this experience.
- Cost: Vector queries can incur high computational resources, especially when executed at scale, leading to significant costs.

Here are some best practices to consider to ensure the effective utilization of vector databases in generative AI applications.

### Embedded vs Client/Server

#### Embedded Vector Databases

**Overview**: An embedded vector database operates as a library or component within the host application. It doesn't run as a separate service or process. Instead, it's directly integrated into the application, much like SQLite in the relational database world.

**Advantages**:

- **Low Overhead**: There's no need for inter-process communication or network calls, which can speed up operations.
- **Simplicity**: No need for separate setup, configuration, or maintenance of a server.
- **Portability**: The database travels with the application, which can be especially useful for standalone applications or devices.

**When to Use**:

- When you need a lightweight, self-contained solution without the complexities of network configuration.
- For applications that need to be easily distributable without dependencies on external database servers.
- When performance is crucial, and the overhead of network communication should be eliminated.

#### Client/Server Vector Databases

**Overview**: In a client/server setup, the vector database runs as a standalone server or service, which clients connect to, typically over a network. Examples include Azure AI Search, PostgreSQL and others.

**Advantages**:

- **Scalability**: Can handle large volumes of data and requests by distributing the load, often supporting clustering and replication.
- **Concurrency**: Built to handle multiple concurrent requests efficiently.
- **Centralization**: A single source of truth, making backups, updates, and maintenance centralized.
- **Security**: Offers more robust security features, including access controls, encryption, and network security.

**When to Use**:

- When you're building a system with multiple applications or services that need to access the same vector database.
- For larger datasets that may need distributed storage and retrieval capabilities.
- When there's a need for high availability, backups, replication, and other advanced database features.
- If you want to keep the data layer separate from the application layer, possibly for security, modularity, or scalability reasons.

### Choose the right index

For small number of records, an exhaustive k Nearest Neighbour (kNN) search may performs well. But when dealing with a large dataset, vector databases often employ advanced indexing techniques, such as Approximate Nearest Neighbor (ANN) algorithms, to accelerate the search process in high-dimensional spaces. Some popular ANN algorithms are HNSW, IVF, FLAT and LSH. Please refer to this site for [ANN Benchmarks](https://ann-benchmarks.com/).

Make sure to pick the right indexing algorithm depending on the use case. Please refer to the [Code Samples](../code_samples/README.md) section to learn about how to create index in different products.

### Use hybrid query

The advantage of vector search is finding information that’s conceptually similar to the search query, even if there are no keyword matches. On the other hand, keyword search is good at finding exact matches in the text. Hybrid search provides greater relevance than either approach alone by combining the precision of keyword search with the semantic matching of neural vectors.

In most cases it's better to use a hybrid query over pure vector search. Please refer to the [Code Samples](../code_samples/README.md) section to learn about how to write hybrid queries for different products.

### Use metadata filtering

Metadata filtering is an important technique for vector search that can help improve the accuracy and relevance of search result. Metadata is additional information that describes the data objects stored in a vector database.

Filtering on metadata helps with both accuracy and latency and should be considered in most scenarios. Please refer to the [Code Samples](../code_samples/README.md) section to learn about how apply metadata filtering for different products.

### Simpler data model

The data model plays a big role in the complexity and performance of the queries that the application will use. Sometimes it may be tempting to build multiple tables with relationships to store the data. But make sure it doesn't result in complex queries and multiple lookups which can degrade the performance. 

In many scenarios, it's better to use simpler data model (less joins, wide tables) for enabling simpler queries.

### Preprocess data

While generating embeddings, it's often important to preprocess the data to remove noise from the data and save tokens. Some common proprocessing techniques are -

- Data cleanup: Data cleanup helps to remove unnecesary text from the original dataset. It can be as simple as removing stop words from the soruce text to removing DOM elements from HTML source that has been web scraped.

- Data chunking: Data chunking is a technique used in vector databases to break down large data objects into smaller, more manageable parts called chunks. Chunking can be done using various techniques such as fixed-size chunks, variable-sized chunks based on content, or a combination of both.

- MultiVector generation: In addition to using smaller chunks for large docuemnts, sometimes it's also useful to summarize and generate embedding of the summary.

### Evaluate tools and parameters

There are many databases which support vector search. On top of that, the same technology can be configured in many different ways to support vector search. For example -

- Different types of indexing algorithms
- Different parameters to configure the indexing algorithm
- Different types of queries - pure vector search, hybrid search etc.
- Different similarity metrics - cosine, L2 etc.

Also all approaches have associated cost and latency consideration. A particular approach might return very accurate results, but at the same time be slow or very expensive. 

So it's very important to evaluate to pick the right vector database technology, query and parameters. Evaluating will involve creating an evaluation dataset, defining metrics and running experimentations. For details on evaluation, please check - [Evaluating Vector Databases](../evaluation/README.md).

### Data pipeline consideration

In most cases, there will be two types of data load to the vector database.

- Initial load: It can be as simple as a script that runs once to process and loads the embeddigns and metadata to the database.

- Incremental load: In most cases in real life, data changes and a data pipeline has to keep the data refreshed on a regular basis. Some key considerations for the data pipeline are -

    - How often to run the data pipeline: This is specially important if the database is serving a realtime app like a chat bot. Constantly upating a database that is connected to a production app may degrade the performance.

    - Consistency of the index: Some vector databases support real-time data ingestion and updates. On the otherhand, some vector databases will trigger a re-index for ingestion and updates. This may become a big issue for particualrly large datasets.

    - Deprecating expired data: Any record is part of the index as long they are not deleted from the table. So it's better to remove the records when they are deprecated. 