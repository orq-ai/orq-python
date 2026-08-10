# IdentityBudgetScopeRestResponse

Per-identity cap. Keyed by the contact's external_id (not the
 internal Mongo `_id`) so the scope is stable across imports.


## Fields

| Field                  | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `identity_external_id` | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |