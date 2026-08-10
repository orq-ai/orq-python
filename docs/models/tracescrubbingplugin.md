# TraceScrubbingPlugin


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`                                                                                    | [models.TraceScrubbingPluginID](../models/tracescrubbingpluginid.md)                    | :heavy_check_mark:                                                                      | Plugin discriminator. Must be `trace_scrubbing`.                                        |
| `mask`                                                                                  | List[[models.Mask](../models/mask.md)]                                                  | :heavy_check_mark:                                                                      | Trace surfaces to scrub. `all` includes system, input, output, metadata, and variables. |