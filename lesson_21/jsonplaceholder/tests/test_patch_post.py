from lesson_21.jsonplaceholder.endpoints.create_post_endpoint import CreatePostEndpoint
from lesson_21.jsonplaceholder.endpoints.patch_post_endpoint import PatchPostEndpoint


def test_patch_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    create_response = CreatePostEndpoint.create_post(data)
    patch_id = create_response.json()["id"]

    patch_data = {"title": "updated title"}
    patch_response = PatchPostEndpoint.patch_post(patch_id, patch_data)
    assert patch_response.status_code == 200
    assert patch_response.json()["title"] == patch_data["title"]
