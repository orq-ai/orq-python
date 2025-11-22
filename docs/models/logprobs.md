# Logprobs

Log probability information for the choice.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `content`                                                          | List[[models.DataContent](../models/datacontent.md)]               | :heavy_check_mark:                                                 | A list of message content tokens with log probability information. |
| `refusal`                                                          | List[[models.Refusal](../models/refusal.md)]                       | :heavy_check_mark:                                                 | A list of message refusal tokens with log probability information. |