from typing import Any, Dict, List

from orquesta_sdk.exceptions import handle_request_exception
from orquesta_sdk.http_client import post
from orquesta_sdk.models import Store
from orquesta_sdk.util import extract_json

DEPLOYMENTS_API = "https://api.orquesta.cloud/v2/deployments"

GET_CONFIG_URL = "{}/get_config".format(DEPLOYMENTS_API)
INVOKE_URL = "{}/invoke".format(DEPLOYMENTS_API)

from typing import Optional, TypedDict


class DeploymentFeedback(TypedDict):
    score: int


class DeploymentUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: Optional[int]


class DeploymentPerformance(TypedDict):
    latency: Optional[float]
    time_to_first_token: Optional[float]


class BaseDeployment:
    def __init__(self, event_id: str):
        if event_id is None:
            raise Exception(
                "Something went wrong while fetching the deployment. Please try again."
            )
        self.id = event_id

    def add_metrics(
            self,
            feedback: Optional[DeploymentFeedback] = None,
            usage: Optional[DeploymentUsage] = None,
            performance: Optional[DeploymentPerformance] = None,
            metadata: Optional[Dict] = None,
            chain_id: Optional[str] = None,
            conversation_id: Optional[str] = None,
            user_id: Optional[str] = None,
            messages: Optional[List[Dict[str, Any]]] = None,
            choices: Optional[List[Dict[str, Any]]] = None,
    ):
        body = {}

        if feedback is not None:
            body["feedback"] = feedback

        if usage is not None:
            body["usage"] = usage

        if performance is not None:
            body["performance"] = performance

        if metadata is not None:
            body["metadata"] = metadata

        if chain_id is not None:
            body["chain_id"] = chain_id

        if conversation_id is not None:
            body["conversation_id"] = conversation_id

        if user_id is not None:
            body["user_id"] = user_id

        if messages is not None:
            body["messages"] = messages

        if choices is not None:
            body["choices"] = choices

        response = post(
            url="{}/{}/metrics".format(DEPLOYMENTS_API, self.id),
            api_key=Store['api_key'],
            body=body,
            environment=Store['environment'],
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)


class DeploymentDataChoice:
    def __init__(self, data: Dict[str, Any]):
        self.index = data.get("index", None)
        self.message = DeploymentDataChoiceMessage(data["message"])
        self.finish_reason = data.get("finish_reason", None)

    def to_dict(self):
        return {
            "index": self.index,
            "message": self.message.to_dict(),
            "finish_reason": self.finish_reason,
        }


class DeploymentDataChoiceMessage:
    def __init__(self, data: Dict[str, Any]):
        self.role = data.get("role")

        if data.get("url") is not None:
            self.url = data["url"]

        if data.get("content") is not None:
            self.content = data["content"]

        if data.get("tool_calls") is not None:
            self.content = data.get("content", None)

            self.tool_calls = [
                DeploymentDataChoiceToolCall(tool_call)
                for tool_call in data.get("tool_calls", [])
            ]

    def to_dict(self):
        value = {}

        if hasattr(self, "role"):
            value["role"] = self.role

        if hasattr(self, "url") and self.url is not None:
            value["url"] = self.url

        if hasattr(self, "content") and self.content is not None:
            value["content"] = self.content

        if hasattr(self, "tool_calls") and self.tool_calls is not None:
            value["tool_calls"] = [tool_call.to_dict() for tool_call in self.tool_calls]

        return value


class DeploymentDataChoiceToolCall:
    def __init__(self, data: Dict[str, Any]):
        self.type = data["type"]
        self.function = ToolCallFunction(data["function"])

    def to_dict(self):
        return {
            "type": self.type,
            "function": self.function.to_dict(),
        }


class ToolCallFunction:
    def __init__(self, data: Dict[str, Any]):
        self.name = data.get("name", None)
        self.arguments = data.get("arguments")

    def to_dict(self):
        value = {}

        if self.name is not None:
            value["name"] = self.name

        if self.arguments is not None:
            value["arguments"] = self.arguments

        return value


class Deployment(BaseDeployment):
    def __init__(
            self,
            **params,
    ):
        super().__init__(event_id=params.get("id"))

        self.id = params.get("id", None)
        self.created = params.get("created", None)
        self.object = params.get("object", None)
        self.model = params.get("model", None)
        self.provider = params.get("provider", None)
        self.is_final = params.get("is_final", None)
        self.finalized = params.get("finalized", None)
        self.system_fingerprint = params.get("system_fingerprint", None)
        self.choices = [
            DeploymentDataChoice(choice) for choice in params.get("choices", [])
        ]

    def to_dict(self):
        """
        Converts the deployment object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the deployment object.

        """
        return {
            "id": self.id,
            "created": self.created,
            "object": self.object,
            "model": self.model,
            "provider": self.provider,
            "is_final": self.is_final,
            "finalized": self.finalized,
            "system_fingerprint": self.system_fingerprint,
            "choices": [choice.to_dict() for choice in self.choices],
        }


