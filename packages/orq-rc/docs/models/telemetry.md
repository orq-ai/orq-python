# Telemetry

Telemetry information for correlating the response with traces


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `trace_id`                                          | *str*                                               | :heavy_check_mark:                                  | The root trace ID for the agent execution           |
| `span_id`                                           | *str*                                               | :heavy_check_mark:                                  | The span ID of the agent execution within the trace |