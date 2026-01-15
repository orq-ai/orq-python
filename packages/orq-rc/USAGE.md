<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.create(field="rating", value=[
        "good",
    ], trace_id="67HTZ65Z9W91HSF51CW68KK1QH")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from orq_ai_sdk import Orq
import os

async def main():

    async with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as orq:

        res = await orq.feedback.create_async(field="rating", value=[
            "good",
        ], trace_id="67HTZ65Z9W91HSF51CW68KK1QH")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->