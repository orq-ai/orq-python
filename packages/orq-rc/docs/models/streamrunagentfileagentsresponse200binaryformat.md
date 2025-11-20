# StreamRunAgentFileAgentsResponse200BinaryFormat

Binary in base64 format. Check in the model's documentation for the supported mime types for the binary format.


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `bytes_`                           | *str*                              | :heavy_check_mark:                 | base64 encoded content of the file |
| `mime_type`                        | *Optional[str]*                    | :heavy_minus_sign:                 | Optional mimeType for the file     |
| `name`                             | *Optional[str]*                    | :heavy_minus_sign:                 | Optional name for the file         |