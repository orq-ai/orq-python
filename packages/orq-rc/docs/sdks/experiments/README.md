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
* [cancel_run](#cancel_run) - Cancel a run
* [update_run_column_layout](#update_run_column_layout) - Update column layout
* [list_evals](#list_evals) - List eval columns
* [create_eval](#create_eval) - Add an eval column
* [delete_eval](#delete_eval) - Remove an eval column
* [patch_eval_cell](#patch_eval_cell) - Correct an eval cell
* [execute_run](#execute_run) - Execute a run
* [get_run_metrics](#get_run_metrics) - Get run metrics
* [query_run](#query_run) - Query run cells
* [list_reviews](#list_reviews) - List human review columns
* [create_review](#create_review) - Add a human review column
* [delete_review](#delete_review) - Remove a human review column
* [update_review](#update_review) - Update review column metadata
* [patch_review_cell](#patch_review_cell) - Set a human review cell
* [delete_rows](#delete_rows) - Delete rows
* [update_run_cell](#update_run_cell) - Update a cell
* [duplicate_row](#duplicate_row) - Duplicate a row
* [list_tasks](#list_tasks) - List task columns
* [create_task](#create_task) - Add a task column
* [delete_task](#delete_task) - Delete a task column
* [update_task](#update_task) - Update a task column
* [patch_task_cell](#patch_task_cell) - Ingest a task cell
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListExperimentsResponse](../../models/listexperimentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates an experiment. project_id defaults to the API key's project and is required for keys that span several projects. When dataset_id is set, a draft run is created with rows from that dataset.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentCreate" method="post" path="/v3/experiments" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `project_id`                                                                                                  | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | Project the experiment is created in; defaults to the API key's project when omitted.                         |
| `dataset_id`                                                                                                  | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `dataset_version_id`                                                                                          | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `source_run`                                                                                                  | [Optional[models.RunRef]](../../models/runref.md)                                                             | :heavy_minus_sign:                                                                                            | Copies the task, evaluator and review columns of an existing run into the<br/> new experiment's first run (fork). |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Experiment](../../models/experiment.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes an experiment and its runs.

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `selected_run_id`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `row_height_level`                                                  | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_metrics`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListExperimentRunsResponse](../../models/listexperimentrunsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_run

Creates a new run, copying columns from the selected run when present. A rerun is a new run.

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `key`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `settings`                                                          | [Optional[models.RunSettings]](../../models/runsettings.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_run

Deletes a run and its cell data. Distinct from cancel, which keeps completed cells.

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `key`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `settings`                                                          | [Optional[models.RunSettings]](../../models/runsettings.md)         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Run](../../models/run.md)**

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `row_ids`                                                           | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

    res = orq.experiments.update_run_column_layout(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `columns`                                                           | List[[models.ColumnLayout](../../models/columnlayout.md)]           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Run](../../models/run.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_evals

List eval columns

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListEvalColumnsResponse](../../models/listevalcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_eval

Links an existing evaluator. Config is updated at the evaluator source, not here.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentEvalCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/evaluators" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_eval(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `evaluator_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `position`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_eval

Remove an eval column

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `eval_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_eval_cell

Human override of an automated evaluator verdict on one datapoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentEvalCellPatch" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/evaluators/{eval_id}/cells/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.patch_eval_cell(experiment_id="<id>", run_id="<id>", eval_id="<id>", datapoint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `eval_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datapoint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `value`                                                             | [Optional[models.Value]](../../models/value.md)                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Cell](../../models/cell.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## execute_run

Executes cells at the requested scope. FULL, PARTIAL, ROW and COLUMN queue the matching cells (a task column also queues its linked evaluator, metric and review cells) and start the orchestrator, which also re-runs failed cells of every row it picks up; a run that is already running accepts new work. CELL re-runs one task or evaluator cell in place. Re-executing does not require creating a new run.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunExecute" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/execute" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.execute_run(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `experiment_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `run_id`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `scope`                                                                   | [Optional[models.ExecuteScope]](../../models/executescope.md)             | :heavy_minus_sign:                                                        | N/A                                                                       |
| `targets`                                                                 | List[[models.ExecuteTarget](../../models/executetarget.md)]               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `constraints`                                                             | [Optional[models.ExecuteConstraints]](../../models/executeconstraints.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `repeat_count`                                                            | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `baseline_run_id`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRunMetricsResponse](../../models/getrunmetricsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## query_run

Returns selected cells by row and column name. POST because selections can exceed URL limits.

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

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                                      | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `run_id`                                                                                             | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `rows`                                                                                               | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `columns`                                                                                            | List[*str*]                                                                                          | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `repeat_index`                                                                                       | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `limit`                                                                                              | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `starting_after`                                                                                     | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `updated_after`                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                 | :heavy_minus_sign:                                                                                   | Incremental refresh: returns running rows plus completed or failed rows<br/> updated after this instant. |
| `partial_rows`                                                                                       | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `exclude_static_cells`                                                                               | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[models.QueryRunResponse](../../models/queryrunresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_reviews

List human review columns

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentReviewList" method="get" path="/v3/experiments/{experiment_id}/runs/{run_id}/reviews" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.list_reviews(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListReviewColumnsResponse](../../models/listreviewcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_review

Add a human review column

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentReviewCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/reviews" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_review(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `human_eval_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `human_eval_type`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `position`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_review

Remove a human review column

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentReviewDelete" method="delete" path="/v3/experiments/{experiment_id}/runs/{run_id}/reviews/{review_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    orq.experiments.delete_review(experiment_id="<id>", run_id="<id>", review_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `review_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_review

Updates display fields on the column. The human-eval definition is updated at source.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentReviewUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/reviews/{review_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_review(experiment_id="<id>", run_id="<id>", review_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `review_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_review_cell

Set a human review cell

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentReviewCellPatch" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/reviews/{review_id}/cells/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.patch_review_cell(experiment_id="<id>", run_id="<id>", review_id="<id>", datapoint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `experiment_id`                                                                             | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `run_id`                                                                                    | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `review_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `datapoint_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `value`                                                                                     | [Optional[models.PatchReviewCellRequestValue]](../../models/patchreviewcellrequestvalue.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.Cell](../../models/cell.md)**

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

    orq.experiments.delete_rows(experiment_id="<id>", run_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `row_ids`                                                           | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_run_cell

Writes a cell value by cell id, including dataset and review cells. An empty value clears the cell. Running cells cannot be changed.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentRunCellUpdate" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/rows/{row_id}/cells/{cell_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.update_run_cell(experiment_id="<id>", run_id="<id>", row_id="<id>", cell_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `experiment_id`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `run_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `row_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `cell_id`                                                                               | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `value`                                                                                 | [Optional[models.UpdateRunCellRequestValue]](../../models/updateruncellrequestvalue.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.Cell](../../models/cell.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## duplicate_row

Copies a row's dataset cells into a new row placed after the source. Task, evaluator, metric and review cells start empty.

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `row_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

List task columns

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTaskColumnsResponse](../../models/listtaskcolumnsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_task

Attaches a prompt, orq agent, or (reserved) harness config as a task column. Input mapping is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskCreate" method="post" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.create_task(experiment_id="<id>", run_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `experiment_id`                                                                   | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `run_id`                                                                          | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `display_name`                                                                    | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `prompt`                                                                          | [Optional[models.PromptTaskConfig]](../../models/prompttaskconfig.md)             | :heavy_minus_sign:                                                                | N/A                                                                               |
| `agent`                                                                           | [Optional[models.AgentTaskConfig]](../../models/agenttaskconfig.md)               | :heavy_minus_sign:                                                                | N/A                                                                               |
| `harness`                                                                         | [Optional[models.HarnessTaskConfig]](../../models/harnesstaskconfig.md)           | :heavy_minus_sign:                                                                | N/A                                                                               |
| `openresponse`                                                                    | [Optional[models.OpenResponseTaskConfig]](../../models/openresponsetaskconfig.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `position`                                                                        | *Optional[int]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_task

Delete a task column

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
| `experiment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_task

Updates an unlinked task column in place.

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

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `experiment_id`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `run_id`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `task_id`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `display_name`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `prompt`                                                                | [Optional[models.PromptTaskConfig]](../../models/prompttaskconfig.md)   | :heavy_minus_sign:                                                      | N/A                                                                     |
| `agent`                                                                 | [Optional[models.AgentTaskConfig]](../../models/agenttaskconfig.md)     | :heavy_minus_sign:                                                      | N/A                                                                     |
| `harness`                                                               | [Optional[models.HarnessTaskConfig]](../../models/harnesstaskconfig.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.Column](../../models/column.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_task_cell

Writes a cell result, including externally executed or harness cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExperimentTaskCellPatch" method="patch" path="/v3/experiments/{experiment_id}/runs/{run_id}/tasks/{task_id}/cells/{datapoint_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.experiments.patch_task_cell(experiment_id="<id>", run_id="<id>", task_id="<id>", datapoint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `experiment_id`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `run_id`                                                                                | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `task_id`                                                                               | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `datapoint_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `repeat_index`                                                                          | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `value`                                                                                 | [Optional[models.PatchTaskCellRequestValue]](../../models/patchtaskcellrequestvalue.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `artifacts`                                                                             | [Optional[models.ArtifactRefs]](../../models/artifactrefs.md)                           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.Cell](../../models/cell.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## export_run

Downloads the run as a file, including human review and evaluator corrections made after an earlier export.

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

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `experiment_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `run_id`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `format_`                                                             | [Optional[models.QueryParamFormat]](../../models/queryparamformat.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ExperimentRunExportResponse](../../models/experimentrunexportresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |