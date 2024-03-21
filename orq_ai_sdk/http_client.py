import httpx

from .version import VERSION


def build_headers(api_key: str):
    return {
        "X-SDK-Version": "@orq.ai/python@{}".format(VERSION),
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "orq.ai/{};python".format(VERSION),
    }


def build_body(environment, body):
    if environment:
        if body.get("context", None) is None:
            body["context"] = {"environments": [environment]}
        else:
            body["context"]["environments"] = [environment]
    return body


def post(url: str, api_key: str, body: dict, environment=None):
    headers = build_headers(api_key)
    body = build_body(environment, body)
    return httpx.post(url, json=body, headers=headers, timeout=300)


def stream(url: str, api_key: str, body: dict, environment=None):
    headers = build_headers(api_key)
    body = build_body(environment, body)
    headers["Accept"] = "text/event-stream"
    body["stream"] = True
    with httpx.stream("POST", url, json=body, headers=headers, timeout=300) as response:
        for chunk in response.iter_bytes():
            yield chunk


async def post_async(url: str, api_key: str, body: dict, environment=None):
    headers = build_headers(api_key)
    body = build_body(environment, body)

    async with httpx.AsyncClient(timeout=300) as client:
        return await client.post(url, json=body, headers=headers)


async def stream_async(url: str, api_key: str, body: dict, environment=None):
    headers = build_headers(api_key)
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
