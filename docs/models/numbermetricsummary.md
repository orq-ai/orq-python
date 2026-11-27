# NumberMetricSummary

Statistics of a numeric metric.


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `min`                          | *Optional[float]*              | :heavy_minus_sign:             | Lowest value.                  |
| `max`                          | *Optional[float]*              | :heavy_minus_sign:             | Highest value.                 |
| `avg`                          | *Optional[float]*              | :heavy_minus_sign:             | Average value.                 |
| `sum`                          | *Optional[float]*              | :heavy_minus_sign:             | Sum of the values.             |
| `median`                       | *Optional[float]*              | :heavy_minus_sign:             | Approximate median.            |
| `range`                        | *Optional[float]*              | :heavy_minus_sign:             | `max` minus `min`.             |
| `std_dev`                      | *Optional[float]*              | :heavy_minus_sign:             | Population standard deviation. |
| `count`                        | *Optional[int]*                | :heavy_minus_sign:             | Number of rows with a value.   |