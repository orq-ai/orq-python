# FileInURIFormat

File in URI format. Check in the model's documentation for the supported mime types for the URI format


## Fields

| Field                          | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `uri`                          | *str*                          | :heavy_check_mark:             | URL for the File content       | https://example.com/report.pdf |
| `mime_type`                    | *Optional[str]*                | :heavy_minus_sign:             | Optional mimeType for the file |                                |
| `name`                         | *Optional[str]*                | :heavy_minus_sign:             | Optional name for the file     |                                |