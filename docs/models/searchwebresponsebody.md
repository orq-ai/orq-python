# SearchWebResponseBody

Search completed. Results may be empty or fewer than the requested limit.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `items`                                                                                             | List[[models.SearchWebItems](../models/searchwebitems.md)]                                          | :heavy_check_mark:                                                                                  | Results in the provider's order, after any required PII redaction. Empty when no results are found. |
| `metadata`                                                                                          | [models.SearchWebMetadata](../models/searchwebmetadata.md)                                          | :heavy_check_mark:                                                                                  | Details about this search request.                                                                  |