# Vector Database Best Practices

Vector databases are becoming an essential component of generative AI applications by enabling efficient information retrieval. For the applications to be successful, the information retrieval part has to be accurate, fast, and commercially viable.

- Accuracy: If the query returns wrong or incomplete information, the application will fail to provide meanigful answer.
- Latency: Many copilot or chatbot style applications require real-time conversational experience. The system has to be fast enough to cater to this experience.
- Cost: Vector queries can incur high computational resources, especially when executed at scale, leading to significant costs.

Here we are presenting some best practices which will help to ensure that vector databases are used effectively in generative AI applications.

## Appropriate use of index

For small number of records, an exhaustive k Nearest Neighbour (kNN) search may performs well. But when dealing with a large dataset, vector databases often employ advanced indexing techniques, such as Approximate Nearest Neighbor (ANN) algorithms, to accelerate the search process in high-dimensional spaces. Some popular ANN algorithms are HNSW, IVF, FLAT and LSH. 

Make sure to pick the right indexing technique depending on the use case.

## Use hybrid query

The advantage of vector search is finding information that’s conceptually similar to the search query, even if there are no keyword matches. On the other hand, keyword search is good at finding exact matches in the text. Hybrid search provides greater relevance than either approach alone by combining the precision of keyword search with the semantic matching of neural vectors.

In most cases it's better to use a hybrid query over pure vector search.

## Use metadata filtering

Metadata filtering is an important technique for vector search that can help improve the accuracy and relevance of search result. Metadata is additional information that describes the data objects stored in a vector database.

Filtering on metadata helps with both accuracy and latency and should be considered in most scenarios.

## Simpler data model

The data model plays a big role in the complexity and performance of the queries that the application will use. Sometimes it may be tempting to build multiple tables with relationships to store the data. But make sure it doesn't result in complex queries and multiple lookups which can degrade the performance. 

In many scenarios, it's better to use simpler data model (less joins, wide tables) for enabling simpler queries.

## Preprocess data

While generating embeddings, it's often important to preprocess the data to remove noise from the data and save tokens. Some common proprocessing techniques are -

- Data cleanup: Data cleanup helps to remove unnecesary text from the original dataset. It can be as simple as removing stop words from the soruce text to removing DOM elements from HTML source that has been web scraped.

- Data chunking: Data chunking is a technique used in vector databases to break down large data objects into smaller, more manageable parts called chunks. Chunking can be done using various techniques such as fixed-size chunks, variable-sized chunks based on content, or a combination of both.

- MultiVector generation: In addition to using smaller chunks for large docuemnts, sometimes it's also useful to summarize and generate embedding of the summary.

## Evaluate tools and parameters

There are many databases which support vector search. On top of that, the same technology can be configured in many different ways to support vector search. For example -

- Different types of indexing algorithms
- Different parameters to configure the indexing algorithm
- Different types of queries - pure vector search, hybrid search etc.
- Different similarity metrics - cosine, L2 etc.

Also all approaches have associated cost and latency consideration. A particular approach might return very accurate results, but at the same time be slow or very expensive. 

So it's very important to evaluate to pick the right vector database technology, query and parameters. Evaluating will involve creating an evaluation dataset, defining metrics and running experimentations. For details on evaluation, please check - [Evaluating Vector Databases](../evaluation/README.md).

## Data pipeline consideration

In most cases, there will be two types of data load to the vector database.

- Initial load: It can be as simple as a script that runs once to process and loads the embeddigns and metadata to the database.

- Incremental load: In most cases in real life, data changes and a data pipeline has to keep the data refreshed on a regular basis. Some key considerations for the data pipeline are -

    - How often to run the data pipeline: This is specially important if the database is serving a realtime app like a chat bot. Constantly upating a database that is connected to a production app may degrade the performance.

    - Consistency of the index: Some vector databases support real-time data ingestion and updates. On the otherhand, some vector databases will trigger a re-index for ingestion and updates. This may become a big issue for particualrly large datasets.

    - Deprecating expired data: Any record is part of the index as long they are not deleted from the table. So it's better to remove the records when they are deprecated. 