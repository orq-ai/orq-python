# CreateClassifyResponseBody

Returns one answer per question.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `answers`                                                            | Dict[str, [models.ClassifyAnswer](../models/classifyanswer.md)]      | :heavy_check_mark:                                                   | Answers keyed by the question identifiers from the request.          |
| `model`                                                              | *str*                                                                | :heavy_check_mark:                                                   | The model ID from the request.                                       |
| `telemetry`                                                          | [Optional[models.ResponseTelemetry]](../models/responsetelemetry.md) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `usage`                                                              | [models.ClassifyUsage](../models/classifyusage.md)                   | :heavy_check_mark:                                                   | N/A                                                                  |