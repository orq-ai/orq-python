from typing import Dict, Any, Union

from pydantic import BaseModel

from orq_ai_sdk.constants import BASE_URL
from orq_ai_sdk.http_client import post, post_async

CONTACTS_API = '{}{}'.format(BASE_URL, '/v2/contacts')


class Contact(BaseModel):
    id: str
    external_id: str
    display_name: Union[str, None] = None
    email: Union[str, None] = None
    avatar_url: Union[str, None] = None
    metadata: Dict[str, Any] = dict


class Contacts:
    def create(
            self,
            external_id: str,
            display_name: None,
            email: None,
            avatar_url: None,
            metadata=None
    ):
        """
        Attributes:
        :param external_id: An external identifier for the user
        :param display_name: The user's display name or full name
        :param email: The user's email address (validated format)
        :param avatar_url: URL to the user's avatar image (validated URL format)
        :param metadata: Additional key-value pairs for storing extra contact information
        :return:
        """

        if not external_id:
            raise ValueError("External ID is required.")

        response = post(
            url=CONTACTS_API,
            body={
                "external_id": external_id,
                "display_name": display_name,
                "email": email,
                "avatar_url": avatar_url,
                "metadata": metadata
            }
        )

        response.raise_for_status()

        return Contact(**response.json())

    async def acreate(
            self,
            external_id: str,
            display_name: None,
            email: None,
            avatar_url: None,
            metadata=dict
    ):
        """
        Attributes:
        :param external_id: An external identifier for the user
        :param display_name: The user's display name or full name
        :param email: The user's email address (validated format)
        :param avatar_url: URL to the user's avatar image (validated URL format)
        :param metadata: Additional key-value pairs for storing extra contact information
        :return:
        """

        if not external_id:
            raise ValueError("External ID is required.")

        response = await post_async(
            url=CONTACTS_API,
            body={
                "external_id": external_id,
                "display_name": display_name,
                "email": email,
                "avatar_url": avatar_url,
                "metadata": metadata
            }
        )

        response.raise_for_status()

        return Contact(**response.json())
