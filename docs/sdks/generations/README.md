# Router.Images.Generations

## Overview

### Available Operations

* [create](#create) - Create image

## create

Create an Image

### Example Usage

<!-- UsageSnippet language="python" operationID="createImage" method="post" path="/v2/router/images/generations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.images.generations.create(prompt="<value>", model="2", n=1, orq={
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

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt`                                                                                                                                                                                | *str*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                      | A text description of the desired image(s).                                                                                                                                             |
| `model`                                                                                                                                                                                 | *str*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                      | The model to use for image generation. One of `openai/dall-e-2`, `openai/dall-e-3`, or `openai/gpt-image-1`.                                                                            |
| `background`                                                                                                                                                                            | [OptionalNullable[models.Background]](../../models/background.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                      | Allows to set transparency for the background of the generated image(s). This parameter is only supported for `openai/gpt-image-1`.                                                     |
| `moderation`                                                                                                                                                                            | [OptionalNullable[models.Moderation]](../../models/moderation.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                      | Control the content-moderation level for images generated by `gpt-image-1`. Must be either `low` or `auto`.                                                                             |
| `n`                                                                                                                                                                                     | *OptionalNullable[int]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.                                                                                    |
| `output_compression`                                                                                                                                                                    | *OptionalNullable[int]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | The compression level (0-100%) for the generated images. This parameter is only supported for `gpt-image-1` with the `webp` or `jpeg` output formats.                                   |
| `output_format`                                                                                                                                                                         | [OptionalNullable[models.OutputFormat]](../../models/outputformat.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                      | The format in which the generated images are returned. This parameter is only supported for `openai/gpt-image-1`.                                                                       |
| `quality`                                                                                                                                                                               | [OptionalNullable[models.Quality]](../../models/quality.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | The quality of the image that will be generated. `auto` will automatically select the best quality for the given model.                                                                 |
| `response_format`                                                                                                                                                                       | [OptionalNullable[models.CreateImageResponseFormat]](../../models/createimageresponseformat.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | The format in which generated images are returned. Must be one of `url` or `b64_json`. This parameter isn't supported for `gpt-image-1` which will always return base64-encoded images. |
| `size`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | The size of the generated images. Must be one of the specified sizes for each model.                                                                                                    |
| `style`                                                                                                                                                                                 | [OptionalNullable[models.Style]](../../models/style.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | The style of the generated images. This parameter is only supported for `openai/dall-e-3`. Must be one of `vivid` or `natural`.                                                         |
| `orq`                                                                                                                                                                                   | [Optional[models.CreateImageOrq]](../../models/createimageorq.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                      | N/A                                                                                                                                                                                     |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |

### Response

**[models.CreateImageResponseBody](../../models/createimageresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |