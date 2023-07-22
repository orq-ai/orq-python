import requests

from .version import __version__

API_URL = "https://api.orquesta.dev/v2"
PROMPTS_URL = f"{API_URL}/prompts"
REMOTE_CONFIGS_URL = f"{API_URL}/remoteconfigs"


def post(
        url: str,
        api_key: str,
        body: dict
):
    headers = {
        "X-SDK-Version": "@orquesta/python@{}".format(__version__),
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "orquesta/{};python".format(__version__),
    }

    response = requests.post(url, json=body, headers=headers)
    return response
