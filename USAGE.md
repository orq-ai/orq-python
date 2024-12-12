<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from orq_ai_sdk import Orq
import os

async def main():
    async with Orq(
        api_key=os.getenv("ORQ_API_KEY", ""),
    ) as orq:

        res = await orq.contacts.create_async(external_id="<id>")

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->