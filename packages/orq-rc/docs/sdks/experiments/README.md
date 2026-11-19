# Experiments

## Overview

### Available Operations

* [list](#list) - List experiments
* [create](#create) - Create an experiment
* [get](#get) - Get an experiment
* [delete](#delete) - Delete an experiment
* [update](#update) - Update an experiment
* [list_runs](#list_runs) - List runs
* [create_run](#create_run) - Create a run
* [get_run](#get_run) - Get a run
* [delete_run](#delete_run) - Delete a run
* [update_run](#update_run) - Update a run
* [list_annotations](#list_annotations) - List annotation columns
* [create_annotation](#create_annotation) - Add an annotation column
* [delete_annotation](#delete_annotation) - Remove an annotation column
* [update_annotation](#update_annotation) - Update annotation column metadata
* [patch_annotation_cell](#patch_annotation_cell) - Set an annotation cell
* [cancel_run](#cancel_run) - Cancel a run
* [update_run_column_layout](#update_run_column_layout) - Update column layout
* [list_evals](#list_evals) - List eval columns
* [create_eval](#create_eval) - Add an eval column
* [delete_eval](#delete_eval) - Remove an eval column
* [execute_run](#execute_run) - Execute a run
* [get_run_metrics](#get_run_metrics) - Get run metrics
* [query_run](#query_run) - Query run cells
* [delete_rows](#delete_rows) - Delete rows
* [duplicate_row](#duplicate_row) - Duplicate a row
* [list_tasks](#list_tasks) - List task columns
* [create_task](#create_task) - Add a task column
* [delete_task](#delete_task) - Delete a task column
* [update_task](#update_task) - Update a task column
* [export_run](#export_run) - Export a run

## list

Lists experiments in the workspace, newest first.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentList" method="get" path="/v3/experiments" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `limit`                                                                                               | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Page size, 1 to 200. Defaults to 25.                                                                  |
| `starting_after`                                                                                      | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Cursor for forward pagination. Set to the `experiment_id` of the last item<br/> from the previous page. |
| `ending_before`                                                                                       | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Cursor for backward pagination. Set to the `experiment_id` of the first<br/> item from the previous page. |
| `project_id`                                                                                          | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Restrict results to one project. Omit to list every project the caller<br/> can access.               |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ListExperimentsResponse](../../models/listexperimentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates an experiment and its first run, a draft named Run 1. When dataset_id is set, the run gets one row per datapoint, up to 1000. project_id defaults to the caller's project and is required for API keys that span several projects.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentCreate" method="post" path="/v3/experiments" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create(display_name="Dorothea_Quigley28")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                               | Type                                                                                                                                                                                                    | Required                                                                                                                                                                                                | Description                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                                                                                          | *str*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | Experiment name, 1 to 255 characters.                                                                                                                                                                   |
| `project_id`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                      | Project the experiment is created in. Defaults to the caller's project:<br/> the API key's project, or the project open in the AI Studio. Required for<br/> API keys that span several projects.        |
| `dataset_id`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                      | Dataset whose datapoints become the rows of the first run, at most 1000.<br/> Must be in the experiment's project. Omit to start with an empty run.                                                     |
| `source_run`                                                                                                                                                                                            | [Optional[models.RunRef]](../../models/runref.md)                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                      | Run to fork. Its task, metric, evaluator and annotation columns are copied<br/> into the new experiment's first run; rows still come from `dataset_id`.<br/> Must be in the same project as the new experiment. |
| `retries`                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                     |

### Response

**[models.Experiment](../../models/experiment.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Returns experiment metadata. Runs and cell data are separate resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentGet" method="get" path="/v3/experiments/{experiment_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.get(experiment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Experiment](../../models/experiment.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes an experiment with all its runs, rows and cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentDelete" method="delete" path="/v3/experiments/{experiment_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete(experiment_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates experiment metadata. Omitted optional fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentUpdate" method="patch" path="/v3/experiments/{experiment_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update(experiment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                                               | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the experiment.                                                                                                                         |
| `display_name`                                                                                                                                | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | New experiment name, 1 to 255 characters.                                                                                                     |
| `selected_run_id`                                                                                                                             | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Run to show by default. Must be a run of this experiment.                                                                                     |
| `row_height_level`                                                                                                                            | *Optional[int]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Row height in the AI Studio grid: 1 (compact), 2 or 3 (tallest).                                                                              |
| `project_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Moves the experiment to another project the caller can access. The<br/> dataset stays where it is, so new runs need a dataset in the new project. |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.Experiment](../../models/experiment.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_runs

Lists runs for an experiment, newest first. Each run is metadata only.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunList" method="get" path="/v3/experiments/{experiment_id}/runs" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list_runs(experiment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                | *str*                                                                                          | :heavy_check_mark:                                                                             | ID of the experiment.                                                                          |
| `limit`                                                                                        | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | Page size, 1 to 200. Defaults to 25.                                                           |
| `starting_after`                                                                               | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for forward pagination. Set to the `run_id` of the last item from<br/> the previous page. |
| `ending_before`                                                                                | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for backward pagination. Set to the `run_id` of the first item from<br/> the previous page. |
| `include_metrics`                                                                              | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Include each run's average evaluator results in `metrics`.                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.ListExperimentRunsResponse](../../models/listexperimentrunsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_run

Creates a new run, copying columns from the selected run when present. A new run starts with empty output cells; executing cells on an existing run does not create one.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunCreate" method="post" path="/v3/experiments/{experiment_id}/runs" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_run(experiment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `experiment_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | ID of the experiment.                                                     |
| `key`                                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Run name. Defaults to `Run ` plus the last four characters of the run ID. |
| `settings`                                                                | [Optional[models.RunSettings]](../../models/runsettings.md)               | :heavy_minus_sign:                                                        | Execution settings. Concurrency defaults to 10.                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_run

Returns run status, per-cell status counts, row count, and column configs. Does not return the cell matrix.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunGet" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.get_run(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_run

Deletes a run and its cell data. The last run of an experiment cannot be deleted. Distinct from cancel, which keeps completed cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunDelete" method="delete" path="/v3/experiments/{experiment_id}/runs/{run_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_run(experiment_id="<id>", run_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_run

Updates run key and execution settings. Does not execute the run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_run(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                                                | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | ID of the experiment.                                                                                                                          |
| `run_id`                                                                                                                                       | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | ID of the run.                                                                                                                                 |
| `key`                                                                                                                                          | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | New run name. Must not be empty.                                                                                                               |
| `settings`                                                                                                                                     | [Optional[models.RunSettings]](../../models/runsettings.md)                                                                                    | :heavy_minus_sign:                                                                                                                             | Settings to change. `concurrency`, `timeout` and `max_turns` change only<br/> when set. `hidden_column_ids` is replaced, and cleared when omitted. |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_annotations

Lists the annotation columns of a run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentAnnotationList" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/annotations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list_annotations(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAnnotationColumnsResponse](../../models/listannotationcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_annotation

Adds an annotation column. Each row gets one annotation cell per task column.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentAnnotationCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/annotations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_annotation(experiment_id="<id>", run_id="<id>", annotation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `experiment_id`                                                                                                                | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | ID of the experiment.                                                                                                          |
| `run_id`                                                                                                                       | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | ID of the run.                                                                                                                 |
| `annotation_id`                                                                                                                | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | ID of the annotation definition. Each row gets one annotation cell per task<br/> column.                                       |
| `display_name`                                                                                                                 | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Column name. Defaults to `annotation_id`.                                                                                      |
| `annotation_type`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Value type the annotation accepts: `range`, `single_select`, `multi_select`, `text` or `correction`. Empty accepts<br/> any value. |
| `position`                                                                                                                     | *Optional[int]*                                                                                                                | :heavy_minus_sign:                                                                                                             | 0-based position among the run's columns. Defaults to the end.                                                                 |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_annotation

Removes an annotation column and all its cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentAnnotationDelete" method="delete" path="/v3/experiments/{experiment_id}/runs/{run_id}/annotations/{annotation_column_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_annotation(experiment_id="<id>", run_id="<id>", annotation_column_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `annotation_column_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | ID of the annotation column.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_annotation

Updates display fields on the column. The human-eval definition is updated at source.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentAnnotationUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/annotations/{annotation_column_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_annotation(experiment_id="<id>", run_id="<id>", annotation_column_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `annotation_column_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | ID of the annotation column.                                        |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New column name. Must not be empty.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_annotation_cell

Writes the annotation value of one row for one task column. An annotation column holds one cell per task column, so task_id selects which response is being annotated. The task output of that row must be completed. The value must match the annotation type, and a running cell cannot be changed.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentAnnotationCellPatch" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/annotations/{annotation_column_id}/cells/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.patch_annotation_cell(experiment_id="<id>", run_id="<id>", annotation_column_id="<id>", datapoint_id="<id>", value={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | ID of the experiment.                                                                                                                                                                                                                                                            |
| `run_id`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | ID of the run.                                                                                                                                                                                                                                                                   |
| `annotation_column_id`                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | ID of the annotation column.                                                                                                                                                                                                                                                     |
| `datapoint_id`                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | ID of the row.                                                                                                                                                                                                                                                                   |
| `value`                                                                                                                                                                                                                                                                          | Dict[str, *Any*]                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                               | Annotation value. type is required: range uses {type: range, value: number}; single- and multi-select use {type: categorical, value: string} or {type: categorical, values: [{value: string, sentiment: string}]}; text and correction use {type: free_form_text, text: string}. |
| `task_id`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                               | ID of the task column whose response is being annotated. An annotation column<br/> holds one cell per task column.                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                              |

### Response

**[models.Cell](../../models/cell.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## cancel_run

Stops queued and running cells and moves the run to canceled. A cell whose execution is already in flight may still write its result.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunCancel" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/cancel" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.cancel_run(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                   | *str*                                                                                                             | :heavy_check_mark:                                                                                                | ID of the experiment.                                                                                             |
| `run_id`                                                                                                          | *str*                                                                                                             | :heavy_check_mark:                                                                                                | ID of the run.                                                                                                    |
| `row_ids`                                                                                                         | List[*str*]                                                                                                       | :heavy_minus_sign:                                                                                                | Rows whose queued and running cells are canceled. Empty cancels every row.<br/> The run moves to canceled either way. |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_run_column_layout

Reorders, resizes, hides or shows columns of a run in one call. Columns not listed keep their layout.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunColumnLayoutUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/columns/layout" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_run_column_layout(experiment_id="<id>", run_id="<id>", columns=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `columns`                                                           | List[[models.ColumnLayout](../../models/columnlayout.md)]           | :heavy_check_mark:                                                  | Layout changes, at least one. Columns not listed keep their layout. |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_evals

Lists the evaluator columns of a run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentEvalList" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/evaluators" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list_evals(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListEvalColumnsResponse](../../models/listevalcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_eval

Links an existing evaluator. Each row gets one evaluator cell per task column. Config is updated at the evaluator source, not here.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentEvalCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/evaluators" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_eval(experiment_id="<id>", run_id="<id>", evaluator_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `experiment_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | ID of the experiment.                                                          |
| `run_id`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | ID of the run.                                                                 |
| `evaluator_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | ID of the evaluator to add. Each row gets one evaluator cell per task<br/> column. |
| `position`                                                                     | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | 0-based position among the run's columns. Defaults to the end.                 |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_eval

Removes an evaluator column and all its cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentEvalDelete" method="delete" path="/v3/experiments/{experiment_id}/runs/{run_id}/evaluators/{eval_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_eval(experiment_id="<id>", run_id="<id>", eval_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `eval_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the evaluator column.                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## execute_run

Executes cells at the requested scope. FULL, PARTIAL, ROW and COLUMN queue the matching cells (a task column also queues its linked evaluator and metric cells) and start the orchestrator, which also re-runs failed cells of every row it picks up. A run that is already queued or running rejects new execution until it finishes or is cancelled. CELL re-runs one task or evaluator cell in place. Re-executing a terminal run does not require creating a new run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunExecute" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/execute" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.execute_run(experiment_id="<id>", run_id="<id>", scope="EXECUTE_SCOPE_COLUMN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `experiment_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | ID of the experiment.                                                     |
| `run_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | ID of the run.                                                            |
| `scope`                                                                   | [models.ExecuteScope](../../models/executescope.md)                       | :heavy_check_mark:                                                        | N/A                                                                       |
| `targets`                                                                 | List[[models.ExecuteTarget](../../models/executetarget.md)]               | :heavy_minus_sign:                                                        | Rows and columns to execute. Required for row, column and cell scope.     |
| `constraints`                                                             | [Optional[models.ExecuteConstraints]](../../models/executeconstraints.md) | :heavy_minus_sign:                                                        | Limits for this execution, saved into the run's settings.                 |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_run_metrics

Returns aggregated evaluator and built-in metrics for a run, keyed by task column and metric. Pass baseline_run_id to include the delta against another run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunMetricsGet" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/metrics" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.get_run_metrics(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `experiment_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the experiment.                                                                     |
| `run_id`                                                                                  | *str*                                                                                     | :heavy_check_mark:                                                                        | ID of the run.                                                                            |
| `baseline_run_id`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Run of the same experiment to compare against. A run without values<br/> returns no baseline. |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.GetRunMetricsResponse](../../models/getrunmetricsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## query_run

Returns the rows of a run with their cells, filtered by row and column. POST because selections can exceed URL limits.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunQuery" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/query" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.query_run(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                                                                              | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | ID of the experiment.                                                                                                                                                        |
| `run_id`                                                                                                                                                                     | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | ID of the run.                                                                                                                                                               |
| `rows`                                                                                                                                                                       | List[*str*]                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                           | Row IDs to return. Unknown IDs are ignored. Omit for every row.                                                                                                              |
| `columns`                                                                                                                                                                    | List[*str*]                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                           | Columns to return, matched against column ID, key and display name. Every<br/> matching column is used, and an entry that matches nothing is rejected.<br/> Omit for every column. |
| `limit`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Page size, 1 to 1000. Defaults to 25.                                                                                                                                        |
| `starting_after`                                                                                                                                                             | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | Cursor for forward pagination. Set to the `row_id` of the last row from<br/> the previous page.                                                                              |
| `updated_after`                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                         | :heavy_minus_sign:                                                                                                                                                           | Incremental refresh: return only rows updated after this instant. Pass the<br/> previous response's `server_timestamp`. With `partial_rows`, running rows<br/> are returned as well. |
| `partial_rows`                                                                                                                                                               | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Return only running, completed and failed rows.                                                                                                                              |
| `exclude_static_cells`                                                                                                                                                       | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Leave out data cells: inputs, messages, expected output and job output.                                                                                                      |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.QueryRunResponse](../../models/queryrunresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_rows

Deletes the given rows of a run and their cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunRowsDelete" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/rows/bulk-delete" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_rows(experiment_id="<id>", run_id="<id>", row_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `experiment_id`                                                                    | *str*                                                                              | :heavy_check_mark:                                                                 | ID of the experiment.                                                              |
| `run_id`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | ID of the run.                                                                     |
| `row_ids`                                                                          | List[*str*]                                                                        | :heavy_check_mark:                                                                 | Rows to delete, at least one. Unknown IDs are ignored as long as one row<br/> matches. |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## duplicate_row

Copies a row into a new row at the end of the run. Dataset and annotation cells keep their values; response, agent response, open response, evaluator and metric cells start empty.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunRowDuplicate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/rows/{row_id}/duplicate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.duplicate_row(experiment_id="<id>", run_id="<id>", row_id="<id>", duplicate_row_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `row_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the row to copy.                                              |
| `duplicate_row_request`                                             | [models.DuplicateRowRequest](../../models/duplicaterowrequest.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.QueryRow](../../models/queryrow.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_tasks

Lists the task columns of a run: prompt, agent and openresponse columns.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskList" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list_tasks(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTaskColumnsResponse](../../models/listtaskcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_task

Adds a task column with one source: a prompt, an agent, or an openresponse column filled outside orq.ai. Every existing row gets a cell for it, and the first task column also adds cost and latency metric columns.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_task(experiment_id="<id>", run_id="<id>", display_name="Mohammed.Hickle")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `experiment_id`                                                                   | *str*                                                                             | :heavy_check_mark:                                                                | ID of the experiment.                                                             |
| `run_id`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | ID of the run.                                                                    |
| `display_name`                                                                    | *str*                                                                             | :heavy_check_mark:                                                                | Column name.                                                                      |
| `prompt`                                                                          | [Optional[models.PromptTaskConfig]](../../models/prompttaskconfig.md)             | :heavy_minus_sign:                                                                | Runs a prompt. Set exactly one of `prompt`, `agent` or `openresponse`.            |
| `agent`                                                                           | [Optional[models.AgentTaskConfig]](../../models/agenttaskconfig.md)               | :heavy_minus_sign:                                                                | Runs an agent.                                                                    |
| `openresponse`                                                                    | [Optional[models.OpenResponseTaskConfig]](../../models/openresponsetaskconfig.md) | :heavy_minus_sign:                                                                | Creates a column whose cells are filled outside orq.ai.                           |
| `position`                                                                        | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | 0-based position among the run's columns. Defaults to the end.                    |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_task

Deletes a task column with its cells and the evaluator, metric and annotation cells linked to it. Deleting the last task column also removes the metric columns.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskDelete" method="delete" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks/{task_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_task(experiment_id="<id>", run_id="<id>", task_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | ID of the experiment.                                               |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the run.                                                      |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | ID of the task column.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_task

Renames a task column or replaces its source. Existing cells are not changed.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks/{task_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_task(experiment_id="<id>", run_id="<id>", task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                                                         | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the experiment.                                                                                                                                   |
| `run_id`                                                                                                                                                | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the run.                                                                                                                                          |
| `task_id`                                                                                                                                               | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the task column.                                                                                                                                  |
| `display_name`                                                                                                                                          | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | New column name. Must not be empty.                                                                                                                     |
| `prompt`                                                                                                                                                | [Optional[models.PromptTaskConfig]](../../models/prompttaskconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                      | Replaces the column's source with this prompt. A new source replaces the<br/> whole config and can change the column type; existing cells are not<br/> changed. |
| `agent`                                                                                                                                                 | [Optional[models.AgentTaskConfig]](../../models/agenttaskconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                      | Replaces the column's source with this agent.                                                                                                           |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## export_run

Downloads the run as a file, including annotations and evaluator corrections made after an earlier export.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunExport" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/export" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.export_run(experiment_id="<id>", run_id="<id>", format_="json")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                                            | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | ID of the experiment.                                                                                                      |
| `run_id`                                                                                                                   | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | ID of the run.                                                                                                             |
| `format_`                                                                                                                  | [Optional[models.QueryParamFormat]](../../models/queryparamformat.md)                                                      | :heavy_minus_sign:                                                                                                         | File format: `json` (an array of records), `jsonl` (one record per line) or `csv`. Each record is one row and task column. |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[models.ExperimentRunExportResponse](../../models/experimentrunexportresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |