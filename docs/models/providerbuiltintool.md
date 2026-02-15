# ProviderBuiltInTool

Provider-specific built-in tools that are passed through to the provider. Must be prefixed with the provider name (e.g., openai:web_search, anthropic:web_search_20250305, google:google_search).


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `type`                                               | *str*                                                | :heavy_check_mark:                                   | Provider-prefixed tool type                          |
| `requires_approval`                                  | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Whether this tool requires approval before execution |