# CreateTranscriptionLoadBalancerModels


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `model`                                          | *str*                                            | :heavy_check_mark:                               | Model identifier for load balancing              | openai/gpt-5.6-sol                               |
| `weight`                                         | *Optional[float]*                                | :heavy_minus_sign:                               | Weight assigned to this model for load balancing | 0.7                                              |