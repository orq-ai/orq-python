<<<<<<< HEAD
from orquesta_sdk.helpers import orquesta_openai_parameters_mapper

import os

from orquesta_sdk import OrquestaClient, OrquestaClientOptions
from orquesta_sdk.prompts import OrquestaPromptRequest
from orquesta_sdk.remoteconfigs import OrquestaRemoteConfigRequest

api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")
=======
import os

from orquesta_sdk import OrquestaClient, OrquestaClientOptions
from orquesta_sdk.endpoints import OrquestaEndpoint, OrquestaEndpointRequest
from orquesta_sdk.exceptions import OrquestaException

api_key = os.environ.get(
    "ORQUESTA_API_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6IjhkMjZjODdkLTU1YzUtNDM0My1hYmI0LWM0YTAxYjFhNDVhMSIsImlhdCI6MTY5Nzk3NzgyMDE3M30.01jUpko1fW5mP7rlvME7NfEnrDocfSm7UWNSaE8iEZY",
)
>>>>>>> 113e75d ( cd /Users/tony/Projects/orquesta/orquesta-python ; /usr/bin/env /Users/tony/Projects/orquesta/orquesta-python/venv/bin/python /Users/tony/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 51707 -- /Users/tony/Projects/orquesta/orquesta-python/cases.py)

options = OrquestaClientOptions(api_key=api_key, ttl=3600, environment="production")

client = OrquestaClient(options)

<<<<<<< HEAD
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
=======
request = OrquestaEndpointRequest(
    key="chat-multimodel",
)


stream_generator = client.endpoints.stream(request)

try:
    for chunk in stream_generator:
        print("Received data:", chunk.content)
except OrquestaException as e:
    print("Error:", e)
except Exception as e:
    print("Error:", e)
>>>>>>> 113e75d ( cd /Users/tony/Projects/orquesta/orquesta-python ; /usr/bin/env /Users/tony/Projects/orquesta/orquesta-python/venv/bin/python /Users/tony/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 51707 -- /Users/tony/Projects/orquesta/orquesta-python/cases.py)
