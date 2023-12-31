import requests

from .version import VERSION

PROMPTS_API = "https://api.orquesta.cloud/v1/prompts"
REMOTE_CONFIGS_API = "https://api.orquesta.cloud/v1/remoteconfigs"
ENDPOINTS_API = "https://api.orquesta.cloud/v1/endpoints"
METRICS_API = "https://api.orquesta.cloud/v1/metrics"


def post(url: str, api_key: str, body: dict, stream=False, environment=None):
    headers = {
        "X-SDK-Version": "@orquesta/python@{}".format(VERSION),
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "orquesta/{};python".format(VERSION),
    }

    if environment:
        if body.get("context", None) is None:
            body["context"] = {"environments": [environment]}
        else:
            body["context"]["environments"] = [environment]

    if stream:
        headers["Accept"] = "text/event-stream"
        body["stream"] = True
        return requests.post(url, json=body, headers=headers, stream=True)

    return requests.post(url, json=body, headers=headers)
