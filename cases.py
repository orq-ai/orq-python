from orquesta_sdk.helpers import orquesta_openai_parameters_mapper

import os

from orquesta_sdk import OrquestaClient, OrquestaClientOptions
from orquesta_sdk.prompts import OrquestaPromptRequest
from orquesta_sdk.remoteconfigs import OrquestaRemoteConfigRequest

api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")

options = OrquestaClientOptions(api_key=api_key, ttl=3600, environment="production")

client = OrquestaClient(options)

request = OrquestaPromptRequest(
    key="prompt_key",
    context={"environments": "production", "workspaceId": "soql1odAABC2"},
    variables={"firstname": "John", "city": "New York"},
    metadata={"chain_id": "ad1231xsdaABw"},
)

request = OrquestaRemoteConfigRequest(
    key="prompt_key",
    context={"environments": "production", "workspaceId": "soql1odAABC2"},
    metadata={"chain_id": "ad1231xsdaABw"},
)

prompt = client.prompts.query(
    request=request,
)

print(prompt.value)
