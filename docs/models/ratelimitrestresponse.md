# RateLimitRestResponse

RateLimit is the per-minute request ceiling. Enforced via atomic
 increment-first semantics in the enforcement middleware.


## Fields

| Field                 | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `requests_per_minute` | *Optional[int]*       | :heavy_minus_sign:    | N/A                   |