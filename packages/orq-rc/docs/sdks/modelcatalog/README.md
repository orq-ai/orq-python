# ModelCatalog

## Overview

### Available Operations

* [list](#list) - List the model catalog
* [list_offerings](#list_offerings) - List model catalog offerings
* [get](#get) - Retrieve a model catalog entry

## list

Returns every model orq offers, optionally filtered, searched and sorted. Deprecated models are never listed; fetch one directly by id to inspect it. Unset `limit` returns the whole catalog. Use `starting_after` or `ending_before` to page through the collection.

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

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `limit`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Page size, 1–1000. Unset returns every non-deprecated model in one response.               |
| `starting_after`                                                                           | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for forward pagination. Set to the `id` of the last item from<br/> the previous page. |
| `ending_before`                                                                            | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for backward pagination. Set to the `id` of the first item<br/> from the previous page. |
| `provider`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by catalog provider key. Repeat to match any of several<br/> providers.             |
| `endpoint`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by API endpoint. Repeat to match any of several endpoints.                          |
| `input_modality`                                                                           | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by input modality. Repeat to match any of several modalities.                       |
| `output_modality`                                                                          | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by output modality. Repeat to match any of several modalities.                      |
| `location`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by region. Repeat to match any of several regions.                                  |
| `feature`                                                                                  | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by normalized feature name. Repeat to match any of several<br/> features.           |
| `supported_parameter`                                                                      | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by supported parameter key. Repeat to match any of several<br/> parameters.         |
| `tier`                                                                                     | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by supported service tier. Repeat to match any of several<br/> tiers.               |
| `offering_of`                                                                              | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Filter to offerings of one base model reference, `<developer>/<stem>`.                     |
| `search`                                                                                   | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Case-insensitive substring search over `id`, `name` and `description`.                     |
| `sort_by`                                                                                  | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Field to sort by.                                                                          |
| `order`                                                                                    | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Sort order. Defaults to ascending.                                                         |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[models.ListModelCatalogResponse](../../models/listmodelcatalogresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_offerings

Returns every provider offering of one base model, identified by `<developer>/<stem>` (for example `anthropic/claude-opus-4-7`). Deprecated models are never listed.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCatalogListOfferings" method="get" path="/v2/model-catalog/{model}/offerings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_catalog.list_offerings(model="Cruze")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `model`                                                                                    | *str*                                                                                      | :heavy_check_mark:                                                                         | Base model reference, `<developer>/<stem>` (for example<br/> `anthropic/claude-opus-4-7`). |
| `limit`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Page size, 1–1000. Unset returns every non-deprecated model in one response.               |
| `starting_after`                                                                           | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for forward pagination. Set to the `id` of the last item from<br/> the previous page. |
| `ending_before`                                                                            | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for backward pagination. Set to the `id` of the first item<br/> from the previous page. |
| `provider`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by catalog provider key. Repeat to match any of several<br/> providers.             |
| `endpoint`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by API endpoint. Repeat to match any of several endpoints.                          |
| `input_modality`                                                                           | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by input modality. Repeat to match any of several modalities.                       |
| `output_modality`                                                                          | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by output modality. Repeat to match any of several modalities.                      |
| `location`                                                                                 | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by region. Repeat to match any of several regions.                                  |
| `feature`                                                                                  | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by normalized feature name. Repeat to match any of several<br/> features.           |
| `supported_parameter`                                                                      | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by supported parameter key. Repeat to match any of several<br/> parameters.         |
| `tier`                                                                                     | List[*str*]                                                                                | :heavy_minus_sign:                                                                         | Filter by supported service tier. Repeat to match any of several<br/> tiers.               |
| `search`                                                                                   | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Case-insensitive substring search over `id`, `name` and `description`.                     |
| `sort_by`                                                                                  | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Field to sort by.                                                                          |
| `order`                                                                                    | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Sort order. Defaults to ascending.                                                         |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[models.ListModelCatalogOfferingsResponse](../../models/listmodelcatalogofferingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a single catalog entry by its id, `<provider>/<model>` (for example `openai/gpt-4o`). Unlike the list endpoints this also resolves deprecated models; check `deprecated` and `deprecation` on the response.

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