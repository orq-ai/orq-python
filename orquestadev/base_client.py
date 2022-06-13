from collections import defaultdict

import requests


class BaseClient(object):
    def __init__(self, token, ttl):
        from version import __version__
        self.token = token
        self.ttl = ttl
        self.version = __version__
        self._rules_cache = defaultdict(dict)
        self._domain_cache = defaultdict(dict)

    @property
    def headers(self):
        return {
            'Authorization': '{}'.format(self.token),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "User-Agent": 'orquestadev/{};python'.format(self.version),
        }

    def query(self, rule_key, default_value, context={}, store_in_cache=True, **kwargs):
        if self._rules_cache.get(rule_key, None) is not None:
            return self._rules_cache[rule_key]

        try:
            response = self._perform_request({
                'rule_key': rule_key,
                'context': context
            })

            result = response.json()

            if result.get('status_code', None) is not None:
                return default_value

            if store_in_cache:
                self._rules_cache[rule_key] = result[rule_key]

            return result[rule_key]

        except requests.exceptions.HTTPError as e:
            return default_value

    def query_domain(self, domain, context={}, store_in_cache=True, **kwargs):
        if self._domain_cache.get(domain, None) is not None:
            return self._domain_cache[domain]

        try:
            response = self._perform_request({
                'domain': domain,
                'context': context
            })

            result = response.json()

            if result.get('status_code', None) is not None:
                return defaultdict(dict)

            if store_in_cache:
                self._domain_cache[domain] = result

            return result

        except requests.exceptions.HTTPError as e:
            return defaultdict(dict)

    def _perform_request(self, data):
        return requests.post('http://localhost:8000/evaluate/', headers=self.headers, json=data)
