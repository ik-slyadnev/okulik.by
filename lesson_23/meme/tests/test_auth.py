import pytest


class TestAuth:
    def test_authorize_success(self, auth_endpoint):
        auth_endpoint.authorize('test_user')
        auth_endpoint.check_response_status_is_ok()
        auth_endpoint.check_token_is_not_empty()

    def test_check_token_valid(self, auth_endpoint, auth_token):
        auth_endpoint.token = auth_token
        auth_endpoint.check_token()
        auth_endpoint.check_response_status_is_ok()

    def test_check_token_invalid(self, auth_endpoint):
        auth_endpoint.token = 'invalid_token'
        auth_endpoint.check_token()
        assert auth_endpoint.status == 404
