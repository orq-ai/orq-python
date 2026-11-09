# User

User is the canonical workspace-user record.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Workspace-user identifier.                                             |
| `account_id`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Account identifier.                                                    |
| `email`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Account email.                                                         |
| `display_name`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Account display name.                                                  |
| `logo_url`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Avatar URL.                                                            |
| `team_ids`                                                             | List[*str*]                                                            | :heavy_minus_sign:                                                     | Team identifiers. The support-only team is excluded.                   |
| `roles`                                                                | List[*str*]                                                            | :heavy_minus_sign:                                                     | Effective workspace roles.                                             |
| `last_activity`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Last activity timestamp. Absent when never active.                     |
| `invitation_data`                                                      | [Optional[models.UserInvitationData]](../models/userinvitationdata.md) | :heavy_minus_sign:                                                     | Outstanding invitation metadata. Absent for active accounts.           |