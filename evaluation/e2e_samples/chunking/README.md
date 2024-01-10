# Chunking Evaluation <!-- omit in toc -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Dataset ](#dataset-)
- [Evaluation Metrics ](#evaluation-metrics-)
- [Notebook Setup](#notebook-setup)
  - [Setting up the .env File](#setting-up-the-env-file)
  - [Setting up the Requirements](#setting-up-the-requirements)

## Overview

This end-to-end sample outlines how chunks of documents can be evaluated in a retrieval application.
This sample is fully contained in the [notebook.ipynb](./notebook.ipynb) file.
While the notebook also contains documentation, it is recommended to read this document in its entirety before running the notebook.
This end-to-end sample performs the following steps:

1. Clear and create a new index in Azure AI Search (index name=**evaluation-index**)
1. Load the [pre-chunked markdown data](../../../code_samples/data/e2e_samples/chunking/embeddings.json) into the AI Search index.
1. Perform a similarity search against the [QA dataset](../../../code_samples/data/e2e_samples/chunking/ground_truth/qa_dataset.csv) to retrieve the top 3 chunks and persist the retrieved values.
1. Evaluate the results of the searched chunks according to the evaluation metrics described in [the evaluation section](#evaluation-metrics).

## Dataset <!-- Oscar -->

## Evaluation Metrics <!-- Oscar -->

What metrics did we use
Why did we use the metrics

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

Before you can run this project, you need to ensure that your environment meets the necessary requirements. Follow these steps:

1. **Python**: This project requires Python 3.7 or higher. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Virtual Environment**: It's recommended to create a virtual environment to keep the project's dependencies isolated from your global Python environment. You can create a virtual environment using `venv` or `conda`.

3. **Dependencies**: Install the project dependencies by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure you run this command while your virtual environment is activated.
