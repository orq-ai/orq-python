<p align="left">
  <a href="https://orq.ai" target="_blank">
    <img src="https://asset.brandfetch.io/idtBhDRr2x/idcrPsCm4K.png" alt="Orq">
  </a>
</p>

Build AI Applications from Playground to Production

![npm](https://img.shields.io/pypi/v/orq-ai-sdk)

# orq.ai Python SDK

The orq.ai Python library enables easy orq.ai REST API integration in Python 3.7+ apps, offering typed request/response elements and httpx-based sync/async clients

# Documentation

The REST API documentation can be found on [docs.orq.ai](https://docs.orq.ai/reference/authentication).

## Installation

```bash
# install from PyPI
pip install orq-ai-sdk
```

## Usage

_You can get your workspace API key from the settings section in your orq.ai workspace. `https://my.orq.ai/<workspace>/settings/developers`_

```python
import os

from orq_ai_sdk import OrqAI

client = OrqAI(
   api_key=os.environ.get("ORQ_API_KEY", "__API_KEY__"),
   environment="production"
)

generation = client.deployments.invoke(
    key="customer_service",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)
```

## Async usage

Simply import AsyncOrqAI instead of OrqAI and use await with each API call:

```python
import os
import asyncio
from orq_ai_sdk import AsyncOrqAI

client = AsyncOrqAI(
    api_key=os.environ.get("ORQ_API_KEY", "__API_KEY__"),
    environment="production"
)


async def main() -> None:
    generation = await client.deployments.invoke(
        key="customer_service",
        context={"environments": "production", "country": "NLD"},
        inputs={"firstname": "John", "city": "New York"},
        metadata={"customer_id": "Qwtqwty90281"},
    )

    print(generation.choices[0].message.content)

asyncio.run(main())
```

## Deployments

<div id="deployments"/>

The Deployments API delivers text outputs, images or tool calls based on the configuration established within Orq
for your deployments. Additionally, this API supports streaming. To ensure ease of use and minimize errors, using the
code snippets from the Orq Admin panel is highly recommended.

### Invoke a deployment

#### `invoke()`

```python
deployment = await client.deployments.invoke(
    key="customer_service",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

print(deployment.choices[0].message.content)
```

#### `invoke_with_stream()`

```python
stream = client.deployments.invoke_with_stream(
    key="customer_service",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

await  for chunk in stream:

    if chunk.is_final:
        print("Stream is finished")

    print(chunk.choices[0].message.content or "", end="")
```

#### Adding messages as part of your request

If you are using the `invoke` method, you can include `messages` in your request to the model. The `messages` property
allows you to combine `chat_history` with the prompt configuration in Orq, or to directly send `messages` to the
model if you are managing the prompt in your code.

```python
generation = client.deployments.invoke(
    key="customer_service",
    context={
        "language": [],
        "environments": []
    },
    metadata={
        "custom-field-name": "custom-metadata-value"
    },
    inputs={"firstname": "John", "city": "New York"},
    messages=[{
        "role": "user",
        "content": "A customer is asking about the latest software update features. Generate a detailed and informative response highlighting the key new features and improvements in the latest update.",
    }]
)
```

#### Logging metrics to the deployment configuration

After invoking, streaming or getting the configuration of a deployment, you can use the `add_metrics` method to add
information to the deployment.

```python

await generation.add_metrics(
    chain_id="c4a75b53-62fa-401b-8e97-493f3d299316",
    conversation_id="ee7b0c8c-eeb2-43cf-83e9-a4a49f8f13ea",
    user_id="e3a202a6-461b-447c-abe2-018ba4d04cd0",
    feedback={"score": 100},
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
    },
    messages=[{
        "role": "user",
        "content": "A customer is asking about the latest software update features. Generate a detailed and informative response highlighting the key new features and improvements in the latest update.",
    }]
)
```

### Get deployment configuration

#### `get_config()`

```python
prompt_config = client.deployments.get_config(
    key="customer_service",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

print(prompt_config.to_dict())
```

#### Logging metrics to the deployment configuration

After invoking, streaming or getting the configuration of a deployment, you can use the `add_metrics` method to add
information to the deployment.

```python

prompt_config.add_metrics(
    chain_id="c4a75b53-62fa-401b-8e97-493f3d299316",
    conversation_id="ee7b0c8c-eeb2-43cf-83e9-a4a49f8f13ea",
    user_id="e3a202a6-461b-447c-abe2-018ba4d04cd0",
    feedback={"score": 100},
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
    },
    usage={
        "prompt_tokens": 100,
        "completion_tokens": 900,
        "total_tokens": 1000,
    },
    performance={
        "latency": 9000,
        "time_to_first_token": 250,
    },
)
```

### Logging LLM responses

<div id="logging"/>

Whether you use the `get_config` or `invoke`, you can log the model generations to the deployment. Here are some
examples of how to do it.

#### Logging the completion choices the model generated for the input prompt

```python
generation.add_metrics(
    choices=[
        {
            "index": 0,
            "finish_reason": "assistant",
            "message": {
                "role": "assistant",
                "content": "Dear customer: Thank you for your interest in our latest software update! We're excited to share with you the new features and improvements we've rolled out. Here's what you can look forward to in this update",
            },
        },
    ]
)
```

#### Logging the completion choices the model generated for the input prompt

You can save the images generated by the model in Orq. If the image format is `base64` we always store it as
a `png`.

```python
generation.add_metrics(
    choices=[
        {
            "index": 0,
            "finish_reason": 'stop',
            "message": {
                "role": "assistant",
                "url": "<image_url>"
            },
        },
    ],
)
```

#### Logging the output of the tool calls

```python
generation.add_metrics(
  choices=[
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": None,
        "tool_calls": [
          {
            "type": "function",
            "id": "call_pDBPMMacPXOtoWhTWibW1D94",
            "function": {
              "name": "get_weather",
              "arguments": '{"location":"San Francisco, CA"}',
            },
          },
        ],
      },
      "finish_reason": 'tool_calls',
    }
  ]
)
```
