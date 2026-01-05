# PartDeltaEvent

Emitted for each content chunk streamed from the LLM. The delta field contains a discriminated union based on the kind field.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `type`                                                       | [models.PartDeltaEventType](../models/partdeltaeventtype.md) | :heavy_check_mark:                                           | N/A                                                          |
| `timestamp`                                                  | *str*                                                        | :heavy_check_mark:                                           | ISO timestamp of when the event occurred                     |
| `data`                                                       | [models.PartDeltaEventData](../models/partdeltaeventdata.md) | :heavy_check_mark:                                           | N/A                                                          |