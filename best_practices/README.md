# Vector Search Best Practices

Vector search is  becoming an essential component of generative AI applications by enabling efficient information retrieval. For the applications to be successful, the information retrieval has to be accurate, fast, and commercially viable.

- Accuracy: If the query returns wrong or incomplete information, the application will fail to provide meanigful answer.
- Latency: Many copilot or chatbot style applications require real-time conversational experience. The system has to be fast enough to cater to this experience.
- Cost: Vector queries can incur high computational resources, especially when executed at scale, leading to significant costs.


Scenarios for Vector Search in Azure AI Search include:

1. **Vector Database**: Use Azure AI Search to store data for long-term memory, knowledge bases, or as grounding data for Retrieval Augmented Generation (RAG) architecture, or any application utilizing vectors.
2. **Similarity Search**: Encode text using embedding models like OpenAI embeddings retrieve documents with queries encoded as vectors.
3. **Multimodal Search**: Encode images and text using multimodal embeddings (e.g., OpenAI CLIP or GPT-4 Turbo with Vision in Azure OpenAI) and query an embedding space composed of vectors from both content types.
4. **Hybrid Search**: Execute vector and keyword queries in the same request. Vector support is at the field level, with queries executing in parallel and results merged into a single response. Optionally, add semantic ranking for more accuracy using language models.
5. **Multilingual Search**: Provide search in users' languages using embedding models and chat models trained in multiple languages. Supplement with Azure AI Search's multi-language capabilities for nonvector content in hybrid search scenarios.
6. **Filtered Vector Search**: Query includes a vector query and a filter expression, applicable to text and numeric fields for metadata filters or including/excluding search results based on filter criteria. Filter can be processed before or after the vector query executes

### Azure Search and Embeddings

Embeddings is a type of vector representation created by machine learning models, capture semantic meaning or representations of content such as text or images. These high-dimensional vectors position similar items close together in an embedding space, aiding in efficient vector search.

To ensure effective vector search, it's crucial to choose a well-trained embedding model that accurately captures the meaning of documents and queries. Azure AI Search allows flexibility in selecting the embedding model, whether pre-existing or custom-trained.

The embedding space serves as the corpus for vector queries, where similar items are clustered together. **Nearest neighbour** search for example is a technique used in vector search that identifies vectors closest to the query vector, quantifying similarity between items.

Azure AI Search supports two nearest neighbour algorithms: **Hierarchical Navigable Small World (HNSW)** and **Exhaustive K-nearest neighbours (KNN)**. HNSW, optimized for high-recall, low-latency applications, organizes data points into a hierarchical graph structure. KNN calculates distances between the query vector and all data points, suitable for smaller datasets.

Additionally, Azure AI Search employs Approximate Nearest Neighbours search (ANN) algorithms, like HNSW, for scalable and faster retrieval of approximate nearest neighbours, balancing accuracy and efficiency in information retrieval applications.

### Embedded Vector Databases

**Overview**: An embedded vector database operates as a library or component within the host application. It doesn't run as a separate service or process. Instead, it's directly integrated into the application, much like SQLite in the relational database world.

**Advantages**:

- **Low Overhead**: There's no need for inter-process communication or network calls, which can speed up operations.
- **Simplicity**: No need for separate setup, configuration, or maintenance of a server.
- **Portability**: The database travels with the application, which can be especially useful for standalone applications or devices.

**When to Use**:

- When you need a lightweight, self-contained solution without the complexities of network configuration.
- For applications that need to be easily distributable without dependencies on external database servers.
- When performance is crucial, and the overhead of network communication should be eliminated.

### Client/Server Vector Databases

**Overview**: In a client/server setup, the vector database runs as a standalone server or service, which clients connect to, typically over a network. Examples include Azure AI Search, PostgreSQL and others.

Implementing and managing vector databases effectively involves several best practices to ensure efficiency and reliability, especially in domains like machine learning, natural language processing, and image and video processing.

1. **Understand data requirements**: Before implementation, understand the data type, size, complexity, and update frequency to select the most suitable vector database.
2. **Choose the right vector database**: Consider factors like scalability, performance, indexing capabilities, storage options, and integration ease when selecting from options Pinecone, Milvus, Redis,Postgres and MongoDB etc.
3. **Optimize hardware and software**: Select hardware and software optimized for vector processing, including cloud providers with specialized hardware accelerators like GPU instances.
4. **Focus on scalability**: Design a database architecture and choose scalable hardware to accommodate increased data volumes as the organization grows.
5. **Ensure data security**: Implement robust security measures, including access controls, data encryption, and regular monitoring for vector databases.

The cost of implementing and maintaining vector databases can vary based on data scale and application requirements. Factors contributing to costs include hardware, software, maintenance, and expertise. Pricing structures vary among providers, with some offering scalable cloud-native solutions and others requiring upfront investment in hardware and infrastructure.

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

### Vector Search Algorithms and Index:

1. - **Exhaustive K-nearest neighbours (KNN) and Hierarchical Navigable Small World (HNSW)** are some of the most common .

     **Exhaustive KNN** scans the entire vector space performing a brute-force search , while **HNSW** performs an approximate nearest neighbour search (**ANN**). The **Graph-based (HNSW)** indexing method that utilizes a hierarchical graph architecture to index the vectors. Also unlike algorithms like NSW, HNSW maintains a hierarchical structure of embeddings, leading to a higher memory footprint and offers various tuneable parameters, requiring careful adjustment to enhance performance effectively which can be challenge when implementing from scratch. 

     - **Comparing KNN and HSNW - Vector Query Execution**:

       - As queries navigate the embedding space to find vectors closest to the query vector.
       - Exhaustive KNN searches "all neighbours," while HNSW employs its graph for more targeted search.

     - **Considerations when creating and Navigating the HNSW Graph**:

       - **During indexing**, the HNSW graph is constructed for efficient nearest neighbour search.
       - Query time involves traversing the graph, considering candidate nodes closer to the query vector.

     - **Tips for Relevance Tuning**:

       - Experiment with query configuration, chunk size, and overlap.

       - Adjust parameters like efConstruction for HNSW.

       - Increase the number of results (k) for better input into downstream models.

       - Consider hybrid queries with semantic ranking for improved relevance.

         

   - **Navigable Small World (NSW)**: it is a graph-based approach crafted to identify approximate nearest neighbours within a dataset. In this algorithm, data points are depicted as nodes in a graph, with each node linked to a predetermined group of neighbouring nodes.

   - **Linear Search Algorithm (Flat Indexing)**: This method involves comparing the query vector with every vector stored in the database sequentially. 

   - **Cluster-based Algorithm (IVF)**: Inverted File is a clustering technique that uses k-means clustering to group vectors into clusters. When a query vector is provided, it calculates the distance between the query vector and the centroids of each cluster, then searches for nearest neighbors in the cluster closest to the query vector. This reduces query time significantly.

   - **Quantization (Scalar and Product Quantization)**: This technique reduces the memory footprint of large embeddings by reducing their precision.

   - **When use the different approaches**:

     - **KNN** : As KNN calculates the distances between all pairs of data points and finds the exact `k` nearest neighbours for a query point. it is suitable for scenarios prioritizing high recall, especially with small to medium datasets as  it's computationally intensive,.

     - **HNSW**: with its hierarchical graph structure, is recommended for most scenarios due to its efficiency with larger datasets.
     - **NSW**: it would be suitable for small datasets ranging from a few hundred to thousands of data points
     - **Linear Search Algorithm** : it is straightforward and efficient for small datasets.
     - **Cluster-based Algorithm (IVF)**: suitable for datasets that exhibit high dimensionality, sparsity, or natural groupings.
     - **Quantization (Scalar and Product Quantization)**: are suitable for datasets with high dimensionality, large memory footprints, approximate search requirements, and a need for efficient storage.

   - **Considerations for the decision**:

     - **Latency and Throughput**: The deployment needs to consider the required latency for serving queries and the expected throughput. These factors determine the scalability and responsiveness of the system.

     - **Accuracy Impact**: Introducing ANNS may lead to a loss in accuracy compared to exact search. Understanding the acceptable level of accuracy loss for the specific use case is vital. This can be evaluated by comparing the output of exact and approximate searches and measuring the overlap between them.

     - **Production Deployment Cost**: The decision also involves assessing the infrastructure requirements and associated costs. This includes determining the number of servers needed for deployment.

       

Make sure to pick the right indexing algorithm depending on the use case. Please refer to the [Code Samples](../code_samples/README.md) section to learn about how to create index in different products.

### Hybrid Query

