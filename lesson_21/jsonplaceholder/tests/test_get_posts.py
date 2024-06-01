from lesson_21.jsonplaceholder.endpoints.get_posts_endpoint import GetPostsEndpoint


def test_get_posts():
    response = GetPostsEndpoint.get_posts()
    assert response.status_code == 200
    assert len(response.json()) > 0
