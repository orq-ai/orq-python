# Router.Images.Edits

## Overview

### Available Operations

* [create](#create) - Create image edit

## create

Edit an Image

### Example Usage

<!-- UsageSnippet language="python" operationID="createImageEdit" method="post" path="/v2/router/images/edits" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.images.edits.create(model="LeBaron", prompt="<value>", n=1, orq={
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
        "cache": {
            "ttl": 3600,
            "type": "exact_match",
        },
        "load_balancer": {
            "type": "weight_based",
            "models": [
                {
                    "model": "openai/gpt-4o",
                    "weight": 0.7,
                },
                {
                    "model": "anthropic/claude-3-5-sonnet",
                    "weight": 0.3,
                },
            ],
        },
        "timeout": {
            "call_timeout": 30000,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                                                                                     | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The model to use for image edit. [Check models](https://docs.orq.ai/docs/ai-gateway-supported-models#image-models)                                                          |
| `prompt`                                                                                                                                                                    | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | A text description of the desired image(s).                                                                                                                                 |
| `image`                                                                                                                                                                     | *Optional[Any]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The image(s) to edit. Must be a supported image file or an array of images.  Each image should be a png, webp, or jpg file less than 50MB. You can provide up to 16 images. |
| `n`                                                                                                                                                                         | *OptionalNullable[int]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The number of images to generate. Must be between 1 and 10.                                                                                                                 |
| `size`                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The size of the generated images                                                                                                                                            |
| `quality`                                                                                                                                                                   | [OptionalNullable[models.CreateImageEditQuality]](../../models/createimageeditquality.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                          | The quality of the image that will be generated. Auto will automatically select the best quality for the given model.                                                       |
| `response_format`                                                                                                                                                           | [Optional[models.CreateImageEditResponseFormat]](../../models/createimageeditresponseformat.md)                                                                             | :heavy_minus_sign:                                                                                                                                                          | The format in which the generated images are returned. Some of the models only return the image in base64 format.                                                           |
| `user`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | A unique identifier representing your end-user, which can help to monitor and detect abuse.                                                                                 |
| `orq`                                                                                                                                                                       | [Optional[models.CreateImageEditOrq]](../../models/createimageeditorq.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |

### Response

**[models.CreateImageEditResponseBody](../../models/createimageeditresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |