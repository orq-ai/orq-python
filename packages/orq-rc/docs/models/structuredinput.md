# StructuredInput

StructuredInput names its fields after the template variables they feed, so
 input.user_query in a prompt is user_query here.


## Fields

| Field                 | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `system_instructions` | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |
| `user_query`          | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |
| `retrievals`          | List[*str*]           | :heavy_minus_sign:    | N/A                   |
| `expected_output`     | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |