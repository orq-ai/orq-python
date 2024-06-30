from typing import Optional

from orq_ai_sdk.api_resources.async_deployments import Deployment as AsyncDeployment
from orq_ai_sdk.api_resources.deployments import Deployment
from orq_ai_sdk.api_resources.feedback.feedback import Feedback
from orq_ai_sdk.exceptions import OrqAIInvalidAPIException
from orq_ai_sdk.models import Store


class OrqAI:
    """
    The OrqAI class represents the main client for interacting with the orq.ai SDK.

    Args:
        api_key (str): The API key used for authentication.
        environment (str, optional): The environment to use for the SDK.

    Attributes:
        deployments: An instance of the Deployments class.

    Methods:
        set_user: Sets the user information.

    Raises:
        OrqInvalidAPIException: If the provided API key is invalid.
    """

    def __init__(self, api_key: str, environment: Optional[str] = None):
        """
        Initializes a new instance of the OrqAI class.

        Args:
            api_key (str): The API key used for authentication.
            environment (str, optional): The environment to use for the SDK.

        Raises:
            OrqInvalidAPIException: If the provided API key is invalid.
        """

        if api_key is None or len(api_key) == 0:
            raise OrqAIInvalidAPIException("The provided API key is invalid.")

        Store["api_key"] = api_key
        Store["environment"] = environment

    @property
    def deployments(self):
        return Deployment()

    @property
    def feedback(self):
        return Feedback()

    def set_user(self, id=None):
        Store["user_info"] = {"id": id}


class AsyncOrqAI:
    """
    The AsyncOrqAI class represents the main client for interacting with the orq.ai SDK.

    Args:
        api_key (str): The API key used for authentication.
        environment (str, optional): The environment to use for the SDK.

    Attributes:
        deployments: An instance of the Deployments class.

    Methods:
        set_user: Sets the user information.

    Raises:
        OrqInvalidAPIException: If the provided API key is invalid.
    """

    def __init__(self, api_key: str, environment: Optional[str] = None):
        """
        Initializes a new instance of the AsyncOrqAI class.

        Args:
            api_key (str): The API key used for authentication.
            environment (str, optional): The environment to use for the SDK.

        Raises:
            OrqInvalidAPIException: If the provided API key is invalid.
        """

        if api_key is None or len(api_key) == 0:
            raise OrqAIInvalidAPIException("The provided API key is invalid.")

        Store["api_key"] = api_key
        Store["environment"] = environment

    @property
    def deployments(self):
        return AsyncDeployment()

    @property
    def feedback(self):
        return Feedback()

    def set_user(self, id=None):
        Store["user_info"] = {"id": id}
