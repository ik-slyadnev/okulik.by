import requests


class DeletePostEndpoint:
    @staticmethod
    def delete_post(post_id):
        response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        return response
