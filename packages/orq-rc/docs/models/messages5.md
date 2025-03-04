# Messages5


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `role`                                                                         | [models.DeploymentsMessages5Role](../models/deploymentsmessages5role.md)       | :heavy_check_mark:                                                             | The role of the messages author, in this case tool.                            |
| `content`                                                                      | [models.DeploymentsMessages5Content](../models/deploymentsmessages5content.md) | :heavy_check_mark:                                                             | The contents of the tool message.                                              |
| `tool_call_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | Tool call that this message is responding to.                                  |