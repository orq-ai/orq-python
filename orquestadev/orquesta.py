import os

from base_client import BaseClient
from utils import is_invalid_api_key


class OrquestaIncorrectAPIException(BaseException):
    pass


class OrquestaClient(BaseClient):
    def __init__(self, api_key, ttl=3600):
        """
        Construct the Orquesta API object.
        Note that the underlying client is set up during initialization,
        therefore changing attributes will not change client behavior.

        :param api_key: Orquesta workspace API key to use. If not provided, value
                        will be read from environment variable "ORQUESTA_API_KEY".
        :type api_key: string
        :param ttl: Time to live for the rules in the cache. Default = 3600 seconds.
        :type ttl: int
        """
        self.api_key = api_key or os.environ.get("ORQUESTA_API_KEY")

        if not self.api_key or is_invalid_api_key(self.api_key):
            raise OrquestaIncorrectAPIException("API key is not valid")

        auth = "Bearer {}".format(self.api_key)
        super(OrquestaClient, self).__init__(auth, ttl)
