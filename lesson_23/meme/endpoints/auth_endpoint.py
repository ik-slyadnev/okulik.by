import requests
from endpoints.endpoints_handler import Endpoint


class AuthEndpoint(Endpoint):
    token = None

    def authorize(self, name):
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json={'name': name}
        )
        self.status = response.status_code
        if self.status == 200:
            self.token = response.json()['token']
        return response

    def check_token(self):
        response = requests.get(f'http://167.172.172.115:52355/authorize/{self.token}')
        self.status = response.status_code
        return response

    def check_token_is_not_empty(self):
        assert self.token is not None and len(self.token) > 0
