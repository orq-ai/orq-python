# ReasoningPartSchema

A message part containing reasoning or chain-of-thought content


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `type`                                                                                                | [models.ReasoningPartSchemaType](../models/reasoningpartschematype.md)                                | :heavy_check_mark:                                                                                    | The type of the content part. Always `reasoning`.                                                     |
| `reasoning`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | The reasoning or thought process behind the response. Used for chain-of-thought or extended thinking. |
| `signature`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Optional cryptographic signature to verify the authenticity and integrity of the reasoning content    |