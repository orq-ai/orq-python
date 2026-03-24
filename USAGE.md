<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.post_v2_feedback()

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

        res = await orq.post_v2_feedback_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->