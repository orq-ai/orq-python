# ListCapabilitiesResponse


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `domains`                                                                                      | List[[models.Domain](../models/domain.md)]                                                     | :heavy_minus_sign:                                                                             | Full capability catalog. Order is stable: workspace-admin first,<br/> then platform, then gateway. |