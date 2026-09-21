# DatapointInput

Datapoint content submitted by the caller.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `inputs`                                                                   | [Optional[models.DatapointInputInputs]](../models/datapointinputinputs.md) | :heavy_minus_sign:                                                         | Structured variables passed to the prompt or workflow.                     |
| `messages`                                                                 | List[*Any*]                                                                | :heavy_minus_sign:                                                         | A JSON array containing dynamically typed values.                          |
| `expected_output`                                                          | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Reference output expected for this datapoint.                              |