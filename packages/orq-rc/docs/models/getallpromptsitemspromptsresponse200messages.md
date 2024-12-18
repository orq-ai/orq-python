# GetAllPromptsItemsPromptsResponse200Messages


## Fields

| Field                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `role`                                                                                                                                                                                                                                                                   | [models.GetAllPromptsItemsPromptsResponse200Role](../models/getallpromptsitemspromptsresponse200role.md)                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                       | The role of the prompt message                                                                                                                                                                                                                                           |
| `content`                                                                                                                                                                                                                                                                | [models.GetAllPromptsItemsPromptsResponse200Content](../models/getallpromptsitemspromptsresponse200content.md)                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                       | The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts.  |
| `tool_calls`                                                                                                                                                                                                                                                             | List[[models.GetAllPromptsItemsPromptsResponse200ToolCalls](../models/getallpromptsitemspromptsresponse200toolcalls.md)]                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                      |