<p align="left">
  <a href="https://orquesta.dev" target="_blank">
    <img src="https://media.licdn.com/dms/image/C4E0BAQEXwCA4xN_AtQ/company-logo_200_200/0/1677578302965?e=2147483647&v=beta&t=df-lwhojzn0ZspaLGbRhZmTsZQimiLoVy9Uh7iYO-5U" alt="Orquesta"  height="84">
  </a>
</p>

_Orquesta's platform provides product teams with no-code building blocks for business rules, remote configurations and AI prompts_

# Orquesta Python SDK

## Table of contents

1. [Installation](#installation)
2. [Usage](#usage)
   1. [Prompts](#prompts)
   2. [Rules](#rules)
3. [Reference][#reference]

# Installation

## Prerequisites

- Python version 2.7 and 3.5+
- A free Orquesta account from [orquesta.cloud](https://orquesta.cloud).

### Installation

<div id='installation'/>

```bash
pip install orquesta-sdk
```

## Usage

<div id="usage"/>

_You can get your workspace API key from the settings section in your Orquesta workspace._

Initialize the Orquesta client with your API key:

The Orquesta SDK can be initialized in two ways. If you have the environment variable `ORQUESTA_API_KEY` is set, the SDK will use that key. Otherwise, you can pass the key as an argument to the `OrquestaClient` constructor.

```python
from orquesta_sdk import OrquestaClient

api_key = os.environ.get('ORQUESTA_API_KEY', '__API_KEY__')

const client = OrquestaClient(api_key=api_key, ttl= 3600);
```

### Query a prompt

<div id="prompts"/>

```python
from orquesta_sdk import OrquestaClient, OrquestaClienOptions

options = OrquestaClienOptions(ttl=3600)

client = OrquestaClient("__API_KEY__", options)

result = client.prompts.query(
    prompt_key="prompt_key",
    context={"environments": ["production"]},
    variables={"name": "John Doe"},
    metadata={"key": "value"},
)
```

The `metadata` properties are optional.

### Query a rule

<div id="rules"/>

```python
from orquesta_sdk import OrquestaClient, OrquestaClienOptions

options = OrquestaClienOptions(ttl=3600)

client = OrquestaClient("__API_KEY__", options)

# Query an string rule
boolean_result = client.rules.query(
    rule_key="boolean_rule_key",
    default_value=False,
    context={"environments": ["production"]},
    metadata={"key": "value"},
)

# Query an string rule
string_result = client.rules.query(
    rule_key="string_rule_key",
    default_value="my_default_value",
    context={"environments": ["production"]},
    metadata={"key": "value"},
)

# Query an int rule
int_result = client.rules.query(
    rule_key="int_rule_key",
    default_value=100,
    context={"environments": ["production"]},
    metadata={"key": "value"},
)

# Query an list rule
list_result = client.rules.query(
    rule_key="list_rule_key",
    default_value=[],
    context={"environments": ["production"]},
    metadata={"key": "value"},
)

# Query an json rule
json_result = client.rules.query(
    rule_key="json_rule_key",
    default_value=[],
    context={"environments": ["production"]},
    metadata={"key": "value"},
)
```

The `context` and `metadata` properties are optional.
