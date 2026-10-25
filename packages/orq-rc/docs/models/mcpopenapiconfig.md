# McpOpenAPIConfig


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `document_url`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | URL the document is fetched from; `:sync` fetches it again.            |
| `operations`                                                           | List[*str*]                                                            | :heavy_minus_sign:                                                     | Tool names of the operations to expose; empty exposes every operation. |
| `title`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | `info.title` of the compiled document.                                 |
| `version`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | `info.version` of the compiled document.                               |