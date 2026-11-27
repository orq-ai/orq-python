# Live

## Overview

### Available Operations

* [create_session](#create_session) - Create a Live WebRTC session

## create_session

Exchanges a WebRTC SDP offer for an answer and starts a GPT-Live session. Apply the returned answer to the peer connection and send Live events over the data channel. Requires an API key with `realtime.execute`.

Voice usage is billed by the second at the active or standby rate. Set `wake_policy.type` to `speech` to start inference on speech. Set `idle_timeout_s` to return the session to standby after inactivity. Use client delegation to run backend work in your application.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-live-session" method="post" path="/v3/router/live/sessions" example="standby" -->
```python
import orq_ai_sdk
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.live.create_session(session=orq_ai_sdk.Session(
        idle_timeout_s=15,
        model="openai/gpt-live-1.1",
        wake_policy=orq_ai_sdk.WakePolicy(
            type="speech",
        ),
    ), transport={
        "sdp": "<SDP offer>",
        "type": "webrtc",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session`                                                           | [models.Session](../../models/session.md)                           | :heavy_check_mark:                                                  | N/A                                                                 |
| `transport`                                                         | [models.Transport](../../models/transport.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateLiveSessionResponseBody](../../models/createlivesessionresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.CreateLiveSessionLiveResponseBody            | 400                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponseResponseBody    | 401                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse402ResponseBody | 402                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse403ResponseBody | 403                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse404ResponseBody | 404                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse429ResponseBody | 429                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse502ResponseBody | 502                                                 | application/json                                    |
| models.CreateLiveSessionLiveResponse503ResponseBody | 503                                                 | application/json                                    |
| models.APIDefaultError                              | 4XX, 5XX                                            | \*/\*                                               |