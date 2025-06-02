# UpdateDatapoint2DatasetsInputAudio


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `data`                                                                               | *str*                                                                                | :heavy_check_mark:                                                                   | Base64 encoded audio data.                                                           |
| `format_`                                                                            | [models.UpdateDatapoint2DatasetsFormat](../models/updatedatapoint2datasetsformat.md) | :heavy_check_mark:                                                                   | The format of the encoded audio data. Currently supports `wav` and `mp3`.            |