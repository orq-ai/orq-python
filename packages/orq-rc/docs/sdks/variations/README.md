# Router.Images.Variations

## Overview

### Available Operations

* [create](#create) - Create image variation

## create

Create an Image Variation

### Example Usage

<!-- UsageSnippet language="python" operationID="createImageVariation" method="post" path="/v2/gateway/images/variations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.images.variations.create(model="Altima", n=1, response_format="url", size="1024x1024", orq={
        "retry": {
            "on_codes": [
                429,
                500,
                502,
                503,
                504,
            ],
        },
        "fallbacks": [
            {
                "model": "openai/gpt-4o-mini",
            },
        ],
        "prompt": {
            "id": "prompt_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "version": "latest",
        },
        "identity": {
            "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "display_name": "Jane Doe",
            "email": "jane.doe@example.com",
            "metadata": [
                {
                    "department": "Engineering",
                    "role": "Senior Developer",
                },
            ],
            "logo_url": "https://example.com/avatars/jane-doe.jpg",
            "tags": [
                "hr",
                "engineering",
            ],
        },
        "contact": {
            "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "display_name": "Jane Doe",
            "email": "jane.doe@example.com",
            "metadata": [
                {
                    "department": "Engineering",
                    "role": "Senior Developer",
                },
            ],
            "logo_url": "https://example.com/avatars/jane-doe.jpg",
            "tags": [
                "hr",
                "engineering",
            ],
        },
        "cache": {
            "ttl": 3600,
            "type": "exact_match",
        },
        "load_balancer": [
            {
                "type": "weight_based",
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
            {
                "type": "weight_based",
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
        ],
        "timeout": {
            "call_timeout": 30000,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                                                                           | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | The model to use for image generation.                                                                                                                            |
| `image`                                                                                                                                                           | *Optional[Any]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | The image to edit. Must be a supported image file. It should be a png, webp, or jpg file less than 50MB.                                                          |
| `n`                                                                                                                                                               | *OptionalNullable[int]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                | The number of images to generate. Must be between 1 and 10.                                                                                                       |
| `response_format`                                                                                                                                                 | [Optional[models.CreateImageVariationResponseFormat]](../../models/createimagevariationresponseformat.md)                                                         | :heavy_minus_sign:                                                                                                                                                | The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated. |
| `size`                                                                                                                                                            | [Optional[models.Size]](../../models/size.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                | The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.                                                                            |
| `user`                                                                                                                                                            | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | A unique identifier representing your end-user, which can help to monitor and detect abuse.                                                                       |
| `orq`                                                                                                                                                             | [Optional[models.CreateImageVariationOrq]](../../models/createimagevariationorq.md)                                                                               | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |

### Response

**[models.CreateImageVariationResponseBody](../../models/createimagevariationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |