# Batches

## Overview

### Available Operations

* [list](#list) - List batches
* [create](#create) - Create batch
* [retrieve](#retrieve) - Retrieve batch
* [cancel](#cancel) - Cancel batch
* [download_results](#download_results) - Download batch results

## list

Lists the batches in the caller's projects, most recent first. Filter by status and endpoint, or page with `after` and `before`; the two cursors are exclusive. Results are scoped to the projects the API key can reach.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-batches" method="get" path="/v3/router/batches" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.batches.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                            | *Optional[int]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Maximum number of batches to return, 1 to 100. Defaults to 20.                                                                                     |
| `after`                                                                                                                                            | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Cursor: return batches older than this batch id, still newest first.                                                                               |
| `before`                                                                                                                                           | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Cursor: return batches newer than this batch id. Cannot be combined with after.                                                                    |
| `search`                                                                                                                                           | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Case-insensitive match on batch id, model, or endpoint.                                                                                            |
| `status`                                                                                                                                           | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Comma-separated statuses to include: validating, in_progress, finalizing, completed, failed, expired, cancelling, cancelled.                       |
| `endpoint`                                                                                                                                         | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | Comma-separated endpoints to include: /v1/responses, /v1/chat/completions, /v1/embeddings, /v1/completions, /v1/moderations, /v3/router/decisions. |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.ListBatchesResponseBody](../../models/listbatchesresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.ListBatchesBatchesResponseBody            | 400                                              | application/json                                 |
| models.ListBatchesBatchesResponseResponseBody    | 401                                              | application/json                                 |
| models.ListBatchesBatchesResponse500ResponseBody | 500                                              | application/json                                 |
| models.APIDefaultError                           | 4XX, 5XX                                         | \*/\*                                            |

## create

Creates a batch from an uploaded JSONL file whose purpose is `batch`. Each line is sent to `endpoint` with its own request body, without the throughput limits of real-time traffic. Provider batches run through the provider's batch service at its batch rates; `/v3/router/decisions` batches run on the deployment's workers. See the [Batches guide](/ai-gateway/features/batches) for input file format, supported endpoints, and result files.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-batch" method="post" path="/v3/router/batches" example="chat_completions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.batches.create(completion_window="24h", endpoint="/v1/chat/completions", input_file_id="file-abc123", metadata={
        "job": "nightly-eval",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `completion_window`                                                                 | [models.CompletionWindow](../../models/completionwindow.md)                         | :heavy_check_mark:                                                                  | Time window the batch runs in. Only 24h is supported.                               |
| `endpoint`                                                                          | [models.Endpoint](../../models/endpoint.md)                                         | :heavy_check_mark:                                                                  | Endpoint each line is sent to. The batch model must support it.                     |
| `input_file_id`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | ID of an uploaded JSONL file whose purpose is batch.                                |
| `metadata`                                                                          | Dict[str, *str*]                                                                    | :heavy_minus_sign:                                                                  | Up to 16 key/value pairs, keys up to 64 characters and values up to 512.            |
| `output_expires_after`                                                              | [Optional[models.PublicBatchExpiresAfter]](../../models/publicbatchexpiresafter.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreateBatchResponseBody](../../models/createbatchresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.CreateBatchBatchesResponseBody            | 400                                              | application/json                                 |
| models.CreateBatchBatchesResponseResponseBody    | 401                                              | application/json                                 |
| models.CreateBatchBatchesResponse404ResponseBody | 404                                              | application/json                                 |
| models.CreateBatchBatchesResponse500ResponseBody | 500                                              | application/json                                 |
| models.APIDefaultError                           | 4XX, 5XX                                         | \*/\*                                            |

## retrieve

Retrieves one batch, including its status, per-line request counts, and the output and error file IDs once they exist.

### Example Usage

<!-- UsageSnippet language="python" operationID="retrieve-batch" method="get" path="/v3/router/batches/{batch_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.batches.retrieve(batch_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The batch's identifier, as returned from create.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveBatchResponseBody](../../models/retrievebatchresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.RetrieveBatchBatchesResponseBody            | 400                                                | application/json                                   |
| models.RetrieveBatchBatchesResponseResponseBody    | 401                                                | application/json                                   |
| models.RetrieveBatchBatchesResponse404ResponseBody | 404                                                | application/json                                   |
| models.RetrieveBatchBatchesResponse500ResponseBody | 500                                                | application/json                                   |
| models.APIDefaultError                             | 4XX, 5XX                                           | \*/\*                                              |

## cancel

Requests cancellation of a running batch and returns it with the status it holds at that moment. A batch that already reached a terminal status is returned unchanged. Poll the batch until the status is `cancelled`.

### Example Usage

<!-- UsageSnippet language="python" operationID="cancel-batch" method="post" path="/v3/router/batches/{batch_id}/cancel" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.batches.cancel(batch_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The batch's identifier, as returned from create.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CancelBatchResponseBody](../../models/cancelbatchresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.CancelBatchBatchesResponseBody            | 400                                              | application/json                                 |
| models.CancelBatchBatchesResponseResponseBody    | 401                                              | application/json                                 |
| models.CancelBatchBatchesResponse404ResponseBody | 404                                              | application/json                                 |
| models.CancelBatchBatchesResponse500ResponseBody | 500                                              | application/json                                 |
| models.APIDefaultError                           | 4XX, 5XX                                         | \*/\*                                            |

## download_results

Downloads the JSONL result file of a batch that reached a terminal status. `file=output` returns the successful responses, `file=errors` the per-line failures that have an error file. Each line follows the OpenAI batch result format.

### Example Usage

<!-- UsageSnippet language="python" operationID="download-batch-results" method="get" path="/v3/router/batches/{batch_id}/results" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.batches.download_results(batch_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `batch_id`                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                            | The batch's identifier, as returned from create.                                                                                                                                                                                                                              |
| `file`                                                                                                                                                                                                                                                                        | [Optional[models.QueryParamFile]](../../models/queryparamfile.md)                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                            | Which result file to download: output holds successful responses, errors holds the per-line failures. Defaults to output, and answers the errors file when the batch produced no output file. Requesting errors on a batch with no error file returns 409 output_unavailable. |
| `retries`                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                           |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.DownloadBatchResultsResponseBody                   | 400                                                       | application/json                                          |
| models.DownloadBatchResultsBatchesResponseBody            | 401                                                       | application/json                                          |
| models.DownloadBatchResultsBatchesResponseResponseBody    | 404                                                       | application/json                                          |
| models.DownloadBatchResultsBatchesResponse409ResponseBody | 409                                                       | application/json                                          |
| models.DownloadBatchResultsBatchesResponse500ResponseBody | 500                                                       | application/json                                          |
| models.APIDefaultError                                    | 4XX, 5XX                                                  | \*/\*                                                     |