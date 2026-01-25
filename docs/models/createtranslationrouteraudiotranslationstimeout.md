# CreateTranslationRouterAudioTranslationsTimeout

Timeout configuration to apply to the request. If the request exceeds the timeout, it will be retried or fallback to the next model if configured.


## Fields

| Field                         | Type                          | Required                      | Description                   | Example                       |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `call_timeout`                | *float*                       | :heavy_check_mark:            | Timeout value in milliseconds | 30000                         |