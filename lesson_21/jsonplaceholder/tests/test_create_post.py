from lesson_21.jsonplaceholder.endpoints.create_post_endpoint import CreatePostEndpoint


def test_create_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = CreatePostEndpoint.create_post(data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]
