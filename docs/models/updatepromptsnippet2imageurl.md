# UpdatePromptSnippet2ImageURL


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `url`                                                                                | *str*                                                                                | :heavy_check_mark:                                                                   | Either a URL of the image or the base64 encoded data URI.                            |
| `detail`                                                                             | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Specifies the detail level of the image. Currently only supported with OpenAI models |