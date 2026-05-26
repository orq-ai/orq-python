# APIKeyOwner

Owner attribution drives lifecycle.

 `service_account` keys are workspace-owned and outlive any individual
 user. `user` keys are bound to `user_id`: when the user is removed,
 disabled, or loses project access, the key is revoked / its scope
 shrinks per the cascade rules in ADR 0001.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `user`                                                                   | [Optional[models.UserOwner]](../models/userowner.md)                     | :heavy_minus_sign:                                                       | N/A                                                                      |
| `service_account`                                                        | [Optional[models.ServiceAccountOwner]](../models/serviceaccountowner.md) | :heavy_minus_sign:                                                       | N/A                                                                      |