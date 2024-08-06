# Webhooks

### Webhook validation

> [!WARNING]  
> We do require the raw body of the request to perform signature verification. If you are using a framework, make sure
> it doesn't manipulate the raw body. Any manipulation to the raw body of the request causes the verification fail.

```python


from fastapi import Request, FastAPI

import orq_ai_sdk.exceptions

webhook_secret = 'orq_wk_...'

app = FastAPI()


@app.post("/webhooks")
async def get_body(request: Request):
    request_body = await request.json()
    signature = request.headers.get("X-Orq-Signature")
    event = None

    try:
        event = client.webhooks.construct_event(
            request_body,
            signature,
            webhook_secret
        )
    except ValueError as e:
        # Invalid request body
        print('Error parsing payload: {}'.format(str(e)))
    except orq_ai_sdk.exceptions.SignatureVerificationException as e:
        # Invalid signature
        print('Error verifying webhook signature: {}'.format(str(e)))

    if event['type'] == 'deployment.invoked':
        from orq_ai_sdk.api_resources.webhooks import WebhookDeploymentInvokedEvent
        
        invoked_event = WebhookDeploymentInvokedEvent.model_validate(event['data'])
        print('Deployment invoked: {}'.format(invoked_event))







```
