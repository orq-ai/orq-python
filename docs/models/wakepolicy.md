# WakePolicy


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `type`                                                                     | [models.CreateLiveSessionLiveType](../models/createlivesessionlivetype.md) | :heavy_check_mark:                                                         | Wait for speech before starting inference.                                 |
| `vad_threshold`                                                            | *Optional[float]*                                                          | :heavy_minus_sign:                                                         | Evidence of speech required to wake from standby.                          |