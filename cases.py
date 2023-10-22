import os
from orquesta_sdk import OrquestaClient, OrquestaClientOptions

api_key = os.environ.get("ORQUESTA_API_KEY",
                         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6IjhkMjZjODdkLTU1YzUtNDM0My1hYmI0LWM0YTAxYjFhNDVhMSIsImlhdCI6MTY5NzU3NTYzMTE5N30.By3LONyOaIaIXxVEApJQJhHmQMPCUdBVJtI088SZz6Q")

options = OrquestaClientOptions(
    api_key=api_key
)

client = OrquestaClient(options)

from orquesta_sdk.endpoints import OrquestaEndpointRequest

request = OrquestaEndpointRequest(
    key="chat-multimodel",
    context={
        "user-segment": [],
        "environments": [],
        "user-role": [],
        "countries": []
    },
    metadata={"custom-field-name": "custom-metadata-value"}
)

stream = client.endpoints.stream(
    request
)


def handle_next(chunk):
    print(f"Received {chunk.content}")


def handle_error(e):
    print(f"Error Occurred: {e}")


def handle_completed():
    print("Done!")


stream.subscribe(
    on_next=handle_next,
    on_error=handle_error,
    on_completed=handle_completed,
)
