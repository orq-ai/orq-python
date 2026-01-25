# Router.Audio.Speech

## Overview

### Available Operations

* [create](#create) - Create speech

## create

Generates audio from the input text.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSpeech" method="post" path="/v2/router/audio/speech" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.router.audio.speech.create(input_="<value>", model="Grand Caravan", voice="<value>", response_format="mp3", speed=1, retry={
        "on_codes": [
            429,
            500,
            502,
            503,
            504,
        ],
    }, load_balancer={
        "type": "weight_based",
        "models": [
            {
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
        ],
    }, timeout={
        "call_timeout": 30000,
    }, orq={
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
        "thread": {
            "id": "thread_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "tags": [
                "customer-support",
                "priority-high",
            ],
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

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input`                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                          | The text to generate audio for. The maximum length is 4096 characters                                                                                                                                                                                                                                                                       |
| `model`                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                          | ID of the model to use                                                                                                                                                                                                                                                                                                                      |
| `voice`                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                          | The voice to use. <br/><br/> Available voices for OpenAI <br/><br/> `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer` <br/><br/> Available voices for ElevenLabs <br/><br/> `aria`, `roger`, `sarah`, `laura`, `charlie`, `george`, `callum`, `river`, `liam`, `charlotte`, `alice`, `matilda`, `will`, `jessica`, `eric`, `chris`, `brian`, `daniel`, `lily`, `bill` |
| `response_format`                                                                                                                                                                                                                                                                                                                           | [Optional[models.CreateSpeechResponseFormat]](../../models/createspeechresponseformat.md)                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`. If a format is provided but not supported by the provider, the response will be in the default format. When the provided format is not supported by the provider, the response will be in the default format.                                 |
| `speed`                                                                                                                                                                                                                                                                                                                                     | *Optional[float]*                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | The speed of the generated audio.                                                                                                                                                                                                                                                                                                           |
| `name`                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | The name to display on the trace. If not specified, the default system name will be used.                                                                                                                                                                                                                                                   |
| `fallbacks`                                                                                                                                                                                                                                                                                                                                 | List[[models.CreateSpeechFallbacks](../../models/createspeechfallbacks.md)]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | Array of fallback models to use if primary model fails                                                                                                                                                                                                                                                                                      |
| `retry`                                                                                                                                                                                                                                                                                                                                     | [Optional[models.CreateSpeechRetry]](../../models/createspeechretry.md)                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | Retry configuration for the request                                                                                                                                                                                                                                                                                                         |
| `load_balancer`                                                                                                                                                                                                                                                                                                                             | [Optional[models.CreateSpeechLoadBalancer]](../../models/createspeechloadbalancer.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | Load balancer configuration for the request.                                                                                                                                                                                                                                                                                                |
| `timeout`                                                                                                                                                                                                                                                                                                                                   | [Optional[models.CreateSpeechTimeout]](../../models/createspeechtimeout.md)                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | Timeout configuration to apply to the request. If the request exceeds the timeout, it will be retried or fallback to the next model if configured.                                                                                                                                                                                          |
| `orq`                                                                                                                                                                                                                                                                                                                                       | [Optional[models.CreateSpeechOrq]](../../models/createspeechorq.md)                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                         |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |