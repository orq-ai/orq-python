# GetAllPromptTemplatesItemsPromptTemplatesResponseMessages


## Fields

| Field                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `role`                                                                                                                                                                                                                                                                   | [models.GetAllPromptTemplatesItemsPromptTemplatesResponseRole](../models/getallprompttemplatesitemsprompttemplatesresponserole.md)                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                       | The role of the prompt message                                                                                                                                                                                                                                           |
| `content`                                                                                                                                                                                                                                                                | [models.GetAllPromptTemplatesItemsPromptTemplatesResponseContent](../models/getallprompttemplatesitemsprompttemplatesresponsecontent.md)                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                       | The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts.  |
| `tool_calls`                                                                                                                                                                                                                                                             | List[[models.GetAllPromptTemplatesItemsPromptTemplatesResponseToolCalls](../models/getallprompttemplatesitemsprompttemplatesresponsetoolcalls.md)]                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                      |