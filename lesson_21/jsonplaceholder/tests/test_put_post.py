from lesson_21.jsonplaceholder.endpoints.create_post_endpoint import CreatePostEndpoint
from lesson_21.jsonplaceholder.endpoints.put_post_endpoint import PutPostEndpoint


def test_put_post():
    data = {"title": "foo1", "body": "bar21", "userId": 10}
    create_response = CreatePostEndpoint.create_post(data)
    put_id = create_response.json()["id"]

    put_data = {"title": "updated title lolo"}
    put_response = PutPostEndpoint.put_post(put_id, put_data)
    assert put_response.status_code == 200
    assert put_response.json()["title"] == put_data["title"]

