# ChunkingCleanupOptions

The cleanup options applied to the datasource content. All options are enabled by default to ensure enhanced security and optimal chunk quality. Defaults to system-standard cleanup options if not specified.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `delete_emails`                                                        | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Removes email addresses from the provided text.                        |
| `delete_credit_cards`                                                  | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Removes credit card numbers from the provided text.                    |
| `delete_phone_numbers`                                                 | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Removes phone numbers from the provided text.                          |
| `clean_bullet_points`                                                  | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Removes bullet points formatting from the text.                        |
| `clean_numbered_list`                                                  | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Removes numbered list formatting from the text.                        |
| `clean_unicode`                                                        | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Normalizes or removes unnecessary unicode characters from the text.    |
| `clean_dashes`                                                         | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Normalizes or removes various dash characters to standardize the text. |
| `clean_whitespaces`                                                    | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Trims and normalizes excessive whitespace throughout the text.         |