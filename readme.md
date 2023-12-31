<p align="left">
  <a href="https://orquesta.cloud" target="_blank">
    <img src="https://raw.githubusercontent.com/orquestadev/orquesta-node/main/img/banner.png" alt="Orquesta">
  </a>
</p>

Integrate and operate your products with the power of Large Language Models from a single collaboration platform. Conduct prompt engineering, experimentation, operations and monitoring across models, with full transparency on quality and costs.

![npm](https://img.shields.io/pypi/v/orquesta-sdk)

# Orquesta Python SDK

## Contents

- [Installation](#installation)
- [Create a client instance](#createclient)
- [Usage](#usage)
- [Reference](#reference)

## Installation

<div id="installation"/>

```bash
pip install orquesta-sdk
```

## Creating a client instance

<div id="createclient"/>

_You can get your workspace API key from the settings section in your Orquesta workspace. `https://my.orquesta.dev/<workspace>/settings/developers`_

Initialize the Orquesta client with your API key:

```python
import os

from orquesta_sdk import Orquesta, OrquestaClientOptions

api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")

options = OrquestaClientOptions(
    api_key=api_key,
    environment="production"
)

client = Orquesta(options)
```

To configure connection settings when creating a client instance, use the `OrquestaClientOptions` class, which allows for the adjustment of the following parameters:

`OrquestaClientOptions`

- `api_key`: str - workspace API key to use for authentication.
- `environment`: Optional[str] - it is recommended, though not required, to specify the environment for the client. This ensures it is automatically added to the evaluation context.

## Deployments

The Deployments API delivers text outputs, images or tool calls based on the configuration established within Orquesta for your deployments. Additionally, this API supports streaming. To ensure ease of use and minimize errors, using the code snippets from the Orquesta Admin panel is highly recommended.

### Invoke a deployment

#### `invoke()`

```python
deployment = client.deployments.invoke(
     key="customer_service",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

print(deployment.choices[0].message.content)
```

#### `invoke_with_stream()`

```python
deployment = client.deployments.invoke_with_stream(
    key="customer_service",
    context={ "environments": "production", "country": "NLD" },
    inputs={ "firstname": "John", "city": "New York" },
    metadata={ "customer_id": "Qwtqwty90281" },
)

for chunk in deployment:
    if chunk.is_final:
        print("Stream is finished")
```

#### Logging metrics to the deployment configuration

After invoking, streaming or getting the configuration of a deployment, you can use the `add_metrics` method to add information to the deployment.

```python

deployment.add_metrics(
    chain_id="c4a75b53-62fa-401b-8e97-493f3d299316",
    conversation_id="ee7b0c8c-eeb2-43cf-83e9-a4a49f8f13ea",
    user_id="e3a202a6-461b-447c-abe2-018ba4d04cd0",
    feedback={"score": 100},
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
    }
)
```

### Get deployment configuration

#### `get_config()`

```python
config = client.deployments.get_config(
    key="customer_service",
    context={ "environments": "production", "country": "NLD" },
    inputs={ "firstname": "John", "city": "New York" },
    metadata={ "customer_id": "Qwtqwty90281" },
)

print(config.to_dict())
```

#### Logging metrics to the deployment configuration

After invoking, streaming or getting the configuration of a deployment, you can use the `add_metrics` method to add information to the deployment.

```python

deployment.add_metrics(
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

# Orquesta API

## Deployments API

Class:

- <code><a href="https://github.com/orquestadev/orquesta-python/blob/orquesta_sdk/api_resources/deployments.ts#L277">Deployments</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/orquesta_sdk/api_resources/deployments.ts#L165">Deployment</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/orquesta_sdk/api_resources/deployments.ts#L209">DeploymentConfig</a></code>

Methods:

- <code>client.deployments.<a href="https://github.com/orquestadev/orquesta-python/blob/main/orquesta_sdk/api_resources/deployments.ts#L306">get_config</a>({ ...params }) -> `DeploymentConfig`</code>
- <code>client.deployments.<a href="https://github.com/orquestadev/orquesta-python/blob/orquesta_sdk/api_resources/deployments.ts#L325">invoke</a>({ ...params }) -> `Deployment` </code>
- <code>client.deployments.<a href="https://github.com/orquestadev/orquesta-python/blob/orquesta_sdk/api_resources/deployments.ts#L359">invoke_with_stream</a>({ ...params }) -> `Generator[Deployment, Any, None]` </code>
