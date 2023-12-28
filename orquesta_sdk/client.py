import os

from orquesta_sdk.exceptions import OrquestaInvalidAPIException

from .api_resources.deployments import Deployments
from .options import OrquestaClientOptions


class Orquesta:
    """
    Represents an Orquesta client.

    Args:
        options (OrquestaClientOptions): The options for the Orquesta client.

    Attributes:
        deployments (Deployments): An instance of the Deployments class.

    Raises:
        OrquestaInvalidAPIException: If the provided API key is invalid.
    """

    def __init__(self, options: OrquestaClientOptions):
        api_key = options.api_key or os.environ.get("ORQUESTA_API_KEY")

        if api_key is None or len(api_key) == 0:
            raise OrquestaInvalidAPIException("The provided API key is invalid.")

        self.deployments = Deployments(options=options)
