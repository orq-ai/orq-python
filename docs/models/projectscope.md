# ProjectScope

Project authorization scope. Single-project or all-projects.
 Multi-project use cases are served by minting per-project keys or by
 using an all-projects key with `restricted` mode.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `all`                                                        | [Optional[models.AllProjects]](../models/allprojects.md)     | :heavy_minus_sign:                                           | N/A                                                          |
| `single`                                                     | [Optional[models.SingleProject]](../models/singleproject.md) | :heavy_minus_sign:                                           | N/A                                                          |