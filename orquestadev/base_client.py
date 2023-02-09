import requests


class BaseClient(object):
    def __init__(self, token, ttl):
        from version import __version__

        self.token = token
        self.ttl = ttl
        self.version = __version__

    @property
    def headers(self):
        return {
            "Authorization": "{}".format(self.token),
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "orquestadev/{};python".format(self.version),
        }

    def query(self, rule_key, default_value, context={}):

        try:
            response = self._perform_request({"rule_key": rule_key, "context": context})

            result = response.json()

            print(result)

            if result.get("status_code", None) is not None:
                return default_value

            return result[rule_key]

        except requests.exceptions.HTTPError as e:
            return default_value

    def _perform_request(self, data):
        return requests.post(
            "http://api.orquesta.dev/evaluate/", headers=self.headers, json=data
        )
