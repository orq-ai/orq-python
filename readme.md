<p align="left">
  <a href="https://orquesta.dev" target="_blank">
    <img src="https://static.wixstatic.com/media/e063e5_4f60988535a643218a02ad84cf60b7cd~mv2.png/v1/fill/w_130,h_108,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo%2001.png" alt="Orquesta"  height="84">
  </a>
</p>

# Orquesta Python SDK

**This library allows you to quickly and easily use the Orquesta API via Python.**

# Installation

## Prerequisites

- Python version 2.7 and 3.5+
- A free Orquesta account from [orquesta.dev](https://orquesta.dev).

### Install package

```bash
pip install orquestadev
```

## Dependencies

- [requests](https://github.com/psf/requests)

## Usage

#### Query a rule with context

```python

import os
import orquestadev

client = orquestadev.OrquestaClient(os.environ.get('ORQUESTA_API_KEY'))
result = client.query('<your_rule_key>', '<your_default_value>', {'<your_field_key>': '<your_value>'})

## Example

result = client.query(
            "kill_switch", false, {"environments": "production", "isAdmin": True}
        )
```

#### Query a rule without context

```python

import os
import orquestadev

client = orquestadev.OrquestaClient(os.environ.get('ORQUESTA_API_KEY'))
client.query('<your_rule_key>', '<your_default_value>')

## Example

result = client.query("kill_switch", false)
```
