# Skills

## Overview

### Available Operations

* [list](#list) - List all skills
* [create](#create) - Create a new skill
* [import_bundle](#import_bundle) - Import a skill bundle
* [import_from_repository](#import_from_repository) - Import a skill from a repository
* [get](#get) - Retrieve a skill
* [delete](#delete) - Delete a skill
* [update](#update) - Update a skill
* [replace_bundle](#replace_bundle) - Replace a skill bundle
* [put_file](#put_file) - Add or replace a skill file
* [rename_file](#rename_file) - Rename a skill file
* [save_files](#save_files) - Save skill files atomically
* [list_versions](#list_versions) - List skill versions
* [export_bundle](#export_bundle) - Export a skill bundle
* [restore_version](#restore_version) - Restore a skill version
* [delete_file](#delete_file) - Delete a skill file
* [get_file_content](#get_file_content) - Get a presigned URL for a skill file

## list

Returns the skills visible to the current workspace, ordered by creation time with the newest skill first. Use `starting_after` or `ending_before` to page through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillList" method="get" path="/v2/skills" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                     | *Optional[int]*                                                                                             | :heavy_minus_sign:                                                                                          | Page size, 1–200. Unset uses the server default (25). Values outside<br/> the range, including 0, are rejected. |
| `starting_after`                                                                                            | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Cursor for forward pagination. Set to the `skill_id` of the last<br/> item from the previous page.          |
| `ending_before`                                                                                             | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Cursor for backward pagination. Set to the `skill_id` of the first<br/> item from the previous page.        |
| `search`                                                                                                    | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Case-insensitive substring match on display name and description.                                           |
| `project_id`                                                                                                | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Restrict results to one project: its own skills plus the workspace-level skills shared with it.             |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.ListSkillsResponse](../../models/listskillsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a reusable skill in the workspace. Skills store instructions, metadata, and an optional project location so teams can standardize repeatable AI workflows.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillCreate" method="post" path="/v2/skills" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.create(display_name="Josefina_Conn")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                           | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | Workspace-unique display name. Must start with a letter and may contain letters, numbers, dashes, and underscores. Dots are not allowed. |
| `description`                                                                                                                            | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Short human-readable summary of what the skill is for.                                                                                   |
| `tags`                                                                                                                                   | List[*str*]                                                                                                                              | :heavy_minus_sign:                                                                                                                       | Free-form labels for organizing the skill.                                                                                               |
| `path`                                                                                                                                   | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Project path where the skill should be stored.                                                                                           |
| `project_id`                                                                                                                             | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Project that should contain the skill.                                                                                                   |
| `instructions`                                                                                                                           | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Instruction body for the skill. Omit to create metadata first and fill instructions later.                                               |
| `sharing`                                                                                                                                | [Optional[models.Sharing]](../../models/sharing.md)                                                                                      | :heavy_minus_sign:                                                                                                                       | Which projects in the workspace may use this skill. A skill created without a project defaults to every project.                         |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[models.CreateSkillResponse](../../models/createskillresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## import_bundle

Uploads a zip archive containing a SKILL.md file and optional supporting files. Creates a new file-bearing skill. An existing display name returns AlreadyExists. Operating-system archive metadata is ignored: `__MACOSX` entries, AppleDouble sidecars (`._*`), and per-directory metadata such as `.DS_Store`, `Thumbs.db`, and `desktop.ini` are dropped and do not count toward the per-skill file limit.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillImportBundle" method="post" path="/v2/skills/import" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.import_bundle(bundle="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bundle`                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                           | Zip archive containing SKILL.md at the root and optional supporting<br/> files. In JSON requests the bytes are base64 encoded.<br/> Operating-system archive metadata (`__MACOSX`, `._*` AppleDouble<br/> sidecars, `.DS_Store`, `Thumbs.db`, `desktop.ini`) is ignored. |
| `project_id`                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                           | Project that should contain the skill when creating a new skill.<br/> Import creates a new skill; a conflicting name returns AlreadyExists.                                                                                                                  |
| `path`                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                           | Project path where the new skill should be stored.                                                                                                                                                                                                           |
| `sharing`                                                                                                                                                                                                                                                    | [Optional[models.Sharing]](../../models/sharing.md)                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                           | Which projects in the workspace may use this skill. A skill imported without a project defaults to every project.                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                          |

### Response

**[models.ImportSkillBundleResponse](../../models/importskillbundleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## import_from_repository

Creates an editable skill snapshot from a repository directory using a workspace source control connection. The source commit is retained; subsequent repository changes are not synchronized.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillImportFromRepository" method="post" path="/v2/skills/import/repository" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.import_from_repository()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `connection_id`                                                                                                   | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `repository_url`                                                                                                  | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `ref`                                                                                                             | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `subdirectory`                                                                                                    | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `project_id`                                                                                                      | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `path`                                                                                                            | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `sharing`                                                                                                         | [Optional[models.Sharing]](../../models/sharing.md)                                                               | :heavy_minus_sign:                                                                                                | Which projects in the workspace may use this skill. A skill imported without a project defaults to every project. |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.ImportSkillFromRepositoryResponse](../../models/importskillfromrepositoryresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves an existing skill by skill ID. Display names are also accepted for compatibility because they are unique within a workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillGet" method="get" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.get(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                                             | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | Accepts either the skill's ID (e.g. "skill_01H...") or its display<br/> name. Display names are unique within a workspace. |
| `factory_id`                                                                                                           | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Resolve the skill as one factory sees it: the skills of its project plus the workspace-level skills shared with it.    |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[models.GetSkillResponse](../../models/getskillresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401, 404               | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes a skill from the workspace. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillDelete" method="delete" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
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

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates mutable skill fields. Omitted fields keep their current values. When `tags` is provided it replaces the existing tags; send an empty array to clear them.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillUpdate" method="patch" path="/v2/skills/{skill_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.update(skill_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                                                                   | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Skill ID to update.                                                                                                                          |
| `display_name`                                                                                                                               | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | New workspace-unique display name. Must start with a letter and may contain letters, numbers, dashes, and underscores. Dots are not allowed. |
| `description`                                                                                                                                | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | New description. Omit to keep the current description.                                                                                       |
| `tags`                                                                                                                                       | List[*str*]                                                                                                                                  | :heavy_minus_sign:                                                                                                                           | Replacement tag list. When provided, replaces the current tags; send an empty array to clear them.                                           |
| `path`                                                                                                                                       | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | New project path. Omit to keep the current path.                                                                                             |
| `instructions`                                                                                                                               | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | New instruction body. Omit to keep the current instructions.                                                                                 |
| `project_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | New containing project. Omit to keep the current project.                                                                                    |
| `sharing`                                                                                                                                    | [Optional[models.Sharing]](../../models/sharing.md)                                                                                          | :heavy_minus_sign:                                                                                                                           | Which projects in the workspace may use this skill.                                                                                          |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |

### Response

**[models.UpdateSkillResponse](../../models/updateskillresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## replace_bundle

Replace a skill bundle

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillReplaceBundle" method="put" path="/v2/skills/{skill_id}/bundle" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.replace_bundle(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `bundle`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReplaceSkillBundleResponse](../../models/replaceskillbundleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## put_file

Uploads a single file to a skill's bundle. If the path already exists the file is replaced; otherwise it is added to the manifest.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillPutFile" method="put" path="/v2/skills/{skill_id}/files" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.put_file(skill_id="<id>", path="/usr/libexec", content="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `skill_id`                                                                                             | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Skill ID or display name to update.                                                                    |
| `path`                                                                                                 | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Relative path within the skill bundle, including subdirectory<br/> components (e.g. "scripts/extract.py"). |
| `content`                                                                                              | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Raw file content. The MIME type is derived from the path extension.                                    |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[models.PutSkillFileResponse](../../models/putskillfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## rename_file

Changes a file's path within a skill's bundle. The file content is unchanged. SKILL.md cannot be renamed.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillRenameFile" method="post" path="/v2/skills/{skill_id}/files/rename" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.rename_file(skill_id="<id>", old_path="<value>", new_path="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `skill_id`                                                                                                                  | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Skill ID or display name to update.                                                                                         |
| `old_path`                                                                                                                  | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Current relative path of the file within the skill bundle.                                                                  |
| `new_path`                                                                                                                  | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | New relative path for the file within the skill bundle, including any<br/> subdirectory components (e.g. "scripts/extract.py"). |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.RenameSkillFileResponse](../../models/renameskillfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## save_files

Saves file drafts and optional skill metadata as one version.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillSaveFiles" method="post" path="/v2/skills/{skill_id}/files:save" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.save_files(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `files`                                                             | List[[models.SkillFileWrite](../../models/skillfilewrite.md)]       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `instructions`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SaveSkillFilesResponse](../../models/saveskillfilesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_versions

List skill versions

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillListVersions" method="get" path="/v2/skills/{skill_id}/versions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.list_versions(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSkillVersionsResponse](../../models/listskillversionsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## export_bundle

Downloads the skill as a zip archive containing the SKILL.md file and all files in the manifest. Basic Skills receive a synthesized SKILL.md.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillExportBundle" method="get" path="/v2/skills/{skill_id}:export" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.export_bundle(skill_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Skill ID or display name to export.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ExportSkillBundleResponse](../../models/exportskillbundleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## restore_version

Restores a skill to a previous version recorded in the activity log. The restored state becomes a new version.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillRestoreVersion" method="post" path="/v2/skills/{skill_id}:restore" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.restore_version(skill_id="<id>", version_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `skill_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Skill ID or display name to restore.                                |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Version ID (activity ID) to restore to.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RestoreSkillVersionResponse](../../models/restoreskillversionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_file

Removes a file from a skill's bundle by its relative path. SKILL.md cannot be deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillDeleteFile" method="delete" path="/v2/skills/{skill_id}/files/{path}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.delete_file(skill_id="<id>", path="/usr/include")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `skill_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Skill ID or display name to update.                                                              |
| `path`                                                                                           | *str*                                                                                            | :heavy_check_mark:                                                                               | Relative path of the file to delete within the skill bundle (for example `references/guide.md`). |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.DeleteSkillFileResponse](../../models/deleteskillfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_file_content

Returns a time-limited presigned URL that can be used to download the raw content of a file in the skill bundle.

### Example Usage

<!-- UsageSnippet language="python" operationID="SkillGetFileContent" method="get" path="/v2/skills/{skill_id}/files/{path}:presign" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.skills.get_file_content(skill_id="<id>", path="/usr/src")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `skill_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Skill ID or display name.                                                              |
| `path`                                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | Relative path of the file within the skill bundle (for example `references/guide.md`). |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[models.GetSkillFileContentResponse](../../models/getskillfilecontentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |