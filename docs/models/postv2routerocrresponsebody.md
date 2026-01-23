# PostV2RouterOcrResponseBody

Represents an OCR response from the API.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `model`                                                          | *str*                                                            | :heavy_check_mark:                                               | ID of the model used for OCR.                                    |
| `pages`                                                          | List[[models.Pages](../models/pages.md)]                         | :heavy_check_mark:                                               | N/A                                                              |
| `usage`                                                          | [models.PostV2RouterOcrUsage](../models/postv2routerocrusage.md) | :heavy_check_mark:                                               | N/A                                                              |