class DeploymentConfig(BaseDeployment):
    """
    This class represents the configuration for a deployment.

    Attributes:
        :param provider (str): The model provider of the deployment.
        :param model (str): The model of the deployment.
        :param type (str): The type of the deployment model `chat`, `completion`, etc.
        :param messages (list): The prompt template of the deployment
        :param parameters (dict): The parameters of the deployment model
        :param tools (list, optional): A list of tools configured on the deployment
    """

    def __init__(self, **params):
        """
        Initialize a DeploymentConfig instance.

        Args:
            :param id (str): The id of the transaction. Used by the `add_metrics` method to report metrics.
            :param provider (str): The provider of the deployment.
            :param model (str): The model of the deployment.
            :param type (str): The type of the deployment.
            :param messages (list): The messages of the deployment.
            :param parameters (dict): The parameters of the deployment.
            :param tools (list, optional): The tools of the deployment.
        """
        super().__init__(event_id=params.get("id"))

        self.id = params.get("id", None)
        self.provider = params.get("provider", "")
        self.model = params.get("model", "")
        self.type = params.get("type", "")
        self.messages = params.get("messages", [])
        self.parameters = params.get("parameters", {})
        self.tools = params.get("tools", [])

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the DeploymentConfig instance to a dictionary.

        Returns:
            dict: A dictionary representation of the DeploymentConfig instance.
        """
        deployment_dict = {
            "id": self.id,
            "provider": self.provider,
            "model": self.model,
            "type": self.type,
            "messages": self.messages,
            "parameters": self.parameters,
        }

        if self.tools is not None:
            deployment_dict["tools"] = self.tools

        return deployment_dict


class Deployments:
    body_params = {}

    def __validate_params(
            self,
            key: str,
            context: Optional[Dict[str, Any]] = None,
            inputs: Optional[Dict[str, str]] = None,
            metadata: Optional[Dict[str, Any]] = None,
            chain_id: Optional[str] = None,
            conversation_id: Optional[str] = None,
            messages: Optional[List[Dict[str, Any]]] = None,
    ):
        if key is None:
            raise Exception(
                "The deployment key is required. Please provide a deployment key."
            )

        self.body_params["key"] = key

        if context is not None:
            self.body_params["context"] = context

        if inputs is not None:
            self.body_params["inputs"] = inputs

        if metadata is not None:
            self.body_params["metadata"] = metadata

        if messages is not None:
            self.body_params["messages"] = messages

        if chain_id is not None:
            self.body_params["chain_id"] = chain_id

        if conversation_id is not None:
            self.body_params["conversation_id"] = conversation_id

        user_info = Store.get('user_info')

        if user_info is not None and isinstance(user_info, dict):
            self.body_params["user_id"] = user_info.get("id")

    def get_config(self, key: str, context=None, inputs=None, metadata=None):
        self.__validate_params(
            key=key, context=context, inputs=inputs, metadata=metadata
        )

        response = post(
            url=GET_CONFIG_URL,
            body=self.body_params,
            api_key=Store['api_key'],
            environment=Store['environment'],
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        params = response.json()

        return DeploymentConfig(**params)

    def invoke(
            self,
            key: str,
            context=None,
            inputs=None,
            metadata=None,
            chain_id=None,
            conversation_id=None,
            messages=None,
    ):
        """
        Invokes a deployment with the specified key.

        Args:
            :param key (str): The key of the deployment to invoke.
            :param context (dict, optional): The context to pass to the deployment. Defaults to None.
            :param inputs (dict, optional): The input variables to pass to the deployment. Defaults to None.
            :param metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.
            :param chain_id (str, optional): The chain_id being executed. Defaults to None.
            :param conversation_id (str, optional): The conversation_id being executed. Defaults to None.
            :param messages (list, optional): The messages to send to the LLM with the messages template. Defaults to None.
            :param user_input (str, optional): The user input to send to the LLM. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_params(
            key=key,
            context=context,
            inputs=inputs,
            metadata=metadata,
            chain_id=chain_id,
            conversation_id=conversation_id,
            messages=messages,
        )

        response = post(
            url=INVOKE_URL,
            api_key=Store['api_key'],
            body=self.body_params,
            environment=Store['environment'],
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        params = response.json()

        return Deployment(**params)

    def invoke_with_stream(
            self,
            key: str,
            context=None,
            inputs=None,
            metadata=None,
            chain_id=None,
            conversation_id=None,
            messages=None,
    ):
        """
        Invokes a deployment with the specified key and stream the response.

        Streaming is not supported for model of type `image`.

        Args:
            :param key (str): The key of the deployment to invoke.
            :param context (dict, optional): The context to pass to the deployment. Defaults to None.
            :param inputs (dict, optional): The input variables to pass to the deployment. Defaults to None.
            :param metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.
            :param chain_id (str, optional): The chain_id being executed. Defaults to None.
            :param conversation_id (str, optional): The conversation_id being executed. Defaults to None.
            :param messages (list, optional): The messages to send to the LLM with the template. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_params(
            key=key,
            context=context,
            inputs=inputs,
            metadata=metadata,
            chain_id=chain_id,
            conversation_id=conversation_id,
            messages=messages,
        )

        response = post(
            url=INVOKE_URL,
            api_key=Store['api_key'],
            body=self.body_params,
            stream=True,
            environment=Store['environment'],
        )

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        for line in response.iter_lines():
            if line:
                data = extract_json(line)

                if data:
                    for item in data:
                        yield Deployment(**item)
