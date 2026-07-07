# LiteLLMModelInfo


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `db_model`                  | *Nullable[bool]*            | :heavy_check_mark:          | N/A                         |
| `id`                        | *Nullable[str]*             | :heavy_check_mark:          | N/A                         |
| `input_cost_per_token`      | *Optional[float]*           | :heavy_minus_sign:          | N/A                         |
| `key`                       | *Nullable[str]*             | :heavy_check_mark:          | N/A                         |
| `litellm_provider`          | *Nullable[str]*             | :heavy_check_mark:          | N/A                         |
| `max_input_tokens`          | *Optional[int]*             | :heavy_minus_sign:          | N/A                         |
| `max_output_tokens`         | *Optional[int]*             | :heavy_minus_sign:          | N/A                         |
| `mode`                      | *Nullable[str]*             | :heavy_check_mark:          | N/A                         |
| `output_cost_per_token`     | *Optional[float]*           | :heavy_minus_sign:          | N/A                         |
| `supported_openai_params`   | List[*str*]                 | :heavy_minus_sign:          | N/A                         |
| `supports_function_calling` | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_native_streaming` | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_reasoning`        | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_response_schema`  | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_system_messages`  | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_tool_choice`      | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `supports_vision`           | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |