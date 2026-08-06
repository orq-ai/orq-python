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
# requires-python = ">=3.10"
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

    res = orq.evals.all(limit=10)

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

        res = await orq.evals.all_async(limit=10)

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

    res = orq.evals.all(limit=10)

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](docs/sdks/agents/README.md)

* [create](docs/sdks/agents/README.md#create) - Create agent
* [list](docs/sdks/agents/README.md#list) - List agents
* [delete](docs/sdks/agents/README.md#delete) - Delete agent
* [retrieve](docs/sdks/agents/README.md#retrieve) - Retrieve agent
* [update](docs/sdks/agents/README.md#update) - Update agent
* [~~invoke~~](docs/sdks/agents/README.md#invoke) - Execute an agent task :warning: **Deprecated**
* [~~run~~](docs/sdks/agents/README.md#run) - Run an agent with configuration :warning: **Deprecated**
* [~~stream_run~~](docs/sdks/agents/README.md#stream_run) - Run agent with streaming response :warning: **Deprecated**
* [~~stream~~](docs/sdks/agents/README.md#stream) - Stream agent execution in real-time :warning: **Deprecated**

#### [~~Agents.Responses~~](docs/sdks/orqresponses/README.md)

* [~~create~~](docs/sdks/orqresponses/README.md#create) - Create response :warning: **Deprecated**
* [~~get~~](docs/sdks/orqresponses/README.md#get) - Get response :warning: **Deprecated**

### [Alerts](docs/sdks/alerts/README.md)

* [list](docs/sdks/alerts/README.md#list) - List alerts
* [create](docs/sdks/alerts/README.md#create) - Create an alert
* [get](docs/sdks/alerts/README.md#get) - Retrieve an alert
* [delete](docs/sdks/alerts/README.md#delete) - Delete an alert
* [update](docs/sdks/alerts/README.md#update) - Update an alert
* [list_triggers](docs/sdks/alerts/README.md#list_triggers) - List alert triggers
* [list_trigger_events](docs/sdks/alerts/README.md#list_trigger_events) - List alert trigger events

### [AnnotationQueues](docs/sdks/annotationqueues/README.md)

* [list](docs/sdks/annotationqueues/README.md#list) - List annotation queues
* [create](docs/sdks/annotationqueues/README.md#create) - Create an annotation queue
* [retrieve](docs/sdks/annotationqueues/README.md#retrieve) - Retrieve an annotation queue
* [update](docs/sdks/annotationqueues/README.md#update) - Edit an annotation queue
* [delete](docs/sdks/annotationqueues/README.md#delete) - Delete an annotation queue
* [clear](docs/sdks/annotationqueues/README.md#clear) - Delete all items
* [list_items](docs/sdks/annotationqueues/README.md#list_items) - Query items from an annotation queue
* [add_items](docs/sdks/annotationqueues/README.md#add_items) - Add items to an annotation queue
* [remove_items](docs/sdks/annotationqueues/README.md#remove_items) - Remove annotation queue items
* [retrieve_item](docs/sdks/annotationqueues/README.md#retrieve_item) - Retrieve an annotation queue item

### [Annotations](docs/sdks/annotations/README.md)

* [create](docs/sdks/annotations/README.md#create) - Annotate a span
* [delete](docs/sdks/annotations/README.md#delete) - Remove an annotation from a span

### [ApiKeys](docs/sdks/apikeys/README.md)

* [list](docs/sdks/apikeys/README.md#list) - List API keys
* [create](docs/sdks/apikeys/README.md#create) - Create a new API key
* [list_capabilities](docs/sdks/apikeys/README.md#list_capabilities) - List capability catalog
* [get](docs/sdks/apikeys/README.md#get) - Retrieve an API key
* [delete](docs/sdks/apikeys/README.md#delete) - Delete an API key
* [update](docs/sdks/apikeys/README.md#update) - Update an API key

### [Budgets](docs/sdks/budgets/README.md)

* [list](docs/sdks/budgets/README.md#list) - List budgets
* [create](docs/sdks/budgets/README.md#create) - Create a new budget
* [get](docs/sdks/budgets/README.md#get) - Retrieve a budget
* [delete](docs/sdks/budgets/README.md#delete) - Delete a budget
* [update](docs/sdks/budgets/README.md#update) - Update a budget
* [reset_consumption](docs/sdks/budgets/README.md#reset_consumption) - Reset budget consumption

### [Chunking](docs/sdks/chunking/README.md)

* [parse](docs/sdks/chunking/README.md#parse) - Parse text

### [Datasets](docs/sdks/datasets/README.md)

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

### [Deployments](docs/sdks/deployments/README.md)

* [invoke](docs/sdks/deployments/README.md#invoke) - Invoke
* [list](docs/sdks/deployments/README.md#list) - List all deployments
* [get_config](docs/sdks/deployments/README.md#get_config) - Get config
* [stream](docs/sdks/deployments/README.md#stream) - Stream

### [Evals](docs/sdks/evals/README.md)

* [all](docs/sdks/evals/README.md#all) - Get all Evaluators
* [create](docs/sdks/evals/README.md#create) - Create an Evaluator
* [get](docs/sdks/evals/README.md#get) - Retrieve an Evaluator
* [update](docs/sdks/evals/README.md#update) - Update an Evaluator
* [delete](docs/sdks/evals/README.md#delete) - Delete an Evaluator
* [invoke](docs/sdks/evals/README.md#invoke) - Invoke a Custom Evaluator
* [list_versions](docs/sdks/evals/README.md#list_versions) - List evaluator versions

### [Feedback](docs/sdks/feedback/README.md)

* [remove_evaluation](docs/sdks/feedback/README.md#remove_evaluation)
* [create_evaluation](docs/sdks/feedback/README.md#create_evaluation)
* [remove](docs/sdks/feedback/README.md#remove)
* [create](docs/sdks/feedback/README.md#create)

### [Files](docs/sdks/files/README.md)

* [list](docs/sdks/files/README.md#list) - List all files
* [create](docs/sdks/files/README.md#create) - Upload a file
* [get_content](docs/sdks/files/README.md#get_content) - Download file content
* [get](docs/sdks/files/README.md#get) - Retrieve a file
* [delete](docs/sdks/files/README.md#delete) - Delete a file
* [update](docs/sdks/files/README.md#update) - Update a file

### [GuardrailRules](docs/sdks/guardrailrules/README.md)

* [list](docs/sdks/guardrailrules/README.md#list) - List guardrail rules
* [create](docs/sdks/guardrailrules/README.md#create) - Create guardrail rule
* [list_used_guardrails](docs/sdks/guardrailrules/README.md#list_used_guardrails) - List used guardrails
* [delete](docs/sdks/guardrailrules/README.md#delete) - Delete guardrail rule
* [retrieve](docs/sdks/guardrailrules/README.md#retrieve) - Get guardrail rule
* [update](docs/sdks/guardrailrules/README.md#update) - Update guardrail rule

### [HumanReviewSets](docs/sdks/humanreviewsets/README.md)

* [list](docs/sdks/humanreviewsets/README.md#list) - Get all human review sets
* [create](docs/sdks/humanreviewsets/README.md#create) - Create a human review set
* [get](docs/sdks/humanreviewsets/README.md#get) - Get a human review set by ID
* [update](docs/sdks/humanreviewsets/README.md#update) - Update a human review set
* [delete](docs/sdks/humanreviewsets/README.md#delete) - Delete a human review set

### [Identities](docs/sdks/identities/README.md)

* [list](docs/sdks/identities/README.md#list) - List identities
* [create](docs/sdks/identities/README.md#create) - Create an identity
* [retrieve](docs/sdks/identities/README.md#retrieve) - Retrieve an identity
* [delete](docs/sdks/identities/README.md#delete) - Delete an identity
* [update](docs/sdks/identities/README.md#update) - Update an identity

### [Knowledge](docs/sdks/knowledge/README.md)

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

### [Logs](docs/sdks/logs/README.md)

* [aggregate](docs/sdks/logs/README.md#aggregate) - Aggregate logs
* [list_facets](docs/sdks/logs/README.md#list_facets) - List log facets
* [list_facet_values](docs/sdks/logs/README.md#list_facet_values) - List facet values
* [list_fields](docs/sdks/logs/README.md#list_fields) - List log fields
* [find_patterns](docs/sdks/logs/README.md#find_patterns) - Find log patterns
* [query](docs/sdks/logs/README.md#query) - Query logs with OQL
* [search](docs/sdks/logs/README.md#search) - Search logs
* [get](docs/sdks/logs/README.md#get) - Get a single log
* [context](docs/sdks/logs/README.md#context) - Get surrounding log context
* [list_trace_logs](docs/sdks/logs/README.md#list_trace_logs) - List logs for a trace

### [ManagementKeys](docs/sdks/managementkeys/README.md)

* [list](docs/sdks/managementkeys/README.md#list) - List management keys
* [create](docs/sdks/managementkeys/README.md#create) - Create a new management key
* [list_capabilities](docs/sdks/managementkeys/README.md#list_capabilities) - List management capability catalog
* [get](docs/sdks/managementkeys/README.md#get) - Retrieve a management key
* [delete](docs/sdks/managementkeys/README.md#delete) - Delete a management key
* [update](docs/sdks/managementkeys/README.md#update) - Update a management key

### [MemoryStores](docs/sdks/memorystores/README.md)

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

### [Models](docs/sdks/models/README.md)

* [create](docs/sdks/models/README.md#create) - Create custom model
* [create_aws_bedrock](docs/sdks/models/README.md#create_aws_bedrock) - Create AWS Bedrock custom model
* [validate_aws_bedrock](docs/sdks/models/README.md#validate_aws_bedrock) - Validate AWS Bedrock inference profile
* [update_aws_bedrock](docs/sdks/models/README.md#update_aws_bedrock) - Update AWS Bedrock custom model
* [azure_foundry_deployments](docs/sdks/models/README.md#azure_foundry_deployments) - List Azure Foundry deployments under a resource
* [import_litellm](docs/sdks/models/README.md#import_litellm) - Import models from LiteLLM
* [list_litellm](docs/sdks/models/README.md#list_litellm) - List models from configured LiteLLM instance
* [create_openai_like](docs/sdks/models/README.md#create_openai_like) - Create OpenAI-compatible custom model
* [update_openai_like](docs/sdks/models/README.md#update_openai_like) - Update OpenAI-compatible custom model
* [validate](docs/sdks/models/README.md#validate) - Validate model endpoint
* [create_vertex](docs/sdks/models/README.md#create_vertex) - Create Vertex AI custom model
* [delete](docs/sdks/models/README.md#delete) - Delete custom model
* [update](docs/sdks/models/README.md#update) - Update custom model
* [enable](docs/sdks/models/README.md#enable) - Enable model for workspace
* [disable](docs/sdks/models/README.md#disable) - Disable model for workspace
* [list](docs/sdks/models/README.md#list) - List models

### [Notifiers](docs/sdks/notifiers/README.md)

* [list](docs/sdks/notifiers/README.md#list) - List notifiers
* [create](docs/sdks/notifiers/README.md#create) - Create a notifier
* [get](docs/sdks/notifiers/README.md#get) - Retrieve a notifier
* [delete](docs/sdks/notifiers/README.md#delete) - Delete a notifier
* [update](docs/sdks/notifiers/README.md#update) - Update a notifier

### [People](docs/sdks/people/README.md)

* [list](docs/sdks/people/README.md#list) - List all people
* [create](docs/sdks/people/README.md#create) - Invite people to a workspace
* [get](docs/sdks/people/README.md#get) - Retrieve a person
* [delete](docs/sdks/people/README.md#delete) - Delete a person
* [update](docs/sdks/people/README.md#update) - Update a person
* [resend_invitation](docs/sdks/people/README.md#resend_invitation) - Resend invitation

### [Pii](docs/sdks/pii/README.md)

* [detect](docs/sdks/pii/README.md#detect) - Detect PII
* [redact](docs/sdks/pii/README.md#redact) - Redact PII
* [restore](docs/sdks/pii/README.md#restore) - Restore redacted text

### [Policies](docs/sdks/policies/README.md)

* [list](docs/sdks/policies/README.md#list) - List policies
* [create](docs/sdks/policies/README.md#create) - Create policy
* [delete](docs/sdks/policies/README.md#delete) - Delete policy
* [retrieve](docs/sdks/policies/README.md#retrieve) - Get policy
* [update](docs/sdks/policies/README.md#update) - Update policy

### [Projects](docs/sdks/projects/README.md)

* [list](docs/sdks/projects/README.md#list) - List all projects
* [create](docs/sdks/projects/README.md#create) - Create a new project
* [get](docs/sdks/projects/README.md#get) - Retrieve a project
* [delete](docs/sdks/projects/README.md#delete) - Delete a project
* [update](docs/sdks/projects/README.md#update) - Update a project

### [Prompts](docs/sdks/prompts/README.md)

* [list](docs/sdks/prompts/README.md#list) - List all prompts
* [create](docs/sdks/prompts/README.md#create) - Create a prompt
* [retrieve](docs/sdks/prompts/README.md#retrieve) - Retrieve a prompt
* [update](docs/sdks/prompts/README.md#update) - Update a prompt
* [delete](docs/sdks/prompts/README.md#delete) - Delete a prompt
* [list_versions](docs/sdks/prompts/README.md#list_versions) - List all prompt versions
* [get_version](docs/sdks/prompts/README.md#get_version) - Retrieve a prompt version

### [Reporting](docs/sdks/reporting/README.md)

* [query](docs/sdks/reporting/README.md#query) - Query reporting metrics

### [Responses](docs/sdks/responses/README.md)

* [create](docs/sdks/responses/README.md#create) - Create response
* [get](docs/sdks/responses/README.md#get) - Retrieve response

### [Router](docs/sdks/router/README.md)

* [ocr](docs/sdks/router/README.md#ocr) - Extracts text content while maintaining document structure and hierarchy

#### [Router.Audio.Speech](docs/sdks/speech/README.md)

* [create](docs/sdks/speech/README.md#create) - Create speech

#### [Router.Audio.Transcriptions](docs/sdks/transcriptions/README.md)

* [create](docs/sdks/transcriptions/README.md#create) - Create transcription

#### [Router.Audio.Translations](docs/sdks/translations/README.md)

* [create](docs/sdks/translations/README.md#create) - Create translation

#### [Router.Chat.Completions](docs/sdks/orqcompletions/README.md)

* [create](docs/sdks/orqcompletions/README.md#create) - Create chat completion

#### [Router.Completions](docs/sdks/completions/README.md)

* [create](docs/sdks/completions/README.md#create) - Create completion

#### [Router.Embeddings](docs/sdks/embeddings/README.md)

* [create](docs/sdks/embeddings/README.md#create) - Create embeddings

#### [Router.Images.Edits](docs/sdks/edits/README.md)

* [create](docs/sdks/edits/README.md#create) - Create image edit

#### [Router.Images.Generations](docs/sdks/generations/README.md)

* [create](docs/sdks/generations/README.md#create) - Create image

#### [Router.Images.Variations](docs/sdks/variations/README.md)

* [create](docs/sdks/variations/README.md#create) - Create image variation

#### [Router.Moderations](docs/sdks/moderations/README.md)

* [create](docs/sdks/moderations/README.md#create) - Create moderation

#### [Router.Rerank](docs/sdks/rerank/README.md)

* [create](docs/sdks/rerank/README.md#create) - Create rerank

### [RoutingRules](docs/sdks/routingrules/README.md)

* [list](docs/sdks/routingrules/README.md#list) - List routing rules
* [create](docs/sdks/routingrules/README.md#create) - Create routing rule
* [list_used_models](docs/sdks/routingrules/README.md#list_used_models) - List used models
* [delete](docs/sdks/routingrules/README.md#delete) - Delete routing rule
* [retrieve](docs/sdks/routingrules/README.md#retrieve) - Get routing rule
* [update](docs/sdks/routingrules/README.md#update) - Update routing rule

### [Schedules](docs/sdks/schedules/README.md)

* [list](docs/sdks/schedules/README.md#list) - List schedules
* [create](docs/sdks/schedules/README.md#create) - Create schedule
* [delete](docs/sdks/schedules/README.md#delete) - Delete schedule
* [retrieve](docs/sdks/schedules/README.md#retrieve) - Retrieve schedule
* [update](docs/sdks/schedules/README.md#update) - Update schedule
* [trigger](docs/sdks/schedules/README.md#trigger) - Trigger schedule execution

### [Skills](docs/sdks/skills/README.md)

* [list](docs/sdks/skills/README.md#list) - List all skills
* [create](docs/sdks/skills/README.md#create) - Create a new skill
* [get](docs/sdks/skills/README.md#get) - Retrieve a skill
* [delete](docs/sdks/skills/README.md#delete) - Delete a skill
* [update](docs/sdks/skills/README.md#update) - Update a skill

### [SmartRouters](docs/sdks/smartrouters/README.md)

* [list](docs/sdks/smartrouters/README.md#list) - List Smart Routers
* [create](docs/sdks/smartrouters/README.md#create) - Create a Smart Router
* [get](docs/sdks/smartrouters/README.md#get) - Retrieve a Smart Router
* [delete](docs/sdks/smartrouters/README.md#delete) - Delete a Smart Router
* [update](docs/sdks/smartrouters/README.md#update) - Update a Smart Router
* [set_enabled](docs/sdks/smartrouters/README.md#set_enabled) - Enable or disable a Smart Router

### [Tools](docs/sdks/tools/README.md)

* [list](docs/sdks/tools/README.md#list) - List tools
* [create](docs/sdks/tools/README.md#create) - Create tool
* [update](docs/sdks/tools/README.md#update) - Update tool
* [delete](docs/sdks/tools/README.md#delete) - Delete tool
* [retrieve](docs/sdks/tools/README.md#retrieve) - Retrieve tool
* [list_versions](docs/sdks/tools/README.md#list_versions) - List tool versions
* [get_version](docs/sdks/tools/README.md#get_version) - Get tool version

### [Traces](docs/sdks/traces/README.md)

* [aggregate](docs/sdks/traces/README.md#aggregate) - Aggregate traces
* [list_facets](docs/sdks/traces/README.md#list_facets) - List trace facets
* [list_facet_values](docs/sdks/traces/README.md#list_facet_values) - List trace facet values
* [list_fields](docs/sdks/traces/README.md#list_fields) - List trace fields
* [query](docs/sdks/traces/README.md#query) - Query traces with OQL
* [search](docs/sdks/traces/README.md#search) - Search traces
* [get](docs/sdks/traces/README.md#get) - Get trace
* [list_spans](docs/sdks/traces/README.md#list_spans) - List trace spans
* [get_span](docs/sdks/traces/README.md#get_span) - Get trace span

### [Webhooks](docs/sdks/webhooks/README.md)

* [list](docs/sdks/webhooks/README.md#list) - List webhooks
* [create](docs/sdks/webhooks/README.md#create) - Create a webhook
* [count](docs/sdks/webhooks/README.md#count) - Count webhooks
* [~~query~~](docs/sdks/webhooks/README.md#query) - Query webhooks :warning: **Deprecated**
* [generate_secret](docs/sdks/webhooks/README.md#generate_secret) - Generate a webhook secret
* [get](docs/sdks/webhooks/README.md#get) - Retrieve a webhook
* [delete](docs/sdks/webhooks/README.md#delete) - Delete a webhook
* [update](docs/sdks/webhooks/README.md#update) - Update a webhook

### [WorkspaceSettings](docs/sdks/workspacesettingssdk/README.md)

* [get](docs/sdks/workspacesettingssdk/README.md#get) - Retrieve workspace settings
* [update](docs/sdks/workspacesettingssdk/README.md#update) - Update workspace settings

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
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.deployments.stream(key="<key>", identity={
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
    }, documents=[
        {
            "text": "The refund policy allows customers to return items within 30 days of purchase for a full refund.",
            "metadata": {
                "file_name": "refund_policy.pdf",
                "file_type": "application/pdf",
                "page_number": 1,
            },
        },
        {
            "text": "Premium members receive free shipping on all orders over $50.",
            "metadata": {
                "file_name": "membership_benefits.md",
                "file_type": "text/markdown",
            },
        },
    ])

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

    res = orq.router.audio.transcriptions.create(model="Malibu", enable_logging=True, diarize=False, tag_audio_events=True, timestamps_granularity="word", temperature=0.5, timestamp_granularities=[
        "word",
        "segment",
    ], retry={
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
        "fallbacks": [
            {
                "model": "openai/gpt-4o-mini",
            },
        ],
        "retry": {
            "on_codes": [
                429,
                500,
                502,
                503,
                504,
            ],
        },
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

    res = orq.evals.all(limit=10,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

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

    res = orq.evals.all(limit=10)

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

        res = orq.evals.all(limit=10)

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
        if isinstance(e, models.GetEvalsEvalsResponseBody):
            print(e.data.message)  # str
```

### Error Classes
**Primary error:**
* [`OrqError`](./src/orq_ai_sdk/models/orqerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (42)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`OrqError`](./src/orq_ai_sdk/models/orqerror.py)**:
* [`HonoAPIError`](./src/orq_ai_sdk/models/honoapierror.py): Applicable to 12 of 252 methods.*
* [`InvokeEvalEvalsResponseBody`](./src/orq_ai_sdk/models/invokeevalevalsresponsebody.py): Bad request. Status code `400`. Applicable to 1 of 252 methods.*
* [`PostV2FeedbackFeedbackResponseBody`](./src/orq_ai_sdk/models/postv2feedbackfeedbackresponsebody.py): Bad Request. Status code `400`. Applicable to 1 of 252 methods.*
* [`CreateAgentScheduleSchedulesResponseBody`](./src/orq_ai_sdk/models/createagentscheduleschedulesresponsebody.py): Invalid schedule type, expression, or sub-hour cadence. Status code `400`. Applicable to 1 of 252 methods.*
* [`UpdateAgentScheduleSchedulesResponseBody`](./src/orq_ai_sdk/models/updateagentscheduleschedulesresponsebody.py): Invalid type, expression, or sub-hour cadence. Status code `400`. Applicable to 1 of 252 methods.*
* [`TriggerAgentScheduleSchedulesResponseBody`](./src/orq_ai_sdk/models/triggeragentscheduleschedulesresponsebody.py): Schedule is inactive. Status code `400`. Applicable to 1 of 252 methods.*
* [`GetEvalsEvalsResponseBody`](./src/orq_ai_sdk/models/getevalsevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`CreateEvalEvalsResponseBody`](./src/orq_ai_sdk/models/createevalevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`GetEvalEvalsResponseBody`](./src/orq_ai_sdk/models/getevalevalsresponsebody.py): No evaluator with this id exists in the authenticated workspace, or the request carries no workspace. Status code `404`. Applicable to 1 of 252 methods.*
* [`UpdateEvalEvalsResponseBody`](./src/orq_ai_sdk/models/updateevalevalsresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`DeleteEvalResponseBody`](./src/orq_ai_sdk/models/deleteevalresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`InvokeEvalEvalsResponseResponseBody`](./src/orq_ai_sdk/models/invokeevalevalsresponseresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`GetV2EvaluatorsIDVersionsEvalsResponseBody`](./src/orq_ai_sdk/models/getv2evaluatorsidversionsevalsresponsebody.py): Evaluator not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`DeleteAgentResponseBody`](./src/orq_ai_sdk/models/deleteagentresponsebody.py): Agent not found. The specified agent key does not exist in the workspace or has already been deleted. Status code `404`. Applicable to 1 of 252 methods.*
* [`RetrieveAgentRequestAgentsResponseBody`](./src/orq_ai_sdk/models/retrieveagentrequestagentsresponsebody.py): Agent not found. The specified agent key does not exist in the workspace or you do not have permission to access it. Status code `404`. Applicable to 1 of 252 methods.*
* [`UpdateAgentAgentsResponseBody`](./src/orq_ai_sdk/models/updateagentagentsresponsebody.py): Agent not found. The specified agent key does not exist in the workspace or you do not have permission to modify it. Status code `404`. Applicable to 1 of 252 methods.*
* [`StreamRunAgentAgentsResponseBody`](./src/orq_ai_sdk/models/streamrunagentagentsresponsebody.py): Model not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`StreamAgentAgentsResponseBody`](./src/orq_ai_sdk/models/streamagentagentsresponsebody.py): Agent not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`UpdatePromptResponseBody`](./src/orq_ai_sdk/models/updatepromptresponsebody.py): Prompt not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`DeletePromptResponseBody`](./src/orq_ai_sdk/models/deletepromptresponsebody.py): Prompt not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`GetPromptVersionPromptsResponseBody`](./src/orq_ai_sdk/models/getpromptversionpromptsresponsebody.py): Not Found - The prompt or prompt version does not exist. Status code `404`. Applicable to 1 of 252 methods.*
* [`UpdateToolToolsResponseBody`](./src/orq_ai_sdk/models/updatetooltoolsresponsebody.py): Tool not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`GetV2ToolsToolIDVersionsToolsResponseBody`](./src/orq_ai_sdk/models/getv2toolstoolidversionstoolsresponsebody.py): Tool not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`GetV2ToolsToolIDVersionsVersionIDToolsResponseBody`](./src/orq_ai_sdk/models/getv2toolstoolidversionsversionidtoolsresponsebody.py): Tool or version not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`PostV2FeedbackRemoveFeedbackResponseBody`](./src/orq_ai_sdk/models/postv2feedbackremovefeedbackresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`PostV2FeedbackFeedbackResponseResponseBody`](./src/orq_ai_sdk/models/postv2feedbackfeedbackresponseresponsebody.py): Workspace ID is not found on the request. Status code `404`. Applicable to 1 of 252 methods.*
* [`CreateAgentScheduleSchedulesResponseResponseBody`](./src/orq_ai_sdk/models/createagentscheduleschedulesresponseresponsebody.py): Agent (or agent version, when agent_tag is set) not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`DeleteAgentScheduleResponseBody`](./src/orq_ai_sdk/models/deleteagentscheduleresponsebody.py): Schedule not found, or belongs to a different agent. Status code `404`. Applicable to 1 of 252 methods.*
* [`RetrieveAgentScheduleSchedulesResponseBody`](./src/orq_ai_sdk/models/retrieveagentscheduleschedulesresponsebody.py): Schedule not found, or belongs to a different agent. Status code `404`. Applicable to 1 of 252 methods.*
* [`UpdateAgentScheduleSchedulesResponseResponseBody`](./src/orq_ai_sdk/models/updateagentscheduleschedulesresponseresponsebody.py): Schedule or agent version not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`TriggerAgentScheduleSchedulesResponseResponseBody`](./src/orq_ai_sdk/models/triggeragentscheduleschedulesresponseresponsebody.py): Schedule not found, or belongs to a different agent. Status code `404`. Applicable to 1 of 252 methods.*
* [`RetrieveResponseResponsesResponseBody`](./src/orq_ai_sdk/models/retrieveresponseresponsesresponsebody.py): Response not found. Status code `404`. Applicable to 1 of 252 methods.*
* [`DeleteEvalEvalsResponseBody`](./src/orq_ai_sdk/models/deleteevalevalsresponsebody.py): The evaluator is still referenced as an evaluator or guardrail by one or more deployments. Status code `409`. Applicable to 1 of 252 methods.*
* [`CreateModerationRouterModerationsResponseBody`](./src/orq_ai_sdk/models/createmoderationroutermoderationsresponsebody.py): Returns validation error. Status code `422`. Applicable to 1 of 252 methods.*
* [`CreateTranscriptionRouterAudioTranscriptionsResponseBody`](./src/orq_ai_sdk/models/createtranscriptionrouteraudiotranscriptionsresponsebody.py): Returns validation error. Status code `422`. Applicable to 1 of 252 methods.*
* [`CreateTranslationRouterAudioTranslationsResponseBody`](./src/orq_ai_sdk/models/createtranslationrouteraudiotranslationsresponsebody.py): Returns validation error. Status code `422`. Applicable to 1 of 252 methods.*
* [`InvokeEvalEvalsResponse500ResponseBody`](./src/orq_ai_sdk/models/invokeevalevalsresponse500responsebody.py): Error running the evaluator. Status code `500`. Applicable to 1 of 252 methods.*
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

    res = orq.evals.all(limit=10)

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
