# Projects

## Overview

### Available Operations

* [list](#list) - List all projects
* [create](#create) - Create a new project
* [get](#get) - Retrieve a project
* [delete](#delete) - Delete a project
* [update](#update) - Update a project

## list

Returns projects visible to the current workspace, ordered by creation time with the newest project first. Use `starting_after` or `ending_before` to page through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="ProjectList" method="get" path="/v2/projects" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.projects.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `limit`                                                                                            | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Page size, 1-200. Unset uses the server default.                                                   |
| `starting_after`                                                                                   | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Cursor for forward pagination. Set to the `project_id` of the last<br/> item from the previous page. |
| `ending_before`                                                                                    | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Cursor for backward pagination. Set to the `project_id` of the first<br/> item from the previous page. |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.ListProjectsResponse](../../models/listprojectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a project in the current workspace. Projects are workspace-level containers for resources such as skills, deployments, datasets, rules, and related team access.

### Example Usage

<!-- UsageSnippet language="python" operationID="ProjectCreate" method="post" path="/v2/projects" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.projects.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Project name. Names must be non-empty and at most 128 characters.   |
| `teams`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | Team identifiers to associate with the project.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateProjectResponse](../../models/createprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the details of an existing project by its unique project ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="ProjectGet" method="get" path="/v2/projects/{project_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.projects.get(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID to retrieve.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProjectResponse](../../models/getprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a project from the workspace. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="ProjectDelete" method="delete" path="/v2/projects/{project_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.projects.delete(project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Project ID to delete.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteProjectResponse](../../models/deleteprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates the specified project by setting the values of the parameters passed.

### Example Usage

<!-- UsageSnippet language="python" operationID="ProjectUpdate" method="patch" path="/v2/projects/{project_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.projects.update(project_id_param="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `project_id_param`                                                                                              | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Project ID to update.                                                                                           |
| `project_id`                                                                                                    | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Project ID to update.                                                                                           |
| `name`                                                                                                          | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | New project name. Omit to keep the current name.                                                                |
| `teams`                                                                                                         | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | Replacement list of team identifiers associated with the project.<br/> Leave empty to remove all team associations. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.UpdateProjectResponse](../../models/updateprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |