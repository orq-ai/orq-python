# AuditLogDestinations

## Overview

### Available Operations

* [list](#list) - List audit log destinations
* [create](#create) - Create an audit log destination
* [get](#get) - Retrieve an audit log destination
* [delete](#delete) - Delete an audit log destination
* [update](#update) - Update an audit log destination
* [list_deliveries](#list_deliveries) - List deliveries
* [replay](#replay) - Replay audit events
* [rotate_secret](#rotate_secret) - Rotate the signing secret
* [test](#test) - Send a test event

## list

Returns the audit log destinations of the workspace, newest first, with cursor pagination.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationList" method="get" path="/v3/audit-log-destinations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAuditLogDestinationsResponse](../../models/listauditlogdestinationsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a signed webhook destination that receives every audit log event recorded in the workspace from this point on. The signing secret is returned once in this response and never again.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationCreate" method="post" path="/v3/audit-log-destinations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.create(display_name="Leonie73", url="https://lighthearted-overheard.org")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `display_name`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | Required. Human-readable destination name, unique within the workspace.    |
| `url`                                                                      | *str*                                                                      | :heavy_check_mark:                                                         | Required. Absolute HTTPS URL. Private and loopback addresses are rejected. |
| `description`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Optional. Description of the receiving system.                             |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.CreateAuditLogDestinationResponse](../../models/createauditlogdestinationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves an audit log destination by ID. The signing secret is never returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationGet" method="get" path="/v3/audit-log-destinations/{destination_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.get(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `destination_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAuditLogDestinationResponse](../../models/getauditlogdestinationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes a destination and cancels its pending deliveries.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationDelete" method="delete" path="/v3/audit-log-destinations/{destination_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.delete(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `destination_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAuditLogDestinationResponse](../../models/deleteauditlogdestinationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates a destination. Set `status` to `AUDIT_LOG_DESTINATION_STATUS_PAUSED` to stop deliveries while retaining the backlog, and back to `AUDIT_LOG_DESTINATION_STATUS_ACTIVE` to drain it. The URL can only change while the destination is paused.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationUpdate" method="patch" path="/v3/audit-log-destinations/{destination_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.update(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `destination_id`                                                                        | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `display_name`                                                                          | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional. New destination name.                                                         |
| `description`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional. New description. An empty string clears it.                                   |
| `url`                                                                                   | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Optional. New HTTPS endpoint. Accepted only while the destination is paused.            |
| `status`                                                                                | [Optional[models.AuditLogDestinationStatus]](../../models/auditlogdestinationstatus.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.UpdateAuditLogDestinationResponse](../../models/updateauditlogdestinationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_deliveries

Returns the delivery history of a destination, newest first, optionally filtered by status.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationListDeliveries" method="get" path="/v3/audit-log-destinations/{destination_id}/deliveries" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.list_deliveries(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `destination_id`                                                              | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `starting_after`                                                              | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `ending_before`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `status`                                                                      | List[[models.AuditLogDeliveryStatus](../../models/auditlogdeliverystatus.md)] | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListAuditLogDeliveriesResponse](../../models/listauditlogdeliveriesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## replay

Queues a new delivery for every retained audit event recorded in the time window, up to 10,000 events per request. Replays keep the original event IDs and never extend event retention.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationReplay" method="post" path="/v3/audit-log-destinations/{destination_id}/replay" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.replay(destination_id="<id>", from_=parse_datetime("2025-10-22T02:10:16.524Z"), to=parse_datetime("2024-07-11T11:51:53.939Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `destination_id`                                                              | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `from_`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_check_mark:                                                            | Required. Start of the window (inclusive).                                    |
| `to`                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_check_mark:                                                            | Required. End of the window (exclusive). The window may span at most 31 days. |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ReplayAuditLogDeliveriesResponse](../../models/replayauditlogdeliveriesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## rotate_secret

Generates a new signing secret for the destination. Deliveries attempted after the rotation are signed with the new secret. The new secret is returned once in this response and never again.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationRotateSecret" method="post" path="/v3/audit-log-destinations/{destination_id}/rotate-secret" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.rotate_secret(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `destination_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotateAuditLogDestinationSecretResponse](../../models/rotateauditlogdestinationsecretresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## test

Sends a signed synthetic `audit_log.test` event to the destination synchronously and returns the receiver outcome. Test deliveries appear in the delivery history.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogDestinationTest" method="post" path="/v3/audit-log-destinations/{destination_id}/test" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.audit_log_destinations.test(destination_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `destination_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestAuditLogDestinationResponse](../../models/testauditlogdestinationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |