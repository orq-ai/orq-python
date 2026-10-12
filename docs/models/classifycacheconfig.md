# ClassifyCacheConfig


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `ttl`                                                                                     | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | Time to live for the cached response in seconds, up to 259200 (3 days). Defaults to 3600. |
| `type`                                                                                    | [models.ClassifyCacheConfigType](../models/classifycacheconfigtype.md)                    | :heavy_check_mark:                                                                        | Cache type. Only exact_match is supported.                                                |