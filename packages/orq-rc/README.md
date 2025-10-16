# orq-ai-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *orq-ai-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=orq-ai-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary

orq.ai API: orq.ai API documentation

For more information about the API: [orq.ai Documentation](https://docs.orq.ai)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [orq-ai-sdk](#orq-ai-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add orq-ai-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install orq-ai-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add orq-ai-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from orq-ai-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "orq-ai-sdk",
# ]
# ///

from orq_ai_sdk import Orq

sdk = Orq(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from orq_ai_sdk import Orq
import os

async def main():

    async with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as orq:

        res = await orq.contacts.create_async(request={
            "external_id": "user_12345",
            "display_name": "Jane Smith",
            "email": "jane.smith@example.com",
            "avatar_url": "https://example.com/avatars/jane-smith.jpg",
            "tags": [
                "premium",
                "beta-user",
                "enterprise",
            ],
            "metadata": {
                "department": "Engineering",
                "role": "Senior Developer",
                "subscription_tier": "premium",
                "last_login": "2024-01-15T10:30:00Z",
            },
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      | Environment Variable |
| --------- | ---- | ----------- | -------------------- |
| `api_key` | http | HTTP Bearer | `ORQ_API_KEY`        |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [agents](docs/sdks/agents/README.md)

* [retrieve_task](docs/sdks/agents/README.md#retrieve_task) - Retrieve a specific agent task
* [create](docs/sdks/agents/README.md#create) - Create a new agent
* [list](docs/sdks/agents/README.md#list) - List all agents
* [delete](docs/sdks/agents/README.md#delete) - Delete an agent
* [retrieve](docs/sdks/agents/README.md#retrieve) - Get an agent
* [update](docs/sdks/agents/README.md#update) - Update an agent
* [invoke](docs/sdks/agents/README.md#invoke) - Invoke an agent
* [list_tasks](docs/sdks/agents/README.md#list_tasks) - List all tasks for an agent
* [run](docs/sdks/agents/README.md#run) - Run an agent
* [stream_run](docs/sdks/agents/README.md#stream_run) - Run and stream agent execution
* [stream](docs/sdks/agents/README.md#stream) - Stream agent execution events
* [list_actions](docs/sdks/agents/README.md#list_actions) - List all actions
* [retrieve_action](docs/sdks/agents/README.md#retrieve_action) - Retrieve an action executed by an agent task.

### [budgets](docs/sdks/budgets/README.md)

* [list](docs/sdks/budgets/README.md#list) - List budget configurations
* [create](docs/sdks/budgets/README.md#create) - Create budget configuration
* [get](docs/sdks/budgets/README.md#get) - Get budget configuration
* [update](docs/sdks/budgets/README.md#update) - Update budget configuration
* [delete](docs/sdks/budgets/README.md#delete) - Delete budget configuration

### [chunking](docs/sdks/chunking/README.md)

* [parse](docs/sdks/chunking/README.md#parse) - Parse text

### [contacts](docs/sdks/contacts/README.md)

* [create](docs/sdks/contacts/README.md#create) - Create a contact
* [list](docs/sdks/contacts/README.md#list) - List contacts
* [retrieve](docs/sdks/contacts/README.md#retrieve) - Retrieve a contact
* [update](docs/sdks/contacts/README.md#update) - Update a contact
* [delete](docs/sdks/contacts/README.md#delete) - Delete a contact

### [datasets](docs/sdks/datasets/README.md)

* [list](docs/sdks/datasets/README.md#list) - List datasets
* [create](docs/sdks/datasets/README.md#create) - Create a dataset
* [retrieve](docs/sdks/datasets/README.md#retrieve) - Retrieve a dataset
* [update](docs/sdks/datasets/README.md#update) - Update a dataset
* [delete](docs/sdks/datasets/README.md#delete) - Delete a dataset
* [list_datapoints](docs/sdks/datasets/README.md#list_datapoints) - List datapoints
* [create_datapoint](docs/sdks/datasets/README.md#create_datapoint) - Create a datapoint
* [retrieve_datapoint](docs/sdks/datasets/README.md#retrieve_datapoint) - Retrieve a datapoint
* [update_datapoint](docs/sdks/datasets/README.md#update_datapoint) - Update a datapoint
* [delete_datapoint](docs/sdks/datasets/README.md#delete_datapoint) - Delete a datapoint
* [clear](docs/sdks/datasets/README.md#clear) - Delete all datapoints

### [deployments](docs/sdks/deploymentssdk/README.md)

* [list](docs/sdks/deploymentssdk/README.md#list) - List all deployments
* [get_config](docs/sdks/deploymentssdk/README.md#get_config) - Get config
* [invoke](docs/sdks/deploymentssdk/README.md#invoke) - Invoke
* [stream](docs/sdks/deploymentssdk/README.md#stream) - Stream

#### [deployments.metrics](docs/sdks/metrics/README.md)

* [create](docs/sdks/metrics/README.md#create) - Add metrics

### [evals](docs/sdks/evals/README.md)

* [all](docs/sdks/evals/README.md#all) - Get all Evaluators
* [create](docs/sdks/evals/README.md#create) - Create an Evaluator
* [update](docs/sdks/evals/README.md#update) - Update an Evaluator
* [delete](docs/sdks/evals/README.md#delete) - Delete an Evaluator
* [bert_score](docs/sdks/evals/README.md#bert_score) - Run BertScore Evaluator
* [bleu_score](docs/sdks/evals/README.md#bleu_score) - Run BLEU Score Evaluator
* [contains_all](docs/sdks/evals/README.md#contains_all) - Run Contains All Evaluator
* [contains_any](docs/sdks/evals/README.md#contains_any) - Run Contains Any Evaluator
* [contains_email](docs/sdks/evals/README.md#contains_email) - Run Contains Email Evaluator
* [contains_none](docs/sdks/evals/README.md#contains_none) - Run Contains None Evaluator
* [contains_url](docs/sdks/evals/README.md#contains_url) - Run Contains URL Evaluator
* [contains_valid_link](docs/sdks/evals/README.md#contains_valid_link) - Run Contains Valid Link Evaluator
* [contains](docs/sdks/evals/README.md#contains) - Run Contains Evaluator
* [ends_with](docs/sdks/evals/README.md#ends_with) - Run Ends With Evaluator
* [exact_match](docs/sdks/evals/README.md#exact_match) - Run Exact Match Evaluator
* [length_between](docs/sdks/evals/README.md#length_between) - Run Length Between Evaluator
* [length_greater_than](docs/sdks/evals/README.md#length_greater_than) - Run Length Greater Than Evaluator
* [length_less_than](docs/sdks/evals/README.md#length_less_than) - Run Length Less Than Evaluator
* [valid_json](docs/sdks/evals/README.md#valid_json) - Run JSON Validation Evaluator
* [age_appropriate](docs/sdks/evals/README.md#age_appropriate) - Run Age Appropriate Evaluator
* [bot_detection](docs/sdks/evals/README.md#bot_detection) - Run Bot Detection Evaluator
* [fact_checking_knowledge_base](docs/sdks/evals/README.md#fact_checking_knowledge_base) - Run Fact Checking Knowledge Base Evaluator
* [grammar](docs/sdks/evals/README.md#grammar) - Run Grammar Evaluator
* [localization](docs/sdks/evals/README.md#localization) - Run Localization Evaluator
* [pii](docs/sdks/evals/README.md#pii) - Run PII Evaluator
* [sentiment_classification](docs/sdks/evals/README.md#sentiment_classification) - Run Sentiment Classification Evaluator
* [summarization](docs/sdks/evals/README.md#summarization) - Run Summarization Evaluator
* [tone_of_voice](docs/sdks/evals/README.md#tone_of_voice) - Run Tone of Voice Evaluator
* [translation](docs/sdks/evals/README.md#translation) - Run Translation Evaluator
* [ragas_coherence](docs/sdks/evals/README.md#ragas_coherence) - Run Coherence Evaluator
* [ragas_conciseness](docs/sdks/evals/README.md#ragas_conciseness) - Run Conciseness Evaluator
* [ragas_context_precision](docs/sdks/evals/README.md#ragas_context_precision) - Run Context Precision Evaluator
* [ragas_context_recall](docs/sdks/evals/README.md#ragas_context_recall) - Run Context Recall Evaluator
* [ragas_context_entities_recall](docs/sdks/evals/README.md#ragas_context_entities_recall) - Run Context Entities Recall Evaluator
* [ragas_correctness](docs/sdks/evals/README.md#ragas_correctness) - Run Correctness Evaluator
* [ragas_faithfulness](docs/sdks/evals/README.md#ragas_faithfulness) - Run Faithfulness Evaluator
* [ragas_harmfulness](docs/sdks/evals/README.md#ragas_harmfulness) - Run Harmfulness Evaluator
* [ragas_maliciousness](docs/sdks/evals/README.md#ragas_maliciousness) - Run Maliciousness Evaluator
* [ragas_noise_sensitivity](docs/sdks/evals/README.md#ragas_noise_sensitivity) - Run Noise Sensitivity Evaluator
* [ragas_response_relevancy](docs/sdks/evals/README.md#ragas_response_relevancy) - Run Response Relevancy Evaluator
* [ragas_summarization](docs/sdks/evals/README.md#ragas_summarization) - Run Summarization Evaluator
* [invoke](docs/sdks/evals/README.md#invoke) - Invoke a Custom Evaluator

### [feedback](docs/sdks/feedback/README.md)

* [create](docs/sdks/feedback/README.md#create) - Submit feedback

### [files](docs/sdks/files/README.md)

* [create](docs/sdks/files/README.md#create) - Create file
* [list](docs/sdks/files/README.md#list) - List all files
* [get](docs/sdks/files/README.md#get) - Retrieve a file
* [delete](docs/sdks/files/README.md#delete) - Delete file

### [knowledge](docs/sdks/knowledge/README.md)

* [list](docs/sdks/knowledge/README.md#list) - List all knowledge bases
* [create](docs/sdks/knowledge/README.md#create) - Create a knowledge
* [retrieve](docs/sdks/knowledge/README.md#retrieve) - Retrieves a knowledge base
* [update](docs/sdks/knowledge/README.md#update) - Updates a knowledge
* [delete](docs/sdks/knowledge/README.md#delete) - Deletes a knowledge
* [search](docs/sdks/knowledge/README.md#search) - Search knowledge base
* [list_datasources](docs/sdks/knowledge/README.md#list_datasources) - List all datasources
* [create_datasource](docs/sdks/knowledge/README.md#create_datasource) - Create a new datasource
* [retrieve_datasource](docs/sdks/knowledge/README.md#retrieve_datasource) - Retrieve a datasource
* [delete_datasource](docs/sdks/knowledge/README.md#delete_datasource) - Deletes a datasource
* [update_datasource](docs/sdks/knowledge/README.md#update_datasource) - Update a datasource
* [create_chunks](docs/sdks/knowledge/README.md#create_chunks) - Create chunks for a datasource
* [list_chunks](docs/sdks/knowledge/README.md#list_chunks) - List all chunks for a datasource
* [delete_chunks](docs/sdks/knowledge/README.md#delete_chunks) - Delete multiple chunks
* [list_chunks_paginated](docs/sdks/knowledge/README.md#list_chunks_paginated) - List chunks with offset-based pagination
* [get_chunks_count](docs/sdks/knowledge/README.md#get_chunks_count) - Get chunks total count
* [update_chunk](docs/sdks/knowledge/README.md#update_chunk) - Update a chunk
* [delete_chunk](docs/sdks/knowledge/README.md#delete_chunk) - Delete a chunk
* [retrieve_chunk](docs/sdks/knowledge/README.md#retrieve_chunk) - Retrieve a chunk

### [memory_stores](docs/sdks/memorystores/README.md)

* [list](docs/sdks/memorystores/README.md#list) - List memory stores
* [create](docs/sdks/memorystores/README.md#create) - Create memory store
* [retrieve](docs/sdks/memorystores/README.md#retrieve) - Retrieve memory store
* [update](docs/sdks/memorystores/README.md#update) - Update memory store
* [delete](docs/sdks/memorystores/README.md#delete) - Delete memory store
* [list_memories](docs/sdks/memorystores/README.md#list_memories) - List all memories
* [create_memory](docs/sdks/memorystores/README.md#create_memory) - Create a new memory
* [retrieve_memory](docs/sdks/memorystores/README.md#retrieve_memory) - Retrieve a specific memory
* [update_memory](docs/sdks/memorystores/README.md#update_memory) - Update a specific memory
* [delete_memory](docs/sdks/memorystores/README.md#delete_memory) - Delete a specific memory
* [list_documents](docs/sdks/memorystores/README.md#list_documents) - List all documents for a memory
* [create_document](docs/sdks/memorystores/README.md#create_document) - Create a new memory document
* [retrieve_document](docs/sdks/memorystores/README.md#retrieve_document) - Retrieve a specific memory document
* [update_document](docs/sdks/memorystores/README.md#update_document) - Update a specific memory document
* [delete_document](docs/sdks/memorystores/README.md#delete_document) - Delete a specific memory document

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - List models

### [prompts](docs/sdks/prompts/README.md)

* [list](docs/sdks/prompts/README.md#list) - List all prompts
* [create](docs/sdks/prompts/README.md#create) - Create a prompt
* [retrieve](docs/sdks/prompts/README.md#retrieve) - Retrieve a prompt
* [update](docs/sdks/prompts/README.md#update) - Update a prompt
* [delete](docs/sdks/prompts/README.md#delete) - Delete a prompt
* [list_versions](docs/sdks/prompts/README.md#list_versions) - List all prompt versions
* [get_version](docs/sdks/prompts/README.md#get_version) - Retrieve a prompt version

### [remoteconfigs](docs/sdks/remoteconfigs/README.md)

* [retrieve](docs/sdks/remoteconfigs/README.md#retrieve) - Retrieve a remote config

### [tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - List tools
* [create](docs/sdks/tools/README.md#create) - Create tool
* [update](docs/sdks/tools/README.md#update) - Update tool
* [delete](docs/sdks/tools/README.md#delete) - Delete tool
* [retrieve](docs/sdks/tools/README.md#retrieve) - Retrieve tool
* [duplicate](docs/sdks/tools/README.md#duplicate) - Duplicate tool

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
from orq_ai_sdk import Orq
import os


with Orq(
    environment="<value>",
    contact_id="<id>",
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.deployments.stream(key="<key>")

    assert res is not None

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.create(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, purpose="retrieval")

    assert res is not None

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import BackoffStrategy, RetryConfig
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import BackoffStrategy, RetryConfig
import os


with Orq(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`OrqError`](./src/orq_ai_sdk/models/orqerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from orq_ai_sdk import Orq, models
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:
    res = None
    try:

        res = orq.contacts.retrieve(id="<id>")

        assert res is not None

        # Handle response
        print(res)


    except models.OrqError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.RetrieveContactContactsResponseBody):
            print(e.data.error)  # str
```

### Error Classes
**Primary error:**
* [`OrqError`](./src/orq_ai_sdk/models/orqerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (101)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`OrqError`](./src/orq_ai_sdk/models/orqerror.py)**:
* [`HonoAPIError`](./src/orq_ai_sdk/models/honoapierror.py): Applicable to 10 of 136 methods.*
* [`RetrieveContactContactsResponseBody`](./src/orq_ai_sdk/models/retrievecontactcontactsresponsebody.py): Contact not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`UpdateContactContactsResponseBody`](./src/orq_ai_sdk/models/updatecontactcontactsresponsebody.py): Contact not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`DeleteContactResponseBody`](./src/orq_ai_sdk/models/deletecontactresponsebody.py): Contact not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`GetAgentTaskAgentsResponseBody`](./src/orq_ai_sdk/models/getagenttaskagentsresponsebody.py): Agent task not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`DeleteAgentResponseBody`](./src/orq_ai_sdk/models/deleteagentresponsebody.py): Agent not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`GetAgentAgentsResponseBody`](./src/orq_ai_sdk/models/getagentagentsresponsebody.py): Agent not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`UpdateAgentAgentsResponseBody`](./src/orq_ai_sdk/models/updateagentagentsresponsebody.py): Agent not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`ListAgentTasksAgentsResponseBody`](./src/orq_ai_sdk/models/listagenttasksagentsresponsebody.py): No agent tasks found. Status code `404`. Applicable to 1 of 136 methods.*
* [`StreamRunAgentAgentsResponseBody`](./src/orq_ai_sdk/models/streamrunagentagentsresponsebody.py): Model not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`StreamAgentAgentsResponseBody`](./src/orq_ai_sdk/models/streamagentagentsresponsebody.py): Agent not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`UpdatePromptPromptsResponseBody`](./src/orq_ai_sdk/models/updatepromptpromptsresponsebody.py): Prompt not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`GetPromptVersionPromptsResponseBody`](./src/orq_ai_sdk/models/getpromptversionpromptsresponsebody.py): Not Found - The prompt or prompt version does not exist. Status code `404`. Applicable to 1 of 136 methods.*
* [`GetEvalsEvalsResponseBody`](./src/orq_ai_sdk/models/getevalsevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 136 methods.*
* [`CreateEvalEvalsResponseBody`](./src/orq_ai_sdk/models/createevalevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 136 methods.*
* [`UpdateEvalEvalsResponseBody`](./src/orq_ai_sdk/models/updateevalevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 136 methods.*
* [`DeleteEvalResponseBody`](./src/orq_ai_sdk/models/deleteevalresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsBertScoreEvalsResponseBody`](./src/orq_ai_sdk/models/evalsbertscoreevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsBleuScoreEvalsResponseBody`](./src/orq_ai_sdk/models/evalsbleuscoreevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsAllEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsallevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsAnyEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsanyevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsEmailEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsemailevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsNoneEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsnoneevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsURLEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsurlevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsValidLinkEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsvalidlinkevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsContainsEvalsResponseBody`](./src/orq_ai_sdk/models/evalscontainsevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsEndsWithEvalsResponseBody`](./src/orq_ai_sdk/models/evalsendswithevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsExactMatchEvalsResponseBody`](./src/orq_ai_sdk/models/evalsexactmatchevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsLengthBetweenEvalsResponseBody`](./src/orq_ai_sdk/models/evalslengthbetweenevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsLengthGreaterThanEvalsResponseBody`](./src/orq_ai_sdk/models/evalslengthgreaterthanevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsLengthLessThanEvalsResponseBody`](./src/orq_ai_sdk/models/evalslengthlessthanevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsValidJSONEvalsResponseBody`](./src/orq_ai_sdk/models/evalsvalidjsonevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsAgeAppropriateEvalsResponseBody`](./src/orq_ai_sdk/models/evalsageappropriateevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsBotDetectionEvalsResponseBody`](./src/orq_ai_sdk/models/evalsbotdetectionevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsFactCheckingKnowledgeBaseEvalsResponseBody`](./src/orq_ai_sdk/models/evalsfactcheckingknowledgebaseevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsGrammarEvalsResponseBody`](./src/orq_ai_sdk/models/evalsgrammarevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsLocalizationEvalsResponseBody`](./src/orq_ai_sdk/models/evalslocalizationevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsPiiEvalsResponseBody`](./src/orq_ai_sdk/models/evalspiievalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsSentimentClassificationEvalsResponseBody`](./src/orq_ai_sdk/models/evalssentimentclassificationevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsSummarizationEvalsResponseBody`](./src/orq_ai_sdk/models/evalssummarizationevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsToneOfVoiceEvalsResponseBody`](./src/orq_ai_sdk/models/evalstoneofvoiceevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsTranslationEvalsResponseBody`](./src/orq_ai_sdk/models/evalstranslationevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasCoherenceEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragascoherenceevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasConcisenessEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasconcisenessevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextPrecisionEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragascontextprecisionevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextRecallEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragascontextrecallevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextEntitiesRecallEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragascontextentitiesrecallevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasCorrectnessEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragascorrectnessevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasFaithfulnessEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasfaithfulnessevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasHarmfulnessEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasharmfulnessevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasMaliciousnessEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasmaliciousnessevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasNoiseSensitivityEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasnoisesensitivityevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasResponseRelevancyEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragasresponserelevancyevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`EvalsRagasSummarizationEvalsResponseBody`](./src/orq_ai_sdk/models/evalsragassummarizationevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`InvokeEvalEvalsResponseBody`](./src/orq_ai_sdk/models/invokeevalevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 136 methods.*
* [`UpdateToolToolsResponseBody`](./src/orq_ai_sdk/models/updatetooltoolsresponsebody.py): Tool not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`DuplicateToolToolsResponseBody`](./src/orq_ai_sdk/models/duplicatetooltoolsresponsebody.py): Tool not found. Status code `404`. Applicable to 1 of 136 methods.*
* [`CreateAgentAgentsResponseBody`](./src/orq_ai_sdk/models/createagentagentsresponsebody.py): Agent with this key already exists in the workspace. Status code `409`. Applicable to 1 of 136 methods.*
* [`EvalsBertScoreEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsbertscoreevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsBleuScoreEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsbleuscoreevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsAllEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsallevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsAnyEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsanyevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsEmailEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsemailevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsNoneEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsnoneevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsURLEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsurlevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsValidLinkEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsvalidlinkevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsContainsEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalscontainsevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsEndsWithEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsendswithevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsExactMatchEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsexactmatchevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsLengthBetweenEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalslengthbetweenevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsLengthGreaterThanEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalslengthgreaterthanevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsLengthLessThanEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalslengthlessthanevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsValidJSONEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsvalidjsonevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsAgeAppropriateEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsageappropriateevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsBotDetectionEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsbotdetectionevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsFactCheckingKnowledgeBaseEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsfactcheckingknowledgebaseevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsGrammarEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsgrammarevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsLocalizationEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalslocalizationevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsPiiEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalspiievalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsSentimentClassificationEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalssentimentclassificationevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsSummarizationEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalssummarizationevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsToneOfVoiceEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalstoneofvoiceevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsTranslationEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalstranslationevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasCoherenceEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragascoherenceevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasConcisenessEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasconcisenessevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextPrecisionEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragascontextprecisionevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextRecallEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragascontextrecallevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasContextEntitiesRecallEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragascontextentitiesrecallevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasCorrectnessEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragascorrectnessevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasFaithfulnessEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasfaithfulnessevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasHarmfulnessEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasharmfulnessevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasMaliciousnessEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasmaliciousnessevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasNoiseSensitivityEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasnoisesensitivityevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasResponseRelevancyEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragasresponserelevancyevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`EvalsRagasSummarizationEvalsResponseResponseBody`](./src/orq_ai_sdk/models/evalsragassummarizationevalsresponseresponsebody.py): Internal server error. Status code `500`. Applicable to 1 of 136 methods.*
* [`InvokeEvalEvalsResponseResponseBody`](./src/orq_ai_sdk/models/invokeevalevalsresponseresponsebody.py): Error running the evaluator. Status code `500`. Applicable to 1 of 136 methods.*
* [`ResponseValidationError`](./src/orq_ai_sdk/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from orq_ai_sdk import Orq
import os


with Orq(
    server_url="https://my.orq.ai",
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from orq_ai_sdk import Orq
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Orq(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Orq(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Orq` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from orq_ai_sdk import Orq
import os
def main():

    with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as orq:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as orq:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from orq_ai_sdk import Orq
import logging

logging.basicConfig(level=logging.DEBUG)
s = Orq(debug_logger=logging.getLogger("orq_ai_sdk"))
```

You can also enable a default debug logger by setting an environment variable `ORQ_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=orq-ai-sdk&utm_campaign=python)
