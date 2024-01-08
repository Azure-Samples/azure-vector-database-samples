# Evaluating Vector Databases

## Goal

Different samples of vector search evaluation.

## TREC Evaluation

Uses [NIST TREC Tools](https://trec.nist.gov/) to evaluate vector search (in this case Postgres vector search, but the DB can be substituted for any variant).

Requires:​

- A set of queries, with ground truth ranked result set of relevant search results​
- A result set from your query engine (a vector db) with ranked results and a system-specific scoring (like distance measure)

Results in a series of evaluation metrics such as:

- Mean Average Precision (MAP)​, Average precision score for each relevant document​
- Geometric Mean Average Precision​, Geometric mean of MAP​
- R-Precision​, How many relevant docs retrieved before an irrelevant result​
- Reciprocal Rank​, Rank of first relevant document (R), 1/R

This example uses a very small, fake dataset meant to show working code. Suggest using either:

1. A groundtruth evaluation dataset relevant to the application's domain
2. A large search dataset such as [MS Marco](https://microsoft.github.io/msmarco/)
