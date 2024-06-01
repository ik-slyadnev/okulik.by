from lesson_21.magic_api.endpoints.get_post_endpoint import GetPostEndpoint


def test_get_post():
    post_id = 1
    response = GetPostEndpoint.get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
