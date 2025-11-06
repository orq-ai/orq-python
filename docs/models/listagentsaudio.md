# ListAgentsAudio

Parameters for audio output. Required when audio output is requested with modalities: ["audio"]. Learn more.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `voice`                                                                                                | [models.ListAgentsVoice](../models/listagentsvoice.md)                                                 | :heavy_check_mark:                                                                                     | The voice the model uses to respond. Supported voices are alloy, echo, fable, onyx, nova, and shimmer. |
| `format_`                                                                                              | [models.ListAgentsFormat](../models/listagentsformat.md)                                               | :heavy_check_mark:                                                                                     | Specifies the output audio format. Must be one of wav, mp3, flac, opus, or pcm16.                      |