import requests


class PatchPostEndpoint:
    @staticmethod
    def patch_post(post_id, data):
        response = requests.patch(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=data)
        return response
