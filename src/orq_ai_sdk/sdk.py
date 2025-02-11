"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from orq_ai_sdk import models, utils
from orq_ai_sdk._hooks import SDKHooks
from orq_ai_sdk.contacts import Contacts
from orq_ai_sdk.deployments_sdk import DeploymentsSDK
from orq_ai_sdk.feedback import Feedback
from orq_ai_sdk.files import Files
from orq_ai_sdk.models import internal
from orq_ai_sdk.prompts import Prompts
from orq_ai_sdk.promptsnippets import PromptSnippets
from orq_ai_sdk.remoteconfig import Remoteconfig
from orq_ai_sdk.types import OptionalNullable, UNSET
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref


class Orq(BaseSDK):
    r"""[Dev] orq.ai API: orq.ai API documentation
    https://docs.orq.ai - orq.ai Documentation
    """

    contacts: Contacts
    feedback: Feedback
    deployments: DeploymentsSDK
    files: Files
    prompt_snippets: PromptSnippets
    prompts: Prompts
    remoteconfig: Remoteconfig

    def __init__(
        self,
        api_key: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        contact_id: Optional[str] = None,
        environment: Optional[str] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :param contact_id: Configures the contact_id parameter for all supported operations
        :param environment: Configures the environment parameter for all supported operations
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(api_key):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(api_key=api_key())
        else:
            security = models.Security(api_key=api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        _globals = internal.Globals(
            contact_id=utils.get_global_from_env(contact_id, "ORQ_CONTACT_ID", str),
            environment=utils.get_global_from_env(environment, "ORQ_ENVIRONMENT", str),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                globals=_globals,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.async_client,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.contacts = Contacts(self.sdk_configuration)
        self.feedback = Feedback(self.sdk_configuration)
        self.deployments = DeploymentsSDK(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.prompt_snippets = PromptSnippets(self.sdk_configuration)
        self.prompts = Prompts(self.sdk_configuration)
        self.remoteconfig = Remoteconfig(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()
