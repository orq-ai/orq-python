import sys
import os

from orq_ai_sdk import OrqAI, AsyncOrqAI
from orq_ai_sdk.messages import UserMessage


def main():

    client = OrqAI(
        api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6ImRkOWQ0ZTcxLTYyMzEtNDg3Ny1iYzY5LWE2YjA4MzU0NmYwYSIsImlhdCI6MTY5Nzk3MDU1MjUxOH0.2MsRZGdK78qA4axKbR0sqacVzPVPQiAFwIQGCCjZKBE",
        environment="production",
    )

    generation = client.deployments.invoke(
        key="20240503-1523_x7qu_58", messages=[UserMessage(content="I need help")]
    )

    client.feedback.report(property="rating", value=["bad"], trace_id=generation.id)


# asyncio.run(main())
main()
