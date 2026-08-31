# QueryAuditLogsResponse

Paginated audit log query result.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `audit_logs`                                                            | List[[models.AuditLog](../models/auditlog.md)]                          | :heavy_check_mark:                                                      | Audit logs matching the query.                                          |                                                                         |
| `overall_total`                                                         | *str*                                                                   | :heavy_check_mark:                                                      | Total number of audit logs matching the query before cursor pagination. | 42                                                                      |
| `has_more`                                                              | *bool*                                                                  | :heavy_check_mark:                                                      | Whether another page exists after the returned audit logs.              | false                                                                   |