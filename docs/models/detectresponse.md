# DetectResponse


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `has_pii`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `entities`                                                            | Dict[str, *int*]                                                      | :heavy_minus_sign:                                                    | Per-entity-type counts. Populated only when include_entities was set. |