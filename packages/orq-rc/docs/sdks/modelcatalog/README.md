# ModelCatalog

## Overview

### Available Operations

* [list](#list) - List the model catalog
* [list_offerings](#list_offerings) - List model catalog offerings
* [get](#get) - Retrieve a model catalog entry

## list

Returns every model orq offers, optionally filtered, searched and sorted. Use `starting_after` or `ending_before` to page through the collection.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCatalogList" method="get" path="/v2/model-catalog" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_catalog.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ModelCatalogListRequest](../../models/modelcataloglistrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ListModelCatalogResponse](../../models/listmodelcatalogresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_offerings

Returns catalog entries as a flat list of offerings. Pass `model` to narrow the list to every provider offering of one base model reference (for example `anthropic/claude-opus`).

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCatalogListOfferings" method="get" path="/v2/model-catalog/offerings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_catalog.list_offerings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ModelCatalogListOfferingsRequest](../../models/modelcataloglistofferingsrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListModelCatalogOfferingsResponse](../../models/listmodelcatalogofferingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a single catalog entry by its id, `<provider>/<model>` (for example `openai/gpt-4o`).

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCatalogGet" method="get" path="/v2/model-catalog/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_catalog.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | Catalog identifier, `<provider>/<model>` (for example `openai/gpt-4o`). |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetModelCatalogModelResponse](../../models/getmodelcatalogmodelresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |