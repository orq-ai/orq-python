# WorkspaceSecurity

## Overview

### Available Operations

* [list_domains](#list_domains) - List verified domains
* [create_domain](#create_domain) - Add a domain
* [delete_domain](#delete_domain) - Delete a domain
* [verify_domain](#verify_domain) - Verify a domain
* [get_ip_allowlist](#get_ip_allowlist) - Retrieve the IP allowlist
* [update_ip_allowlist](#update_ip_allowlist) - Enable or disable the IP allowlist
* [add_ip_range](#add_ip_range) - Add an IP range
* [delete_ip_range](#delete_ip_range) - Delete an IP range

## list_domains

Lists domain-verification records for the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityListDomains" method="get" path="/v2/{workspace_key}/domains" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.list_domains(workspace_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDomainsResponse](../../models/listdomainsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_domain

Creates a domain-verification challenge and returns the TXT record to add to DNS.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityCreateDomain" method="post" path="/v2/{workspace_key}/domains" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.create_domain(workspace_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `domain`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateDomainResponse](../../models/createdomainresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_domain

Permanently removes a domain-verification record.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityDeleteDomain" method="delete" path="/v2/{workspace_key}/domains/{domain_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.workspace_security.delete_domain(workspace_key="<value>", domain_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `domain_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## verify_domain

Checks DNS for the expected TXT record and marks the domain as verified when it matches.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityVerifyDomain" method="post" path="/v2/{workspace_key}/domains/{domain_id}/verify" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.verify_domain(workspace_key="<value>", domain_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `domain_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerifyDomainResponse](../../models/verifydomainresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_ip_allowlist

Returns the workspace IP allowlist and the current caller IP when available.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityGetIPAllowlist" method="get" path="/v2/{workspace_key}/ip-allowlist" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.get_ip_allowlist(workspace_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetIPAllowlistResponse](../../models/getipallowlistresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_ip_allowlist

Updates the workspace-level allowlist switch. Every listed range applies while the allowlist is enabled.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityUpdateIPAllowlist" method="patch" path="/v2/{workspace_key}/ip-allowlist" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.update_ip_allowlist(workspace_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateIPAllowlistResponse](../../models/updateipallowlistresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## add_ip_range

Adds an IPv4 or IPv6 CIDR range to the workspace allowlist.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityAddIPRange" method="post" path="/v2/{workspace_key}/ip-allowlist/entries" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_security.add_ip_range(workspace_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `cidr`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddIPRangeResponse](../../models/addiprangeresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_ip_range

Permanently removes a CIDR range from the workspace allowlist.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSecurityDeleteIPRange" method="delete" path="/v2/{workspace_key}/ip-allowlist/entries/{range_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.workspace_security.delete_ip_range(workspace_key="<value>", range_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_key`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `range_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |