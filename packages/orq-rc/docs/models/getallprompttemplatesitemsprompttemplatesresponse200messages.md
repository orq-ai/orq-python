# GetAllPromptTemplatesItemsPromptTemplatesResponse200Messages


## Fields

| Field                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `role`                                                                                                                                                                                                                                                                   | [models.GetAllPromptTemplatesItemsPromptTemplatesResponse200Role](../models/getallprompttemplatesitemsprompttemplatesresponse200role.md)                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                       | The role of the prompt message                                                                                                                                                                                                                                           |
| `content`                                                                                                                                                                                                                                                                | [models.GetAllPromptTemplatesItemsPromptTemplatesResponse200Content](../models/getallprompttemplatesitemsprompttemplatesresponse200content.md)                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                       | The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts.  |
| `tool_calls`                                                                                                                                                                                                                                                             | List[[models.GetAllPromptTemplatesItemsPromptTemplatesResponse200ToolCalls](../models/getallprompttemplatesitemsprompttemplatesresponse200toolcalls.md)]                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                      |