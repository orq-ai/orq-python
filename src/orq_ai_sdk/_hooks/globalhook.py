from typing import Union
from .types import BeforeRequestContext, BeforeRequestHook

import json
import httpx


class GlobalHook(BeforeRequestHook):
    def before_request(self, hook_ctx: BeforeRequestContext, request: httpx.Request) -> Union[httpx.Request, Exception]:
        contact_id = request.headers['contactid'] if 'contactid' in request.headers else None

        if contact_id:
            del request.headers['contactid']
            request.headers['X-ORQ-CONTACT-ID'] = contact_id

        environment = request.headers['environment'] if 'environment' in request.headers else None

        if hook_ctx.operation_id in ["DeploymentInvoke", "DeploymentStream", "DeploymentGetConfig"]:
            
            raw_payload = request.content.decode('utf-8')
            payload = json.loads(raw_payload)

            if hook_ctx.operation_id == 'DeploymentStream':
                payload['stream'] = True
            else:
                payload['stream'] = False

            if environment:
                del request.headers['environment']
                if 'context' in payload and isinstance(payload['context'], dict):
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
