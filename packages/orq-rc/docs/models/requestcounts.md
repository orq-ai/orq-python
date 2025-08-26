# RequestCounts

The request counts for different statuses within the batch.


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `total`                                                   | *int*                                                     | :heavy_check_mark:                                        | Total number of requests in the batch.                    |
| `completed`                                               | *int*                                                     | :heavy_check_mark:                                        | Number of requests that have been completed successfully. |
| `failed`                                                  | *int*                                                     | :heavy_check_mark:                                        | Number of requests that have failed.                      |