# Chunking Evaluation <!-- omit in toc -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Dataset](#dataset)
  - [QA Ground Truth Dataset](#qa-ground-truth-dataset)
  - [Raw Articles Dataset](#raw-articles-dataset)
- [Evaluation Metrics](#evaluation-metrics)
  - [RougeL](#rougel)
  - [In-top](#in-top)
- [Notebook Setup](#notebook-setup)
  - [Setting up the .env File](#setting-up-the-env-file)
  - [Setting up the Requirements](#setting-up-the-requirements)

## Overview

This end-to-end sample outlines how chunks of documents can be evaluated in a retrieval application.
This sample is fully contained in the [notebook.ipynb](./notebook.ipynb) file.
While the notebook also contains documentation, it is recommended to read this document in its entirety before running
the notebook.
This end-to-end sample performs the following steps:

1. Clear and create a new index in Azure AI Search (index name=**evaluation-index**)
1. Load the [pre-chunked markdown data](../../../code_samples/data/e2e_samples/chunking/embeddings.json) into the
AI Search index.
1. Perform a similarity search against the [QA dataset](../../../code_samples/data/e2e_samples/chunking/ground_truth/qa_dataset.csv)
to retrieve the top 3 chunks and persist the retrieved values.
1. Evaluate the results of the searched chunks according to the evaluation metrics described in [the evaluation section](#evaluation-metrics).

## Dataset

### QA Ground Truth Dataset

This compact [dataset](../../../code_samples/data/e2e_samples/chunking/ground_truth/qa_dataset.csv) is used to evaluate the
expected answer with the retrieved values from a vector database. The schema of this database includes the following fields:

- `id`: The id of the question.
- `question`: The question to query.
- `answer`: The expected answer.
- `source`: The document from which the question and answer were extracted.

This dataset helps in assessing the performance of a QA system by comparing its responses to the ground truth answers.

### Raw Articles Dataset

We included a set of [raw articles](../../../code_samples/data/e2e_samples/chunking/raw/) for chunking ingestion into the
vector retrieval database.

To simplify the process of chunking and embedding these documents, we have provided the [embeddings](../../../code_samples/data/e2e_samples/chunking/embeddings.json)
using the `text-embedding-ada-002` from OpenAI. Otherwise, you can generate new embeddings using this [notebook](../../../code_samples/common/generate_embeddings.ipynb).


## Evaluation Metrics

### RougeL

ROUGE-L (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) is a metric used in the field of
Natural Language Processing for evaluating the quality of summaries by comparing them to reference summaries.

The LCS is a measure of how many elements a sequence has in common with another, in the same order. RougeL is particularly
useful in tasks like text summarization where the goal is to generate a concise summary that captures the most important
information from a larger text.

### In-top

Checks if the expected source is contained in any of the chunks. If the source is found in at least 1 of the retrieved
chunks, the in-top is 1. If the source is not found in the retrieved chunks, the in-top is 0.

This metric is useful in tasks like document retrieval or question answering where the goal is to find the
most relevant information for a given query.

## Notebook Setup

### Setting up the .env File

Several environment variables are required to run this sample.
To get started, we recommend copying the [sample.env](./sample.env) file into a new file named `.env`.
Once this is done, you need to set the following environment variables:

- **AIS_ENDPOINT** [Required]: The Azure AI Search endpoint.
- **AIS_API_VERSION** [Required]: The Azure AI Search version (e.g., `2023-11-01`).
- **AIS_KEY** [Required]: The Azure AI Search key.
- **AOAI_ENDPOINT** [Required]: The Azure OpenAI endpoint.
- **AOAI_API_VERSION** [Required]: The Azure OpenAI version (e.g., `2023-09-01-preview`).
- **AZURE_OPENAI_KEY** [Required]: The Azure OpenAI key.
- **AOAI_EMBEDDING_DEPLOYED_MODEL** [Required]: The Azure OpenAI embedding model.

### Setting up the Requirements

Before you can run this project, you need to ensure that your environment meets the necessary requirements. Follow these
steps:

1. **Python**: This project requires Python 3.7 or higher. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Virtual Environment**: It's recommended to create a virtual environment to keep the project's dependencies isolated
from your global Python environment. You can create a virtual environment using `venv` or `conda`.

3. **Dependencies**: Install the project dependencies by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure you run this command while your virtual environment is activated.
