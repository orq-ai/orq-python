<p align="left">
  <a href="https://orquesta.dev" target="_blank">
    <img src="https://raw.githubusercontent.com/orquestadev/orquesta-javascript/main/img/banner.png" alt="Orquesta"  height="84">
  </a>
</p>

_Orquesta provides your product teams with no-code collaboration tooling to experiment, operate and monitor LLMs and
remote configurations within your SaaS_

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

_You can get your workspace API key from the settings section in your Orquesta
workspace. `https://my.orquesta.dev/<workspace>/settings/developers`_

Initialize the Orquesta client with your API key:

```python
import os

from orquesta_sdk import OrquestaClient, OrquestaClientOptions

api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")

options = OrquestaClientOptions(
    api_key=api_key,
    ttl=3600
)

client = OrquestaClient(options)
```

When creating a client instance, the following connection settings can be adjusted using the `OrquestaClientOptions`
class:

`OrquestaClientOptions`

- `api_key`: str - your workspace API key to use for authentication.
- `ttl?`: int - the time to live in seconds for the local cache. Default is 3600 seconds (1 hour).

## Usage

<div id="usage"/>

Use the Prompts API to query your prompts from Orquesta.

Orquesta supports completion and chat prompts. The prompt value type is `OrquestaPrompt`. We recommend to use the code
snippets provided in the Orquesta Admin panel to reduce risk of errors and improve ease of use.

We also provide helper functions that map the returned value from Orquesta to the specific provider. The mapper can be
found inside `helpers`.

#### Example: Querying a completion prompt

```python

from orquesta_sdk.helpers import orquesta_openai_parameters_mapper

prompt = client.prompts.query(
    key="completion_prompt_key",
    context={"environments": "production", "workspaceId": "soql1odAABC2"},
    variables={"firstname": "John", "city": "New York"},
    metadata={"chain_id": "ad1231xsdaABw"},
)

openai_api_parameters = orquesta_openai_parameters_mapper(prompt.value)
```

#### Example: Querying a chat prompt

```python
from orquesta_sdk.helpers import orquesta_openai_parameters_mapper

prompt = client.prompts.query(
    key="chat_prompt_key",
    context={"environments": "production", "workspaceId": "soql1odAABC2"},
    variables={"firstname": "John", "city": "New York"},
    metadata={"chain_id": "ad1231xsdaABw"},
)

openai_api_parameters = orquesta_openai_parameters_mapper(prompt.value)
```

#### Example: Add metrics to your request log

After every query, Orquesta will generate a log with the result of the evaluation. You can add metadata and information
about the interaction with the LLM to the log by using the `add_metrics` method.

The properties `score`, `latency`, `llm_response` and `economics` are reserved for Orquesta use. `metadata` is a set
of `key-value pairs` that you can use to add custom information to the log.

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

## Remote Configurations

Orquesta also comes with a powerful Remote Configurations API that allows you to dynamically configure and run all your
environments and services remotely.

Orquesta supports different types of remote configurations, we recommend to always type the `query` method to help
Typescript infer the correct type.

_Supported types: `bool`, `float`, `str`, `dict`, `list`_

#### Example: Querying a configuration of type boolean

```python
config = client.remote_configs.query(
    key="boolean_config",
    default_value=False,
    context={"environments": "production", "role": "admin"},
    metadata={"user_id": 450}
)
```

#### Example: Querying a configuration of type str

```python


config = client.remote_configs.query(
    key="str_config",
    default_value="str_value",
    context={"environments": "production", "country": "NL"},
    metadata={"timestamp": 1623345600}
)
```

#### Example: Querying a configuration of type int

```python
config = client.remote_configs.query(
    key="int_config",
    default_value=1990,
    context={"environments": "production", "market": "US", },
    metadata={"domain": "ecommerce"}
)
```

#### Example: Querying a configuration of type array

```python
config = client.remote_configs.query(
    key="list_config",
    default_value=["USA", "NL"],
    context={"environments": "acceptance", "is_enable": True},
    metadata={"domain": "ecommerce"}
)
```

#### Example: Querying a configuration of type json

```python
config = client.remote_configs.query(
    key="json_config",
    default_value=dict,
    contenxt={"environments": "develop", "platform": "mobile"},
)
```

#### Example: Add metrics to your request log

After every query, Orquesta will generate a log with data about the request. You can add metadata to the log by using
the `add_metrics` method.

`metadata` is a set of `key-value pairs` that you can use to add custom information to the log.

