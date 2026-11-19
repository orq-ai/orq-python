# CellStatusCounts

Number of cells in each status, across every row and column of the run,
 dataset and annotation cells included.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `not_run`                                                         | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells that have never executed, including cells without a status. |
| `queued`                                                          | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells waiting to execute.                                         |
| `running`                                                         | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells executing now.                                              |
| `completed`                                                       | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells that finished successfully.                                 |
| `failed`                                                          | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells whose execution failed.                                     |
| `canceled`                                                        | *Optional[int]*                                                   | :heavy_minus_sign:                                                | Cells canceled before they finished.                              |