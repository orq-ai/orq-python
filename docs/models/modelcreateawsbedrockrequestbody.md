# ModelCreateAwsBedrockRequestBody


## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `assume_role_arn`         | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `assume_role_external_id` | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `auth_mode`               | *str*                     | :heavy_check_mark:        | N/A                       |
| `description`             | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `display_name`            | *str*                     | :heavy_check_mark:        | N/A                       |
| `has_reasoning`           | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `input_cost`              | *Optional[float]*         | :heavy_minus_sign:        | N/A                       |
| `integration_id`          | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `max_tokens`              | *Optional[int]*           | :heavy_minus_sign:        | N/A                       |
| `model_developer`         | *str*                     | :heavy_check_mark:        | N/A                       |
| `model_family`            | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `model_id`                | *str*                     | :heavy_check_mark:        | N/A                       |
| `model_type`              | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `output_cost`             | *Optional[float]*         | :heavy_minus_sign:        | N/A                       |
| `region`                  | *str*                     | :heavy_check_mark:        | N/A                       |
| `supports_json_mode`      | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `supports_json_schema`    | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `supports_strict_tool`    | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `supports_tool_calling`   | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `supports_vision`         | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |
| `temperature`             | *Optional[float]*         | :heavy_minus_sign:        | N/A                       |