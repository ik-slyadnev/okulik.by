from lesson_21.jsonplaceholder.endpoints.create_post_endpoint import CreatePostEndpoint
from lesson_21.jsonplaceholder.endpoints.delete_post_endpoint import DeletePostEndpoint


def test_delete_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    create_response = CreatePostEndpoint.create_post(data)
    post_id = create_response.json()["id"]

    delete_response = DeletePostEndpoint.delete_post(post_id)
    assert delete_response.status_code == 200
