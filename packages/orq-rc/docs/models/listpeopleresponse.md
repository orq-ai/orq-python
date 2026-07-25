# ListPeopleResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `object`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | Object discriminator for list responses; always `list`.                  |
| `data`                                                                   | List[[models.Person](../models/person.md)]                               | :heavy_check_mark:                                                       | Page of people, ordered newest first.                                    |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether more people are available in the selected pagination<br/> direction. |