from typing import Any, Coroutine, List, Literal, Union

from httpx import Response
from pydantic import BaseModel

from orq_ai_sdk.constants import BASE_URL
from orq_ai_sdk.http_client import post, post_async

FEEDBACK_POST = "/v2/feedback"


class FeedbackReport(BaseModel):
    property: str
    value: List[str]
    trace_id: str


class FeedbackResponse(BaseModel):
    id: str
    product: str
    property: str
    trace_id: str
    value: List[str]


class FeedbackCorrectionResponse(BaseModel):
    id: str
    product: str
    property: str = "correction"
    trace_id: str
    value: str


class FeedbackCorrection(BaseModel):
    property: Literal["correction"]
    value: str
    trace_id: str


FeedbackData = Union[FeedbackReport, FeedbackCorrection]


class Feedback:
    def __create_feedback_request(self, data: FeedbackData):
        return post(
            url="{}/{}".format(BASE_URL, FEEDBACK_POST),
            body=data.model_dump(),
        )

    def __acreate_feedback_request(
        self, data: FeedbackData
    ) -> Coroutine[Any, Any, Response]:
        return post_async(
            url="{}/{}".format(BASE_URL, FEEDBACK_POST),
            data=data.model_dump(),
        )

    def report(
        self, property: str, value: List[str], trace_id: str
    ) -> FeedbackResponse:
        report = FeedbackReport(property=property, value=value, trace_id=trace_id)
        response = self.__create_feedback_request(report)
        return FeedbackResponse(**response.json())

    async def areport(
        self, property: str, value: List[str], trace_id: str
    ) -> FeedbackResponse:
        report = FeedbackReport(property=property, value=value, trace_id=trace_id)
        response = self.__acreate_feedback_request(report)
        return FeedbackResponse(**await response.json())

    def correct(self, correction: str, trace_id: str) -> FeedbackCorrectionResponse:
        correction_payload = FeedbackReport(
            property="correction",
            value=correction,
            trace_id=trace_id,
        )
        response = self.__create_feedback_request(correction_payload)
        return FeedbackCorrectionResponse(**response.json())

    async def acorrect(
        self, correction: str, trace_id: str
    ) -> FeedbackCorrectionResponse:
        correction_payload = FeedbackReport(
            property="correction",
            value=correction,
            trace_id=trace_id,
        )
        response = await self.__acreate_feedback_request(correction_payload)
        return FeedbackCorrectionResponse(await response.json())