```python
from orquesta_sdk.remote_configs import OrquestaRemoteConfigMetrics

metrics = OrquestaRemoteConfigMetrics(
    metadata={
        "custom": "custom_metadata",
        "user_clicks": 20,
        "selected_option": "option1"
    }
)

config.add_metrics(metrics)
```

<div id="references"/>

## Options API

#### `OrquestaPromptQuery`

| Parameter | Type  | Description                                                                       | Required |
|-----------|-------|-----------------------------------------------------------------------------------|----------|
| api_key   | `str` | your workspace API key to use for authentication                                  | Yes      |
| ttl       | `int` | the time to live in seconds for the local cache. Default is 3600 seconds (1 hour) | No       |

## Prompts API

#### `OrquestaPromptQuery`

| Parameter | Type             | Description                                                                                                                                        | Required |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| key       | `str`            | The key of the prompt                                                                                                                              | Yes      |
| context   | `Dict[str, Any]` | Set of key-value pairs from your data model that should be compared against the values in the configuration matrix                                 | No       |
| variables | `Dict[str, Any]` | Set of key-value pairs variables to replace in your prompts. The provided variables are combined with the default variables defined in the prompt. | No       |
| metadata  | `Dict[str, Any]` | Set of key-value pairs of metadata you want to attach to the generated log after the prompt is evaluated. This is optional                         | No       |

#### `OrquestaPrompt`

| Property    | Type                                               | Description                                                                                                                                                            |
|-------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value       | `OrquestaCompletionPrompt` or `OrquestaChatPrompt` | The value of the prompt                                                                                                                                                |
| has_error   | `bool`                                             | A boolean indicating if the request resulted in error                                                                                                                  |
| trace_id    | `str`                                              | Trace ID of the request log to use to report prompt metrics to the API if the method `add_metrics` is not used                                                         |
| add_metrics | `(metrics: OrquestaPromptMetrics) -> None`         | A method that report metadata and information of the LLM interaction to the request log after the prompt value is returned. At least one of the properties is required |

#### `OrquestaPromptMetrics`

| Property     | Type             | Description                                                                                                    | Required |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------|----------|
| score        | `int`            | The value of the prompt                                                                                        | No       |
| economics    | `int`            | Prompt information about the prompt and completion tokens                                                      | No       |
| latency      | `int`            | A boolean indicating if the request resulted in error                                                          | No       |
| llm_response | `str`            | Trace ID of the request log to use to report prompt metrics to the API if the method `add_metrics` is not used | No       |
| metadata     | `Dict[str, Any]` | Set of key-value pairs of metadata you want to attach to the generated log after the prompt is evaluated       | No       |

#### `OrquestaPromptMetricsEconomics`

| Property          | Type  | Description                                  | Required |
|-------------------|-------|----------------------------------------------|----------|
| prompt_tokens     | `int` | Total tokens input into the model            | No       |
| completion_tokens | `int` | Total tokens output by the model             | Yes      |
| total_tokens      | `int` | Sum of `prompt_tokens` + `completion_tokens` | No       |

## Remote Configurations API

#### `OrquestaRemoteConfigQuery`

| Parameter     | Type             | Description                                                                                                                | Required |
|---------------|------------------|----------------------------------------------------------------------------------------------------------------------------|----------|
| key           | `str`            | Key of remote configuration                                                                                                | Yes      |
| default_value | `Any`            | The value to be returned in case there is a en error during evaluation or the remote configuration does not exists         | Yes      |
| context       | `Dict[str, Any]` | Set of key-value pairs from your data model that should be compared against the values in the configuration matrix         | No       |
| metadata      | `Dict[str, Any]` | Set of key-value pairs of metadata you want to attach to the generated log after the prompt is evaluated. This is optional | No       |

#### `OrquestaRemoteConfig`

| Parameter   | Type                                             | Description                                                                                                                            |
|-------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| value       | `Any`                                            | Set of key-value pairs from your data model that should be compared against the values in the configuration matrix                     |
| config_type | `bool` or `str` or `float` or `dict` or `list`   | The value to be returned in case there is a en error during evaluation or the remote configuration does not exists                     |
| trace_id    | `str`                                            | Key of remote configuration                                                                                                            |
| add_metrics | `(metrics: OrquestaRemoteConfigMetrics) -> None` | A method that report metadata to the request log after the configuration value is returned. At least one of the properties is required |

#### `OrquestaRemoteConfigMetrics`

| Parameter | Type             | Description                                                                                                                | Required |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------------------|----------|
| metadata  | `Dict[str, Any]` | Set of key-value pairs of metadata you want to attach to the generated log after the prompt is evaluated. This is optional | No       |
