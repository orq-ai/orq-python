# DeleteChunksResponseBody

Chunks deletion result


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `deleted_count`                          | *float*                                  | :heavy_check_mark:                       | Number of chunks successfully deleted    |
| `failed_ids`                             | List[*str*]                              | :heavy_minus_sign:                       | Array of chunk IDs that failed to delete |