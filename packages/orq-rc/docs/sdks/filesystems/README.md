# FileSystems

## Overview

### Available Operations

* [list](#list) - List file systems
* [create](#create) - Create file system
* [retrieve](#retrieve) - Retrieve file system
* [delete](#delete) - Delete file system
* [update](#update) - Update file system
* [list_files](#list_files) - List files
* [delete_file](#delete_file) - Delete file
* [move_file](#move_file) - Move file
* [stat_file](#stat_file) - Stat file
* [create_folder](#create_folder) - Create folder

## list

Retrieves a paginated list of file systems in the workspace. Use cursor-based pagination parameters to navigate through the results.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListFileSystems" method="get" path="/v2/file-systems" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFileSystemsResponse](../../models/listfilesystemsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a file system. Storage is provisioned lazily on first use by an agent run or MCP client.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateFileSystem" method="post" path="/v2/file-systems" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.create(key="<key>", path="/etc/ppp")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                                            | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | The unique key of the file system. The key is unique and immutable and cannot be repeated within the same workspace.                                             |
| `path`                                                                                                                                                           | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Entity storage path. With workspace-level API keys, the first element identifies the project. With project-level API keys, the path is relative to that project. |
| `display_name`                                                                                                                                                   | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Human readable name shown in the UI. Defaults to the key.                                                                                                        |
| `description`                                                                                                                                                    | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |
| `external_access`                                                                                                                                                | [Optional[models.ExternalAccess]](../../models/externalaccess.md)                                                                                                | :heavy_minus_sign:                                                                                                                                               | Whether external MCP clients may reach this file system. Defaults to disabled.                                                                                   |
| `sharing`                                                                                                                                                        | [Optional[models.Sharing]](../../models/sharing.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                               | Sharing controls which projects in the workspace may use this entity and<br/> what they may do with it.                                                          |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[models.FileSystem](../../models/filesystem.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves detailed information about a specific file system, including its quota and external access configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveFileSystem" method="get" path="/v2/file-systems/{file_system_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.retrieve(file_system_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileSystem](../../models/filesystem.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a file system and every file stored in it. This cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteFileSystem" method="delete" path="/v2/file-systems/{file_system_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.delete(file_system_key="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteFileSystemResponse](../../models/deletefilesystemresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates the mutable file system configuration. The key is immutable.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateFileSystem" method="patch" path="/v2/file-systems/{file_system_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.update(file_system_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `file_system_key`                                                                                                                       | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | N/A                                                                                                                                     |
| `display_name`                                                                                                                          | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Update has no key to fall back on, so an explicitly supplied display_name<br/> may not be empty; Create defaults an omitted one to the key. |
| `description`                                                                                                                           | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | N/A                                                                                                                                     |
| `path`                                                                                                                                  | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | N/A                                                                                                                                     |
| `external_access`                                                                                                                       | [Optional[models.UpdateFileSystemRequestExternalAccess]](../../models/updatefilesystemrequestexternalaccess.md)                         | :heavy_minus_sign:                                                                                                                      | N/A                                                                                                                                     |
| `sharing`                                                                                                                               | [Optional[models.Sharing]](../../models/sharing.md)                                                                                     | :heavy_minus_sign:                                                                                                                      | Sharing controls which projects in the workspace may use this entity and<br/> what they may do with it.                                 |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.FileSystem](../../models/filesystem.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_files

Lists the files and folders stored in a file system. An empty path lists the file system root.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListFiles" method="get" path="/v2/file-systems/{file_system_key}/files" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.list_files(file_system_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `depth`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_entries`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListFileSystemFilesResponse](../../models/listfilesystemfilesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_file

Deletes one file or folder. A folder that still has content is refused unless recursive is set.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteFile" method="delete" path="/v2/file-systems/{file_system_key}/files" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.delete_file(file_system_key="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `recursive`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteFileSystemFileResponse](../../models/deletefilesystemfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## move_file

Moves or renames one file or folder within the same file system. Missing destination folders are created.

### Example Usage

<!-- UsageSnippet language="python" operationID="MoveFile" method="post" path="/v2/file-systems/{file_system_key}/files/move" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.move_file(file_system_key="<value>", from_="<value>", to="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `file_system_key`                                                    | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `from_`                                                              | *str*                                                                | :heavy_check_mark:                                                   | Current path of the file or folder, relative to the file system root |
| `to`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | New path of the file or folder, relative to the file system root     |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.MoveFileSystemFileResponse](../../models/movefilesystemfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## stat_file

Retrieves the metadata of one file or folder without transferring its content.

### Example Usage

<!-- UsageSnippet language="python" operationID="StatFile" method="get" path="/v2/file-systems/{file_system_key}/files/stat" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.stat_file(file_system_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StatFileSystemFileResponse](../../models/statfilesystemfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_folder

Creates a folder and every missing parent. Succeeds on a folder that already exists.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateFolder" method="post" path="/v2/file-systems/{file_system_key}/folders" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.file_systems.create_folder(file_system_key="<value>", path="/boot/defaults")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_system_key`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Folder to create, relative to the file system root                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateFileSystemFolderResponse](../../models/createfilesystemfolderresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |