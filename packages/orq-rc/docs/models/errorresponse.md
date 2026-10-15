# ErrorResponse


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `message`                                               | *str*                                                   | :heavy_check_mark:                                      | Human-readable error message.                           |
| `code`                                                  | *Optional[int]*                                         | :heavy_minus_sign:                                      | gRPC status code, when the service reports one.         |
| `details`                                               | List[*Any*]                                             | :heavy_minus_sign:                                      | Additional error details, when the service reports any. |