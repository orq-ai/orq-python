<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    assert res is not None

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

        res = await orq.contacts.create_async(request={
            "external_id": "user_12345",
            "display_name": "Jane Smith",
            "email": "jane.smith@example.com",
            "avatar_url": "https://example.com/avatars/jane-smith.jpg",
            "tags": [
                "premium",
                "beta-user",
                "enterprise",
            ],
            "metadata": {
                "department": "Engineering",
                "role": "Senior Developer",
                "subscription_tier": "premium",
                "last_login": "2024-01-15T10:30:00Z",
            },
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->