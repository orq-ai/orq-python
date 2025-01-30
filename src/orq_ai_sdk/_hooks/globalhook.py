from .types import BeforeRequestContext, BeforeRequestHook

import json
import httpx


class GlobalHook(BeforeRequestHook):
    def before_request(self, hook_ctx: BeforeRequestContext, request: httpx.Request) -> Union[requests.PreparedRequest, Exception]:
        contact_id = request.headers['contactId']

        if contact_id:
            del request.headers['contactId']
            request.headers['X-ORQ-CONTACT-ID'] = contact_id

        environment = request.headers['environment']

        if hook_ctx.operation_id in ["DeploymentInvoke", "DeploymentStream"] and environment:
            del request.headers['environment']
            raw_payload = request.content.decode('utf-8')
            payload = json.loads(raw_payload)

            if 'context' in payload and type(payload['context']) is dict:
                payload['context']['environments'] = environment
            else:
                payload['context'] = {
                    'environments': environment
                }

            data = json.dumps(payload).encode('utf-8')

            # solve error related to Too much declared Content-Length (will not be dynamically set if its also pass in the init below for httpx.Request)
            del request.headers['Content-Length']

            return httpx.Request(method=request.method, url=request.url, extensions=request.extensions, headers=request.headers, content=data)

        return request