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

_You can get your workspace API key from the settings section in your Orquesta workspace. `https://my.orquesta.dev/<workspace>/settings/developers`_

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

## Usage - Prompts

<div id="usage"/>

Use the Prompts API to query your prompts from Orquesta.

Orquesta supports completion and chat prompts. The prompt value type is `OrquestaPrompt`. We recommend using the code snippets provided in the Orquesta Admin panel to reduce the risk of errors and improve ease of use.

We also provide helper functions that map the returned value from Orquesta to the specific provider.

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

#### Helper functions per LLM provider

We provide `helper` functions and `interfaces` that map the returned value from Orquesta to the specific provider, so it's easy for you to forward the Prompt to your different LLM providers.

| Provider     | Helper                                | Class                             |
| ------------ | ------------------------------------- | ------------------------------------- |
| Anthropic    | `orquesta_anthropic_parameters_mapper`   | `OrquestaAnthropicPromptParameters`   |
| Cohere       | `orquesta_cohere_parameters_mapper`      | `OrquestaCoherePromptParameters`      |
| Google       | `orquesta_google_parameters_mapper`      | `OrquestaGooglePromptParameters`      |
| Hugging Face | `orquesta_huggingface_parameters_mapper` | `OrquestaHuggingFacePromptParameters` |
| OpenAI       | `orquesta_openai_parameters_mapper`      | `OrquestaOpenAIPromptParameters`      |
| Replicate    | `orquesta_replicate_parameters_mapper`   | `OrquestaReplicatePromptParameters`   |

### Logging responses and metadata for prompts

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

Orquesta has a powerful Remote Configurations API that allows you to configure and run all your environments and services remotely dynamically. Orquesta supports different types of remote configurations, and we recommend always typing the `query` method to help Typescript infer the correct type.

Supported types: `bool`, `float`, `str`, `dict`, `list`

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
    context={"environments": "production", "market": "US" },
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

#### Example: Querying a configuration of type JSON

```python
config = client.remote_configs.query(
    key="json_config",
    default_value=dict,
    contenxt={"environments": "develop", "platform": "mobile"},
)
```

### Additional metadata logging

After every query, Orquesta will generate a log with data about the request. You can add metadata to the log using the `add_metrics` method anytime.

`metadata` is a set of `key-value pairs` that you can use to add custom information to the log.

#### Example: Add metrics to your request log

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

<div id="reference"/>

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
| key       | `str`            | Key of prompt to retrieve                                                                                                                              | Yes      |
| context   | `Dict[str, Any]` | Set of key-value pairs from your data model that should be compared against the values in the configuration matrix                                 | No       |
| variables | `Dict[str, Any]` | Set of key-value pairs variables to replace in your prompts. The provided variables are combined with the default variables defined in the prompt. | No       |
| metadata  | `Dict[str, Any]` | Set of key-value pairs of metadata to attach to the generated log after the prompt is evaluated                         | No       |

#### `OrquestaPrompt`

| Property    | Type                                               | Description                                                                                                                                                            |
|-------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value       | `OrquestaCompletionPrompt` or `OrquestaChatPrompt` | The value of the prompt                                                                                                                                                |
| has_error   | `bool`                                             | A boolean indicating if the request resulted in an error                                                                                                                 |
| trace_id    | `str`                                              | Trace ID of the request log to use to report prompt metrics to the API if the method `add_metrics` is not used                                                         |
| add_metrics | `(metrics: OrquestaPromptMetrics) -> None`         |  method that reports metadata and information of the LLM interaction to the request log after the prompt value is returned. At least one of the properties is required |

#### `OrquestaPromptMetrics`

| Property     | Type             | Description                                                                                                    | Required |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------|----------|
| metadata     | `Dict[str, Any]` | Key-value pairs of custom fields to attach to the generated logs       | No       |
| score        | `int`            | Feedback provided by your end user. Number between 0 and 10                                                                          | No       |
| latency      | `int`            | Total time in milliseconds of the request to the LLM provider API                                                          | No       |
| llm_response | `str`            | Full response returned by your LLM provider | No       |
| economics    | `int`            | Prompt information about the prompt and completion tokens                                                      | No       |

#### `OrquestaPromptMetricsEconomics`

| Property          | Type  | Description                                  | Required |
|-------------------|-------|----------------------------------------------|----------|
| prompt_tokens     | `int` | Total tokens input into the model            | Yes      |
| completion_tokens | `int` | Total tokens output by the model             | Yes      |
| total_tokens      | `int` | Sum of `prompt_tokens` + `completion_tokens` | No       |

## Remote Configurations API

#### `OrquestaRemoteConfigQuery`

| Parameter     | Type             | Description                                                                                                                | Required |
|---------------|------------------|----------------------------------------------------------------------------------------------------------------------------|----------|
| key           | `str`            | Key of remote configuration to retrieve                                                                                    | Yes      |
| default_value | `Any`            | The value to be used in case there is an error during evaluation or the remote configuration does not exist         | Yes      |
| context       | `Dict[str, Any]` | Set of key-value pairs from your data model that should be compared against the values in the configuration matrix         | No       |
| metadata      | `Dict[str, Any]` | Set of key-value pairs of metadata to attach to the generated log after the prompt is evaluated | No       |

#### `OrquestaRemoteConfig`

| Parameter   | Type                                             | Description                                                                                                                            |
|-------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| value       | `Any`                                            | The value of the remote configuration                     |
| config_type | `bool` or `str` or `float` or `dict` or `list`   | Return type of the remote configuration                     |
| trace_id    | `str`                                            | Trace ID of the request log to use to report prompt metrics to the API if the method `add_metrics` is not used                                                                                                            |
| add_metrics | `(metrics: OrquestaRemoteConfigMetrics) -> None` | A method that reports metadata to the request log after the configuration value is returned. At least one of the properties is required |

#### `OrquestaRemoteConfigMetrics`

| Parameter | Type             | Description                                                                                                                | Required |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------------------|----------|
| metadata  | `Dict[str, Any]` | Set of key-value pairs of metadata you want to attach to the request log | No       |
