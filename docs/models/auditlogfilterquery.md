# AuditLogFilterQuery

Search and advanced filters for querying audit logs.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `search`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | Optional text search applied to supported display fields.  | Production skill                                           |
| `operator`                                                 | *str*                                                      | :heavy_check_mark:                                         | Logical operator used to combine filters.                  | and                                                        |
| `filters`                                                  | List[[models.AuditLogFilter](../models/auditlogfilter.md)] | :heavy_check_mark:                                         | Advanced filters applied to the query.                     |                                                            |