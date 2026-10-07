# Websearch

## Overview

### Available Operations

* [search](#search) - Search the web with a selected provider

## search

Search with Exa, Ceramic, Linkup, Tavily, Serper, OpenAI, or Perplexity and return page URLs, titles, and descriptions in one response format. Authenticate with an API key that grants **websearch.execute** and send **Content-Type: application/json**.

### Provider and credentials

Each request uses the selected provider. Exa uses **auto** search, Linkup uses **standard** depth, Tavily uses **basic** depth, and Perplexity uses its standard Search API. OpenAI runs one forced **web_search** tool call on gpt-5.6-luna through the Responses API and returns the raw search results.

Credentials are selected from the authenticated workspace. A configured provider integration takes precedence over ORQ-managed credentials: the default integration is used, or the first configured integration if no default is set. Configure BYOK in the workspace integrations settings. Invalid integration credentials cause an error.

### Billing

Managed searches use the same credits as the **AI Gateway** and charge the provider cost plus **US$0.001 per search** (US$1 per 1,000 searches). BYOK searches consume no ORQ credits and add no ORQ markup; the provider bills the integration owner directly.

Exa's published auto rate is **US$7 per 1,000 requests** for up to 10 results, or **US$8 per 1,000** including the ORQ markup. Exa charges use the actual cost reported by the provider.

Perplexity's published Search API rate is **US$5 per 1,000 requests**. OpenAI web search costs **US$10 per 1,000 tool calls** plus the gpt-5.6-luna tokens of the Responses call, computed from the usage reported by OpenAI, so each search is typically US$0.012 to US$0.015 before the ORQ markup.

A successful managed search is billable even if an output guardrail or output redaction failure prevents the results from being returned.

### Policies and observability

PII Redaction is the only supported request plugin. Workspace PII settings and matching guardrail rules also apply. Query redaction runs before input guardrails and the provider call; result redaction runs before output guardrails and the response.

Search spans and metrics record the provider, latency, result count, and cost. Use the **x-orq-trace-id** response header to find the trace.

### Example Usage: basic

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="basic" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="exa", query="Things to do in Salt Lake City in fall", limit=10)

    # Handle response
    print(res)

```
### Example Usage: customer_search

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="customer_search" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="exa", query="Things to do in Salt Lake City in fall", identity={
        "id": "customer-123",
    }, limit=10)

    # Handle response
    print(res)

```
### Example Usage: insufficient_credits

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="insufficient_credits" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="tavily", query="<value>", limit=10)

    # Handle response
    print(res)

```
### Example Usage: invalid_request

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="invalid_request" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="tavily", query="<value>", limit=10)

    # Handle response
    print(res)

```
### Example Usage: no_results

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="no_results" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="tavily", query="<value>", limit=10)

    # Handle response
    print(res)

```
### Example Usage: pii_redaction

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="pii_redaction" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="exa", query="Travel advice for john.smith@example.com", limit=5, plugins=[
        {
            "id": "pii_redaction",
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: results

<!-- UsageSnippet language="python" operationID="search-web" method="post" path="/v3/websearch" example="results" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.websearch.search(provider="tavily", query="<value>", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `provider`                                                                                                                                                                                                                     | [models.Provider](../../models/provider.md)                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                             | Provider to run this search. Exa uses auto, Linkup uses standard depth, Tavily uses basic depth, and OpenAI runs one web_search tool call on gpt-5.6-luna. Workspace credentials are selected automatically for this provider. |
| `query`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | Search text. Must not be blank or exceed 10,000 characters. Ceramic accepts at most 50 words.                                                                                                                                  |
| `identity`                                                                                                                                                                                                                     | [Optional[models.SearchWebIdentity]](../../models/searchwebidentity.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                             | Customer or end-user identity for attributing this search and its usage.                                                                                                                                                       |
| `limit`                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                             | Maximum number of results to return, from 1 to 10. Defaults to 10. The provider may return fewer results.                                                                                                                      |
| `plugins`                                                                                                                                                                                                                      | List[[models.SearchWebPlugins](../../models/searchwebplugins.md)]                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                             | Optional PII Redaction configuration. At most one plugin is accepted, with id pii_redaction. Workspace and matching rule requirements still apply when this field is omitted.                                                  |
| `retries`                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                            |

### Response

**[models.SearchWebResponse](../../models/searchwebresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.SearchWebWebsearchResponseBody            | 400                                              | application/json                                 |
| models.SearchWebWebsearchResponseResponseBody    | 401                                              | application/json                                 |
| models.SearchWebWebsearchResponse402ResponseBody | 402                                              | application/json                                 |
| models.SearchWebWebsearchResponse403ResponseBody | 403                                              | application/json                                 |
| models.SearchWebWebsearchResponse415ResponseBody | 415                                              | application/json                                 |
| models.SearchWebWebsearchResponse422ResponseBody | 422                                              | application/json                                 |
| models.SearchWebWebsearchResponse429ResponseBody | 429                                              | application/json                                 |
| models.SearchWebWebsearchResponse500ResponseBody | 500                                              | application/json                                 |
| models.SearchWebWebsearchResponse502ResponseBody | 502                                              | application/json                                 |
| models.SearchWebWebsearchResponse503ResponseBody | 503                                              | application/json                                 |
| models.SearchWebWebsearchResponse504ResponseBody | 504                                              | application/json                                 |
| models.APIDefaultError                           | 4XX, 5XX                                         | \*/\*                                            |