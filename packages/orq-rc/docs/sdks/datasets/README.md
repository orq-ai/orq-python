# Datasets
(*datasets*)

## Overview

### Available Operations

* [list](#list) - List datasets
* [create](#create) - Create a dataset
* [retrieve](#retrieve) - Retrieve a dataset
* [update](#update) - Update a dataset
* [delete](#delete) - Delete a dataset
* [list_datapoints](#list_datapoints) - List datapoints
* [create_datapoint](#create_datapoint) - Create a datapoint
* [retrieve_datapoint](#retrieve_datapoint) - Retrieve a datapoint
* [update_datapoint](#update_datapoint) - Update a datapoint
* [delete_datapoint](#delete_datapoint) - Delete a datapoint
* [clear](#clear) - Delete all datapoints

## list

Retrieves a paginated list of datasets for the current workspace. Results can be paginated using cursor-based pagination.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListDatasets" method="get" path="/v2/datasets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.list(limit=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListDatasetsResponseBody](../../models/listdatasetsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new dataset in the specified project.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDataset" method="post" path="/v2/datasets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.create(request={
        "display_name": "Neva.Raynor10",
        "path": "Default",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateDatasetRequestBody](../../models/createdatasetrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreateDatasetResponseBody](../../models/createdatasetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves a specific dataset by its unique identifier

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveDataset" method="get" path="/v2/datasets/{dataset_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.retrieve(dataset_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveDatasetResponseBody](../../models/retrievedatasetresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update

Update a dataset

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDataset" method="patch" path="/v2/datasets/{dataset_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.update(dataset_id="<id>", path="Default")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `display_name`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The display name of the dataset                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                 |
| `project_id`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The unique identifier of the project it belongs to                                                                                                                                                                                              |                                                                                                                                                                                                                                                 |
| `path`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists. | Default                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.UpdateDatasetResponseBody](../../models/updatedatasetresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## delete

Permanently deletes a dataset and all its datapoints. This action is irreversible.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDataset" method="delete" path="/v2/datasets/{dataset_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.datasets.delete(dataset_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_datapoints

Retrieves a paginated list of datapoints from a specific dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListDatasetDatapoints" method="get" path="/v2/datasets/{dataset_id}/datapoints" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.list_datapoints(dataset_id="<id>", limit=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                                                                     |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListDatasetDatapointsResponseBody](../../models/listdatasetdatapointsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_datapoint

Creates a new datapoint in the specified dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDatasetItem" method="post" path="/v2/datasets/{dataset_id}/datapoints" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.create_datapoint(dataset_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_body`                                                      | List[[models.RequestBody](../../models/requestbody.md)]             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_datapoint

Retrieves a datapoint object

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveDatapoint" method="get" path="/v2/datasets/{dataset_id}/datapoints/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.retrieve_datapoint(dataset_id="<id>", datapoint_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datapoint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveDatapointResponseBody](../../models/retrievedatapointresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update_datapoint

Update a datapoint

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDatapoint" method="patch" path="/v2/datasets/{dataset_id}/datapoints/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.datasets.update_datapoint(dataset_id="<id>", datapoint_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                                   | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | N/A                                                                                                                                            |
| `datapoint_id`                                                                                                                                 | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | N/A                                                                                                                                            |
| `inputs`                                                                                                                                       | Dict[str, *Any*]                                                                                                                               | :heavy_minus_sign:                                                                                                                             | The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported. |
| `messages`                                                                                                                                     | List[[models.UpdateDatapointMessages](../../models/updatedatapointmessages.md)]                                                                | :heavy_minus_sign:                                                                                                                             | A list of messages comprising the conversation so far                                                                                          |
| `expected_output`                                                                                                                              | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | N/A                                                                                                                                            |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[models.UpdateDatapointResponseBody](../../models/updatedatapointresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## delete_datapoint

Permanently deletes a specific datapoint from a dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDatapoint" method="delete" path="/v2/datasets/{dataset_id}/datapoints/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.datasets.delete_datapoint(dataset_id="<id>", datapoint_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datapoint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## clear

Delete all datapoints from a dataset. This action is irreversible.

### Example Usage

<!-- UsageSnippet language="python" operationID="ClearDataset" method="delete" path="/v2/datasets/{dataset_id}/clear" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.datasets.clear(dataset_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |