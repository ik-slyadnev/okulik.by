import pytest


@pytest.fixture
def post_data():
    return {"title": "foo", "body": "bar", "userId": 1}
