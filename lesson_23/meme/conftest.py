import pytest
from endpoints.auth_endpoint import AuthEndpoint
from endpoints.meme_endpoint import MemeEndpoint


@pytest.fixture(scope='session')
def auth_endpoint():
    return AuthEndpoint()


@pytest.fixture(scope='session')
def meme_endpoint():
    return MemeEndpoint()


@pytest.fixture(scope='session')
def auth_token(auth_endpoint):
    # Попытка авторизации с использованием ранее сохраненного токена
    try:
        with open('token.txt', 'r') as file:
            token = file.read().strip()
            auth_endpoint.token = token
            response = auth_endpoint.check_token()
            if response.status_code == 200:
                return token
    except FileNotFoundError:
        pass

    # Если ранее сохраненный токен не работает, выполняем новую авторизацию
    auth_endpoint.authorize('test_user')
    auth_endpoint.check_response_status_is_ok()
    auth_endpoint.check_token_is_not_empty()
    token = auth_endpoint.token

    # Сохраняем новый токен в файл
    with open('token.txt', 'w') as file:
        file.write(token)

    return token


@pytest.fixture()
def create_meme(meme_endpoint, auth_token):
    text = "Test meme cats"
    url = "https://images.app.goo.gl/osvrdmza9ezNWUK76"
    tags = ["test", "meme"]
    info = {"author": "Tester"}
    meme_endpoint.create_meme(text, url, tags, info, auth_token)
    meme_endpoint.check_response_status_is_ok()
    return meme_endpoint.meme_id, text, url, tags, info
