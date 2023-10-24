<p align="left">
  <a href="https://orquesta.cloud" target="_blank">
    <img src="https://raw.githubusercontent.com/orquestadev/orquesta-javascript/main/img/banner.png" alt="Orquesta"  height="84">
  </a>
</p>

_LLM Operations and Integration Platform_

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

from orquesta_sdk import OrquestaClient, OrquestaClientOptions

api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")

options = OrquestaClientOptions(
    api_key=api_key,
    ttl=3600,
    environment="production"
)

client = OrquestaClient(options)
```

When creating a client instance, the following connection settings can be adjusted using the `OrquestaClientOptions` class:

`OrquestaClientOptions`

- `api_key`: str - your workspace API key to use for authentication.
- `environment`: Optional[str] - the environment to use for the client. Not required but recommended to use so it"s added to the evaluation context automatically.
- `ttl`: Optional[int] - the time to live in seconds for the local cache. Default is 3600 seconds (1 hour).

## Usage - Endpoints

Use the Endpoints API to query or stream your endpoints from Orquesta.

Using endpoints to generate a LLM response based on your use case with Orquesta provides a low-latency, secure connection to the Endpoints API online prediction service. Getting out of the box metrics and logging for your LLMs.

Endpoints API support streaming and querying. We recommend to use the code snippets provided in the Orquesta Admin panel to reduce risk of errors and improve ease of use.

#### Example: Querying an endpoint

```python
from orquesta_sdk.endpoints import OrquestaEndpointRequest

request = OrquestaEndpointRequest(
    key="customer_service",
    context={"environments": "production", "country": "NLD"},
    variables={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

endpoint_ref = client.endpoints.query(
    request
)

print(endpoint_ref.content)
```

#### Example: Streaming your endpoints

```python
request = OrquestaEndpointRequest(
    key="customer_service",
    context={ "environments": "production", "country": "NLD" },
    variables={ "firstname": "John", "city": "New York" },
    metadata={ "customer_id": "Qwtqwty90281" },
)

stream_generator = client.endpoints.stream(request)

for chunk in stream_generator:
    print("Received data:", chunk.content)

    if chunk.is_final:
        print("Stream is finished")
        endpoint_ref = chunk
```

### Logging score and metadata for endpoints

After every query, Orquesta will generate a log with the result of the evaluation. You can add `metadata` and `score` to the endpoint by using the `addMetrics` method.

If you need to cancel a stream, you can call `stream.unsubscribe()` method.

```python

metrics = OrquestaEndpointMetrics(
    score=85,
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
    },
)

endpoint_ref.addMetrics(metrics);
```

## Usage - Prompts

<div id="usage"/>

Use the Prompts API to query your prompts from Orquesta.

You can use Orquesta in prompt management mode by consuming our Prompts API. The prompt value type is `OrquestaPrompt`. We recommend to use the code snippets provided in the Orquesta Admin panel to reduce risk of errors and improve ease of use.

We support an unified data model structure for all our prompts and provide helper functions that map the returned value from Orquesta to the specific provider.

The `query` method receives an object of type `OrquestaPromptRequest` as parameter.

#### Example: Querying a prompt

```python

from orquesta_sdk.prompts import OrquestaPromptRequest

request = OrquestaPromptRequest(
    key="prompt_key",
    context={"environments": "production", "workspaceId": "soql1odAABC2"},
    variables={"firstname": "John", "city": "New York"},
    metadata={"chain_id": "ad1231xsdaABw"},
)

prompt = client.prompts.query(
    request=request,
)
```

#### Helper functions per LLM provider

We provide `helper` functions that map the returned value from Orquesta to a `dict` following the definitions of the specific provider, so it"s easy for you to forward the Prompt to your different LLM providers.

| Provider     | Helper                                 |
| ------------ | -------------------------------------- |
| Anthropic    | `orquesta_anthropic_parameters_mapper` |
| Cohere       | `orquesta_cohere_parameters_mapper`    |
| Google       | `orquesta_google_parameters_mapper`    |
| OpenAI       | `orquesta_openai_parameters_mapper`    |
| Hugging Face | `⚠️ Work in progress`                  |
| Replicate    | `⚠️ Work in progress`                  |

### Logging metrics and metadata for prompts

After every query, Orquesta will generate a log with the result of the evaluation. You can add metadata and information about the interaction with the LLM to the log by using the `add_metrics` method.

The properties `score`, `latency`, `llm_response` and `economics` are reserved and used to generate your real-time dashboards. `metadata` is a set of key-value pairs that you can use to add custom information to the log.

#### Example: Add metrics to your request log

```python

from orquesta_sdk.prompts import OrquestaPromptMetricsEconomics, OrquestaPromptMetrics

economics = OrquestaPromptMetricsEconomics(
    prompt_tokens=1200,
    completion_tokens=750,
    total_tokens=1950,
)

metrics = OrquestaPromptMetrics(
    score=100,
    latency=40,
    llm_response="Orquesta is awesome!",
    economics=economics,
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
        "total_interactions": 200,
    }
)

