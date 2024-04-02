# Adaptive Retrieval Evaluation

## Goal

Embrace trade-offs in different vector search options to optimize performance/cost.

## Matryoshka Representation Learning

From blog on (Matryoshka Representation Learning)[https://aniketrege.github.io/blog/2024/mrl/]:

- OpenAI and others have created embedding models that allow for shortened vectors
- Like a (Matryoshka doll)[https://en.wikipedia.org/wiki/Matryoshka_doll], the same
model comes with a range of smaller embedding options

(This example)[https://huggingface.co/spaces/Xenova/adaptive-retrieval-web] using the
 (Nomic Embeding model)[https://huggingface.co/nomic-ai/nomic-embed-text-v1.5] shows how
 paramaterising the amount of dimensions for an embedding
 vector affects the retrieval of information.

## Binary Vectors

From blog (My binary vector search is better than your FP32 vectors)[https://blog.pgvecto.rs/my-binary-vector-search-is-better-than-your-fp32-vectors#heading-what-is-a-binary-vector],
A binary vector is just a regular vector where each element is a 0 or 1.

## Adaptive Retrieval

Say you have a large dataset to conduct a RAG Pattern application over. In order
to best save on costs, you may decide that an open sourced, self hosted model is
going to save you the most money. However, there's still the cost of maintaining
your search retrieval system:

1) Storing large vectors
2) Computing expensive vector operations


From (Optimization: adaptive retrieval)[https://blog.pgvecto.rs/my-binary-vector-search-is-better-than-your-fp32-vectors#heading-optimization-adaptive-retrieval],
we can optimize both with the following steps:

1) Use the smallest needed dimension parameter from your embedding model. Analyze
apriori your dataset and determine a tradeoff between high dimesionality performance
vs costs. Using a Matryoshka model can drastically reduce storage costs by reducing
the size of the vectors needed to embed your data.

2) Instead of relying on ANN vector search over the entire dataset, do the following
   procedure:

- Turn your query vector into a binary vector, and compare against a binary representation
of your existing vector data. If you're looking for a top 10 result set, query
2 or 10 times as much data as you need in this phase.
- Next, using the larger result set, perform KNN to rerank your dataset using whatever
dimension sized vectors from step your Matryoshka embedding model.
