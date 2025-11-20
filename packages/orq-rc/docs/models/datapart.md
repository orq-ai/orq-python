# DataPart

A structured data part containing JSON-serializable key-value pairs. Used for passing structured information between agents and tools.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `kind`                                                             | [models.GetAgentTaskPartsKind](../models/getagenttaskpartskind.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `data`                                                             | Dict[str, *Any*]                                                   | :heavy_check_mark:                                                 | N/A                                                                |
| `metadata`                                                         | Dict[str, *Any*]                                                   | :heavy_minus_sign:                                                 | N/A                                                                |