prompt.add_metrics(metrics)
```

## Usage - Remote Configurations

Orquesta also comes with a powerful Remote Configurations API that allows you to dynamically configure and run all your
environments and services remotely.

Orquesta has a powerful Remote Configurations API that allows you to configure and run all your environments and services remotely dynamically. Orquesta supports different Class of remote configurations, and we recommend always typing the `query` method to help Classcript infer the correct type.

Supported Class: `bool`, `float`, `str`, `dict`, `list`

#### Example: Querying a configuration of type boolean

```python
config = client.remoteconfigs.query(
    key="boolean_config",
    default_value=False,
    context={"environments": "production", "role": "admin"},
    metadata={"user_id": 450}
)
```

#### Example: Querying a configuration of type str

```python

request = OrquestaRemoteConfigRequest(
    key="str_config",
    default_value="str_value",
    context={"environments": "production", "country": "NL"},
    metadata={"timestamp": 1623345600}
)

config = client.remoteconfigs.query(
    request=request
)
```

#### Example: Querying a configuration of type int

```python
request = OrquestaRemoteConfigRequest(
    key="int_config",
    default_value=1990,
    context={"environments": "production", "market": "US" },
    metadata={"domain": "ecommerce"}
)

config = client.remoteconfigs.query(
    request=request
)

```

#### Example: Querying a configuration of type array

```python
request = OrquestaRemoteConfigRequest(
    key="list_config",
    default_value=["USA", "NL"],
    context={"environments": "acceptance", "is_enable": True},
    metadata={"domain": "ecommerce"}
)

config = client.remoteconfigs.query(
    request=request
)
```

#### Example: Querying a configuration of type JSON

```python
request = OrquestaRemoteConfigRequest(
    key="json_config",
    default_value=dict,
    contenxt={"environments": "develop", "platform": "mobile"},
)

config = client.remoteconfigs.query(
    request=request
)
```

### Additional metadata logging

After every query, Orquesta will generate a log with data about the request. You can add metadata to the log using the `add_metrics` method anytime.

`metadata` is a set of `key-value pairs` that you can use to add custom information to the log.

#### Example: Add metrics to your request log

```python
from orquesta_sdk.remoteconfigs import OrquestaRemoteConfigMetrics

metrics = OrquestaRemoteConfigMetrics(
    metadata={
        "custom": "custom_metadata",
        "user_clicks": 20,
        "selected_option": "option1"
    }
)

config.add_metrics(metrics)
```

<div id="reference"/>

# Orquesta API

## Endpoints API

Class:

- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/endpoints.ts#L59">OrquestaEndpoint</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/endpoints.ts#L39">OrquestaEndpointMetrics</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/endpoints.ts#L11">OrquestaEndpointRequest</a></code>

Methods:

- <code>client.endpoints.<a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/endpoints.ts#L84">query</a>({ ...params }) -> OrquestaEndpoint</code>
- <code>client.endpoints.<a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/endpoints.ts#L103">stream</a>({ ...params }) -> Observable`[OrquestaEndpoint]` </code>

## Prompts API

Class:

- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/prompts.ts#L127">OrquestaPrompt</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/prompts.ts#L95">OrquestaPromptMetrics</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/prompts.ts#L71">OrquestaPromptMetricsEconomics</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/prompts.ts#L9">OrquestaPromptRequest</a></code>

Methods:

- <code>client.prompts.<a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/prompts.ts#L155">query</a>({ ...params }) -> OrquestaPrompt</code>

## RemoteConfigs API

Class:

- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/remoteconfigs.ts#L9">OrquestaRemoteConfigKind</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/remoteconfigs.ts#L90">OrquestaRemoteConfig</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/remoteconfigs.ts#L77">OrquestaRemoteConfigMetrics</a></code>
- <code><a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/remoteconfigs.ts#L17">OrquestaRemoteConfigRequest</a></code>

Methods:

- <code>client.remoteconfigs.<a href="https://github.com/orquestadev/orquesta-python/blob/main/packages/js/src/lib/remoteconfigs.ts#L121">query<T></a>({ ...params }) -> OrquestaRemoteConfig</code>
