# PublicBatchExpiresAfter


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `anchor`                                                | [Optional[models.Anchor]](../models/anchor.md)          | :heavy_minus_sign:                                      | Point the lifetime starts from. Defaults to created_at. |
| `seconds`                                               | *int*                                                   | :heavy_check_mark:                                      | Lifetime of the file, in seconds.                       |