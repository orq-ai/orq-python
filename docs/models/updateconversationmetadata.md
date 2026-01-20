# UpdateConversationMetadata

Metadata fields to update. Only provided fields are modified.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `generating_title`                                                | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Set to `true` to indicate the title is being auto-generated.      |
| `entity_id`                                                       | *OptionalNullable[str]*                                           | :heavy_minus_sign:                                                | Parent entity identifier. Set to `null` to detach from an entity. |