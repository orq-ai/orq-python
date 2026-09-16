# AuditLogPagination

Cursor pagination settings for audit log queries.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `limit`                                                                         | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | Maximum number of audit logs to return. Defaults to 50 when omitted.            | 20                                                                              |
| `starting_after`                                                                | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Cursor for the next page. Use the last audit_log_id from the previous page.     | audit_log_01JZ9QMB6AEH7B8XH0ZQ9ZPQEY                                            |
| `ending_before`                                                                 | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Cursor for the previous page. Use the first audit_log_id from the current page. | audit_log_01JZ9QMB6AEH7B8XH0ZQ9ZPQEY                                            |