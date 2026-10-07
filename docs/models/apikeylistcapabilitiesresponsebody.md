# APIKeyListCapabilitiesResponseBody

The capability catalog


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `domains`                                                                                     | List[[models.Domain](../models/domain.md)]                                                    | :heavy_check_mark:                                                                            | Full capability catalog. Order is stable: workspace-admin first, then platform, then gateway. |