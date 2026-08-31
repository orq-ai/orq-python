# QueryAuditLogsRequest

Request body for querying audit logs in the authenticated workspace.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filters`                                                           | [models.AuditLogFilterQuery](../models/auditlogfilterquery.md)      | :heavy_check_mark:                                                  | Search and advanced filters for querying audit logs.                |
| `pagination`                                                        | [models.AuditLogPagination](../models/auditlogpagination.md)        | :heavy_check_mark:                                                  | Cursor pagination settings for audit log queries.                   |
| `sorting`                                                           | List[[models.AuditLogSort](../models/auditlogsort.md)]              | :heavy_minus_sign:                                                  | Sort expressions. Defaults to audit_log_id descending when omitted. |