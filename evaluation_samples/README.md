# Evaluating Vector Databases <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [Goal](#goal)
- [Samples](#samples)
  - [TREC Evaluation](#trec-evaluation)
  - [Document Chunking Evaluation](#document-chunking-evaluation)

## Goal

Different samples of vector search evaluation.

## Samples

### TREC Evaluation

The [TREC evaluation sample](./evaluation_trec/trec-evaluation.ipynb)
uses [NIST TREC Tools](https://trec.nist.gov/) to evaluate vector search
(in this case Postgres vector search, but the DB can be substituted for any variant).

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

### Document Chunking Evaluation

The [document chunking sample](./evaluation_doc_chunking/README.md)
outlines different evalution techniques used when evaluating search for chunked documents.
A few evaluation metrics used to evaluate searching for chunked documents include:

- RougeL: (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) is a metric used in the field
of Natural Language Processing for evaluating the quality of summaries by comparing them to reference summaries.
- In-Top: Checks if the expected source is contained in any of the chunks. If the source is found in atleast 1 of the retrieved
chunks, the in-top is 1. If the source is not found in the retrieved chunks, the in-top is 0.

This sample is a complete end-to-end solution that leverages [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/),
[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service/?ef_id=_k_Cj0KCQiAnfmsBhDfARIsAM7MKi1FGNLVMVC_qzqNpEQcRJXIRcKX4X64hsMWIcsgyjkICSNfAIwGblUaAscNEALw_wcB_k_&OCID=AIDcmm5edswduu_SEM__k_Cj0KCQiAnfmsBhDfARIsAM7MKi1FGNLVMVC_qzqNpEQcRJXIRcKX4X64hsMWIcsgyjkICSNfAIwGblUaAscNEALw_wcB_k_&gad_source=1&gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi1FGNLVMVC_qzqNpEQcRJXIRcKX4X64hsMWIcsgyjkICSNfAIwGblUaAscNEALw_wcB),
and a sample QA dataset based on a very small subset of the [ISE playbook](https://github.com/microsoft/code-with-engineering-playbook).
For more information on the sample please review the [project-level readme](./chunking_evaluation/README.md).
