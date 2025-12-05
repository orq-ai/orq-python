# RedactedReasoningPartSchema

A message part containing reasoning or chain-of-thought content


## Fields

| Field                                                                                                           | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                          | [models.RedactedReasoningPartSchemaType](../models/redactedreasoningpartschematype.md)                          | :heavy_check_mark:                                                                                              | The type of the content part. Always `reasoning`.                                                               |
| `data`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | The encrypted reasoning or thought process behind the response. Used for chain-of-thought or extended thinking. |