# Chunking Evaluation <!-- omit in toc -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Dataset ](#dataset-)
- [Evaluation Metrics ](#evaluation-metrics-)
- [Notebook Setup ](#notebook-setup-)

## Overview

This end-to-end sample outlines how chunks of documents can be evaluated in a retrieval application.
This sample is fully contained in the [notebook.ipynb](./notebook.ipynb) file.
While the notebook also contains documentation, it is recommended to read this document in its entirety before running the notebook.
This end-to-end sample performs the following steps:

1. Clear and create a new index in Azure AI Search (index name=**evaluation-index**)
2. Load the [pre-chunked markdown data](../../../code_samples/data/e2e_samples/chunking/embeddings.json) into the AI Search index.
3. Perform a similarity search against the [QA dataset](../../../code_samples/data/e2e_samples/chunking/ground_truth/qa_dataset.csv) to retrieve the top 3 chunks and persist the retrieved values.
4. Evaluate the results of the searched chunks according to the evaluation metrics described in [the evaluation section](#evaluation-metrics).

## Dataset <!-- Oscar -->

## Evaluation Metrics <!-- Oscar -->

What metrics did we use
Why did we use the metrics

## Notebook Setup <!-- Paul -->

Ensure that the requirements are installed
Setting up the .env
