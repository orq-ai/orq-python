# PromptConfig


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `tools`                                                              | List[[models.DeploymentsTools](../models/deploymentstools.md)]       | :heavy_check_mark:                                                   | N/A                                                                  |
| `model`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `model_type`                                                         | [models.ModelType](../models/modeltype.md)                           | :heavy_check_mark:                                                   | The type of the model                                                |
| `model_parameters`                                                   | [models.ModelParameters](../models/modelparameters.md)               | :heavy_check_mark:                                                   | Model Parameters: Not all parameters apply to every model            |
| `provider`                                                           | [models.DeploymentsProvider](../models/deploymentsprovider.md)       | :heavy_check_mark:                                                   | N/A                                                                  |
| `messages`                                                           | List[[models.DeploymentsMessages](../models/deploymentsmessages.md)] | :heavy_check_mark:                                                   | N/A                                                                  |