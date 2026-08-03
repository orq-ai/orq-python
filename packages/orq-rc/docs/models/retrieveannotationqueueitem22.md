# RetrieveAnnotationQueueItem22

Represents the output of a function tool call, provided as input to the model.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `type`                                                                                   | [models.RetrieveAnnotationQueueItem2Type](../models/retrieveannotationqueueitem2type.md) | :heavy_check_mark:                                                                       | The type of input item                                                                   |
| `call_id`                                                                                | *str*                                                                                    | :heavy_check_mark:                                                                       | The ID of the function call this output is for                                           |
| `output`                                                                                 | *str*                                                                                    | :heavy_check_mark:                                                                       | The output from the function call                                                        |