import requests

from .version import __version__

PROMPTS_API = "https://api.orquesta.cloud/v1/prompts"
REMOTE_CONFIGS_API = "https://api.orquesta.cloud/v1/remoteconfigs"
ENDPOINTS_API = "https://api.orquesta.cloud/v1/endpoints"
METRICS_API = "https://api.orquesta.cloud/v1/metrics"


def post(url: str, api_key: str, body: dict, stream=False):
    headers = {
        "X-SDK-Version": "@orquesta/python@{}".format(__version__),
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "orquesta/{};python".format(__version__),
    }

    if stream:
        headers["Accept"] = "text/event-stream"
        body["stream"] = True

    response = requests.post(url, json=body, headers=headers)
    return response