Hybrid search combines keyword queries with vector queries in a single request. Hybrid queries enable full text and vector search in parallel, supporting various query capabilities. Filters can be applied before or after query execution.

Semantic hybrid search integrates vector search with semantic ranking for improved relevance, with options for filters. Overall, hybrid search enhances search capabilities by combining keyword and vector queries effectively.

In some scenarios use a hybrid query would be suitable over pure vector search. Specially for applications that require a combination of keyword-based and vector-based search capabilities to deliver accurate, relevant, and flexible search results to users

**About Hybrid Query:**

- All results, including vectors in retrievable fields, are returned in plain text.
- Numeric vectors aren't useful in search results, choose fields in the index as a proxy for the vector match.
- For instance, if the index includes "descriptionVector" and "descriptionText" fields, the query may match on "descriptionVector" while displaying "descriptionText" in the search result.
- The select parameter can be used to specify only human-readable fields in the results.
- When using Semantic Search with ranking be aware: 
  - It's a best practice to set both "k" and "top" to at least 50:
    - `"k": n` results for vector-only queries
    - `"top": n` results for hybrid queries that include a "search" parameter
  - The filter mode affects the number of results available for semantic reranking. Provide semantic ranker with maximum documents (50) for optimal performance and use the prefilter or postfilter with the rank,  if too selective, it might be underserving the semantic ranker by giving it fewer than 50 documents.
    - Prefilter - Applied before query execution and reduces search area to a specified number of documents, for example returning top k=50 matches.
    - Postfilter - Applied after query execution. If initial vector query returns k=50 matches postfilter is applied to these results.

Please refer to the [Code Samples](../code_samples/README.md) section to learn about how to write hybrid queries for different products.

### Metadata filtering

Metadata filtering is an important technique for vector search that can help improve the accuracy and relevance of search result. Metadata is additional information that describes the data objects stored in a vector database.

Filtering on metadata helps with both accuracy and latency and should be considered in most scenarios. Please refer to the [Code Samples](../code_samples/README.md) section to learn about how apply metadata filtering for different products.

### Simpler Data model

The data model plays a big role in the complexity and performance of the queries that the application will use. Sometimes it may be tempting to build multiple tables with relationships to store the data. But make sure it doesn't result in complex queries and multiple lookups which can degrade the performance. 

In many scenarios, it's better to use simpler data model (less joins, wide tables) for enabling simpler queries.

### Pre-process data

While generating embeddings, it's often important to pre-process the data to remove noise from the data and save tokens. Some common proprocessing techniques are -

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

### Query Optimization

- Implement query optimization techniques to enhance search performance. This includes strategies like query caching, query rewriting, and query expansion to refine search results and reduce latency.
- Utilize query profiling and monitoring tools to identify and address bottlenecks in the search process, ensuring efficient query execution.

### Model Selection and Fine-Tuning

- Experiment with different pre-trained embedding models (e.g., BERT, Word2Vec, or GloVe) and fine-tune them on domain-specific data to optimize search performance and relevance for specific use cases or industries.
- Train models with sufficiently large and representative datasets to capture domain variance.
- Regularly update models with new data to keep pace with language and context evolution

### Monitoring and Alerting:

- Set up comprehensive monitoring and alerting systems to detect anomalies, performance degradation, or security threats in the vector database environment. This proactive approach helps ensure system reliability, availability, and data integrity.
- Define clear evaluation metrics to measure embedding performance and accuracy in downstream tasks.

### Privacy and Compliance:

- Address privacy and compliance requirements by implementing techniques such as differential privacy, federated learning, or data anonymization to protect sensitive information while still enabling effective vector search functionality.
- Implement strict access controls and encryption measures to safeguard vector databases.

### References:

[Microsoft Learn Vector Search Overview](https://learn.microsoft.com/azure/search/vector-search-overview)

[Microsoft Learn Vector Search Rank](https://learn.microsoft.com/azure/search/vector-search-ranking)

[Microsoft Learn  Hybrid Query](https://learn.microsoft.com/azure/search/hybrid-search-how-to-query)

[ANN Benchmarks](https://ann-benchmarks.com/).

[Ignite Apache](https://ignite.apache.org/docs/latest/machine-learning/binary-classification/ann#:~:text=The%20difference%20between%20KNN%20and,small%20subset%20of%20candidates%20points)



