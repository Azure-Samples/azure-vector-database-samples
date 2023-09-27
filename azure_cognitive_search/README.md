# Azure Cognitive Search

This folder includes the notebooks to demonstrate vector search capabilities for text, documents and images using Azure Cognitive Search. There are two ways to use Azure Cognitive Search - REST API or Python SDK.

- REST Endpoint
  - [cognitive_search_rest_text.ipynb](./rest_endpoint_sample/cognitive_search_rest_text.ipynb)
  - [cognitive_search_rest_doc.ipynb](./rest_endpoint_sample/cognitive_search_rest_doc.ipynb)
  - [cognitive_search_rest_image.ipynb](./rest_endpoint_sample/cognitive_search_rest_image.ipynb)

- Python SDK
  - [cognitive_search_sdk_text.ipynb](./rest_endpoint_sample/cognitive_search_sdk_text.ipynb)
  - [cognitive_search_sdk_doc.ipynb](./rest_endpoint_sample/cognitive_search_sdk_doc.ipynb)
  - [cognitive_search_sdk_image.ipynb](./rest_endpoint_sample/cognitive_search_sdk_image.ipynb)

## Prerequisites

- Azure resources
  - Azure Cognitive Search
  - Azure OpenAI
  - Azure Computer Vision
- Create a conda environment to include all the python dependencies.
  - For REST endpoint samples - [cognitive_search_rest_conda.yml](./rest_endpoint_sample/cognitive_search_rest_conda.yml)
  - For Python SDK samples - [cognitive_search_sdk_conda.yml](./python_sdk_sample/cognitive_search_sdk_conda.yml)
- Create a *.env* file from the *.env-template* and populate it with all necessary keys.

## Datasets

- [text](../data/text/) - for text search sample
- [docs](../data/docs/) - for document search sample
- [images](../data/images/) - for image search sample
