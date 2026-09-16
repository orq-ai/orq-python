<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.deployments.invoke(key="<key>", stream=False, identity={
        "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
        "display_name": "Jane Doe",
        "email": "jane.doe@example.com",
        "metadata": [
            {
                "department": "Engineering",
                "role": "Senior Developer",
            },
        ],
        "logo_url": "https://example.com/avatars/jane-doe.jpg",
        "tags": [
            "hr",
            "engineering",
        ],
    }, documents=[
        {
            "text": "The refund policy allows customers to return items within 30 days of purchase for a full refund.",
            "metadata": {
                "file_name": "refund_policy.pdf",
                "file_type": "application/pdf",
                "page_number": 1.0,
            },
        },
        {
            "text": "Premium members receive free shipping on all orders over $50.",
            "metadata": {
                "file_name": "membership_benefits.md",
                "file_type": "text/markdown",
            },
        },
    ])

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

        res = await orq.deployments.invoke_async(key="<key>", stream=False, identity={
            "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "display_name": "Jane Doe",
            "email": "jane.doe@example.com",
            "metadata": [
                {
                    "department": "Engineering",
                    "role": "Senior Developer",
                },
            ],
            "logo_url": "https://example.com/avatars/jane-doe.jpg",
            "tags": [
                "hr",
                "engineering",
            ],
        }, documents=[
            {
                "text": "The refund policy allows customers to return items within 30 days of purchase for a full refund.",
                "metadata": {
                    "file_name": "refund_policy.pdf",
                    "file_type": "application/pdf",
                    "page_number": 1.0,
                },
            },
            {
                "text": "Premium members receive free shipping on all orders over $50.",
                "metadata": {
                    "file_name": "membership_benefits.md",
                    "file_type": "text/markdown",
                },
            },
        ])

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->