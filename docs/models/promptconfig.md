# PromptConfig

A list of messages compatible with the openAI schema


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `stream`                                                               | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `model`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `model_type`                                                           | [OptionalNullable[models.ModelType]](../models/modeltype.md)           | :heavy_minus_sign:                                                     | The modality of the model                                              |
| `model_parameters`                                                     | [Optional[models.ModelParameters]](../models/modelparameters.md)       | :heavy_minus_sign:                                                     | Model Parameters: Not all parameters apply to every model              |
| `provider`                                                             | [Optional[models.Provider]](../models/provider.md)                     | :heavy_minus_sign:                                                     | N/A                                                                    |
| `version`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `messages`                                                             | List[[models.CreatePromptMessages](../models/createpromptmessages.md)] | :heavy_check_mark:                                                     | N/A                                                                    |