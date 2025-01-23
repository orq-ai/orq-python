"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from orq_ai_sdk import models, utils
from orq_ai_sdk._hooks import HookContext
from orq_ai_sdk.types import OptionalNullable, UNSET
from orq_ai_sdk.utils import get_security_from_env
from typing import Any, Dict, List, Mapping, Optional, Union


class Metrics(BaseSDK):
    def create(
        self,
        *,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        usage: Optional[Union[models.Usage, models.UsageTypedDict]] = None,
        performance: Optional[
            Union[models.Performance, models.PerformanceTypedDict]
        ] = None,
        messages: Optional[
            Union[
                List[models.DeploymentCreateMetricMessages],
                List[models.DeploymentCreateMetricMessagesTypedDict],
            ]
        ] = None,
        choices: Optional[
            Union[List[models.Choices], List[models.ChoicesTypedDict]]
        ] = None,
        feedback: Optional[
            Union[
                models.DeploymentCreateMetricFeedback,
                models.DeploymentCreateMetricFeedbackTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.DeploymentCreateMetricResponseBody]:
        r"""Add metrics

        Add metrics to a deployment

        :param id: Deployment ID
        :param metadata: Your own custom key-value pairs can be attached to the logs. This is useful for storing additional information related to your interactions with the LLM providers or specifics within your application.
        :param usage: Usage statistics to add to the deployment
        :param performance:
        :param messages: A list of messages sent to the model.
        :param choices: A list of completion choices. If you are using a `completion` model then you must provide the `completion content` with the chat completion format
        :param feedback: Feedback from the user on the completion
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if timeout_ms is None:
            timeout_ms = 600000

        if server_url is not None:
            base_url = server_url

        request = models.DeploymentCreateMetricRequest(
            id=id,
            request_body=models.DeploymentCreateMetricRequestBody(
                metadata=metadata,
                usage=utils.get_pydantic_model(usage, Optional[models.Usage]),
                performance=utils.get_pydantic_model(
                    performance, Optional[models.Performance]
                ),
                messages=utils.get_pydantic_model(
                    messages, Optional[List[models.DeploymentCreateMetricMessages]]
                ),
                choices=utils.get_pydantic_model(
                    choices, Optional[List[models.Choices]]
                ),
                feedback=utils.get_pydantic_model(
                    feedback, Optional[models.DeploymentCreateMetricFeedback]
                ),
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v2/deployments/{id}/metrics",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.DeploymentCreateMetricRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="DeploymentCreateMetric",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.DeploymentCreateMetricResponseBody]
            )
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        usage: Optional[Union[models.Usage, models.UsageTypedDict]] = None,
        performance: Optional[
            Union[models.Performance, models.PerformanceTypedDict]
        ] = None,
        messages: Optional[
            Union[
                List[models.DeploymentCreateMetricMessages],
                List[models.DeploymentCreateMetricMessagesTypedDict],
            ]
        ] = None,
        choices: Optional[
            Union[List[models.Choices], List[models.ChoicesTypedDict]]
        ] = None,
        feedback: Optional[
            Union[
                models.DeploymentCreateMetricFeedback,
                models.DeploymentCreateMetricFeedbackTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.DeploymentCreateMetricResponseBody]:
        r"""Add metrics

        Add metrics to a deployment

        :param id: Deployment ID
        :param metadata: Your own custom key-value pairs can be attached to the logs. This is useful for storing additional information related to your interactions with the LLM providers or specifics within your application.
        :param usage: Usage statistics to add to the deployment
        :param performance:
        :param messages: A list of messages sent to the model.
        :param choices: A list of completion choices. If you are using a `completion` model then you must provide the `completion content` with the chat completion format
        :param feedback: Feedback from the user on the completion
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if timeout_ms is None:
            timeout_ms = 600000

        if server_url is not None:
            base_url = server_url

        request = models.DeploymentCreateMetricRequest(
            id=id,
            request_body=models.DeploymentCreateMetricRequestBody(
                metadata=metadata,
                usage=utils.get_pydantic_model(usage, Optional[models.Usage]),
                performance=utils.get_pydantic_model(
                    performance, Optional[models.Performance]
                ),
                messages=utils.get_pydantic_model(
                    messages, Optional[List[models.DeploymentCreateMetricMessages]]
                ),
                choices=utils.get_pydantic_model(
                    choices, Optional[List[models.Choices]]
                ),
                feedback=utils.get_pydantic_model(
                    feedback, Optional[models.DeploymentCreateMetricFeedback]
                ),
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v2/deployments/{id}/metrics",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.DeploymentCreateMetricRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="DeploymentCreateMetric",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.DeploymentCreateMetricResponseBody]
            )
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
