# Skills

## Overview

### Available Operations

* [list](#list) - List all skills
* [create](#create) - Create a new skill
* [get](#get) - Retrieve a skill
* [delete](#delete) - Delete a skill
* [update](#update) - Update a skill

## list

Returns the skills visible to the current workspace, ordered by creation time with the newest skill first. Use `starting_after` or `ending_before` to page through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillList" method="get" path="/v2/skills" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.skills.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `limit`                                                                                                                        | *Optional[int]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Page size, 1–200. Unset uses the server default (25); explicit 0<br/> (or anything outside the range) is rejected by buf.validate. |
| `starting_after`                                                                                                               | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Cursor for forward pagination. Set to the `skill_id` of the last<br/> item from the previous page.                             |
| `ending_before`                                                                                                                | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Cursor for backward pagination. Set to the `skill_id` of the first<br/> item from the previous page.                           |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.ListSkillsResponse](../../models/listskillsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a reusable skill in the workspace. Skills store instructions, metadata, and an optional project location so teams can standardize repeatable AI workflows.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillCreate" method="post" path="/v2/skills" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.skills.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                              | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Workspace-unique display name. Must start with a letter and may contain letters, numbers, and underscores. Dashes and dots are not allowed. |
| `description`                                                                                                                               | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Short human-readable summary of what the skill is for.                                                                                      |
| `tags`                                                                                                                                      | List[*str*]                                                                                                                                 | :heavy_minus_sign:                                                                                                                          | Free-form labels for organizing the skill.                                                                                                  |
| `path`                                                                                                                                      | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Project path where the skill should be stored.                                                                                              |
| `project_id`                                                                                                                                | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Project that should contain the skill.                                                                                                      |
| `instructions`                                                                                                                              | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Instruction body for the skill. Omit to create metadata first and fill instructions later.                                                  |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.CreateSkillResponse](../../models/createskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves an existing skill by skill ID. Display names are also accepted for compatibility because they are unique within a workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillGet" method="get" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.skills.get(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                                             | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | Accepts either the skill's ID (e.g. "skill_01H...") or its display<br/> name. Display names are unique within a workspace. |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[models.GetSkillResponse](../../models/getskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a skill from the workspace. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillDelete" method="delete" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.skills.delete(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Skill ID to delete.                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSkillResponse](../../models/deleteskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates mutable skill fields. Omitted optional fields keep their current values. Repeated fields such as `tags` replace the existing collection when provided.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillUpdate" method="patch" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.skills.update(skill_id_param="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `skill_id_param`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | Skill ID to update.                                                                                                                                                                                                                        |
| `skill_id`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | Skill ID to update.                                                                                                                                                                                                                        |
| `display_name`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | New workspace-unique display name. Omit to keep the current name.<br/> Must start with a letter and may contain letters, numbers, and<br/> underscores. Dashes and dots are not allowed because skill names<br/> are referenced as template variables. |
| `description`                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | New description. Omit to keep the current description.                                                                                                                                                                                     |
| `tags`                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                         | Replacement tag list. Leave empty to clear tags.                                                                                                                                                                                           |
| `path`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | New project path. Omit to keep the current path.                                                                                                                                                                                           |
| `instructions`                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | New instruction body. Omit to keep the current instructions.                                                                                                                                                                               |
| `project_id`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                         | New containing project. Omit to keep the current project.                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                        |

### Response

**[models.UpdateSkillResponse](../../models/updateskillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |