# RunAgentPartsFilePart

A file content part that can contain either base64-encoded bytes or a URI reference. Used for images, documents, and other binary content in agent communications.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `kind`                                                                                 | [models.RunAgentPartsAgentsResponseKind](../models/runagentpartsagentsresponsekind.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `file`                                                                                 | [models.RunAgentPartsFile](../models/runagentpartsfile.md)                             | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `metadata`                                                                             | Dict[str, *Any*]                                                                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |