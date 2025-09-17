# ToolsBlueprint

The blueprint for the HTTP request. The `arguments` field will be used to replace the placeholders in the `url`, `headers`, `body`, and `arguments` fields.


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `url`                                          | *str*                                          | :heavy_check_mark:                             | The URL to send the request to.                |
| `method`                                       | [models.ToolsMethod](../models/toolsmethod.md) | :heavy_check_mark:                             | The HTTP method to use.                        |
| `headers`                                      | Dict[str, *str*]                               | :heavy_minus_sign:                             | The headers to send with the request.          |
| `body`                                         | Dict[str, *Any*]                               | :heavy_minus_sign:                             | The body to send with the request.             |