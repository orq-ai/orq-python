import httpx

from orq_ai_sdk.models import Store
from .version import VERSION


def build_headers():
    headers = {
        "X-SDK-Version": "@orq.ai/python@{}".format(VERSION),
        "Authorization": "Bearer {}".format(Store["api_key"]),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "orq.ai/{};python".format(VERSION),
    }

    contact_id = Store.get("contact_id")

    if contact_id is not None:
        headers["X-Orq-Contact-Id"] = str(contact_id)

    return headers


def build_body(environment, body):
    if environment:
        if body.get("context", None) is None:
            body["context"] = {"environments": [environment]}
        elif body["context"].get("environments", None) is None:
            body["context"]["environments"] = [environment]
    return body


def post(url: str, body: dict, environment=None):
    headers = build_headers()
    body = build_body(environment, body)
    return httpx.post(url, json=body, headers=headers, timeout=300)


def stream(url: str, body: dict, environment=None):
    headers = build_headers()
    body = build_body(environment, body)
    headers["Accept"] = "text/event-stream"
    body["stream"] = True
    buffer = b""
    with httpx.stream("POST", url, json=body, headers=headers, timeout=300) as response:
        for chunk in response.iter_bytes():
            buffer += chunk
            while b"\n\n" in buffer:
                event, buffer = buffer.split(b"\n\n", 1)
                yield event


async def post_async(url: str, body: dict, environment=None):
    headers = build_headers()
    body = build_body(environment, body)

    async with httpx.AsyncClient(timeout=300) as client:
        return await client.post(url, json=body, headers=headers)


async def stream_async(url: str, body: dict, environment=None):
    headers = build_headers()
    body = build_body(environment, body)
    headers["Accept"] = "text/event-stream"
    body["stream"] = True
    buffer = b""
    async with httpx.AsyncClient(timeout=300) as client:
        async with client.stream("POST", url, json=body, headers=headers) as response:
            async for chunk in response.aiter_bytes():
                buffer += chunk
                while b"\n\n" in buffer:
                    event, buffer = buffer.split(b"\n\n", 1)
                    yield event
