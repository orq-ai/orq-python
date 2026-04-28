# AllowedTools

Filter which tools from the MCP server are exposed.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `read_only`                                     | *Optional[bool]*                                | :heavy_minus_sign:                              | Only expose tools with readOnlyHint annotation. |
| `tool_names`                                    | List[*str*]                                     | :heavy_minus_sign:                              | List of allowed tool names.                     |