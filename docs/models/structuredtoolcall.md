# StructuredToolCall

StructuredToolCall mirrors one tool invocation and its result. Name is the
 only field the grader requires; a call without one is dropped.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `arguments`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `output`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |