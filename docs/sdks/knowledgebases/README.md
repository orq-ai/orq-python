# KnowledgeBases
(*knowledge_bases*)

## Overview

### Available Operations

* [chunk_text](#chunk_text) - Chunk text

## chunk_text

Split large text documents into smaller, manageable chunks using different chunking strategies optimized for RAG (Retrieval-Augmented Generation) workflows. This endpoint supports multiple chunking algorithms including token-based, sentence-based, recursive, semantic, and specialized strategies.

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge_bases.chunk_text(request={
        "text": "The quick brown fox jumps over the lazy dog. This is a sample text that will be chunked into smaller pieces. Each chunk will maintain context while respecting the maximum chunk size.",
        "metadata": True,
        "strategy": "semantic",
        "chunk_size": 256,
        "threshold": 0.8,
        "embedding_model": "openai/text-embedding-3-small",
        "mode": "window",
        "similarity_window": 1,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.ChunkTextChunkingRequest](../../models/chunktextchunkingrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ChunkTextResponseBody](../../models/chunktextresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |