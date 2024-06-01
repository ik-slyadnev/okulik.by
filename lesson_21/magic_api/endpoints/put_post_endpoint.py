import requests


class PutPostEndpoint:
    @staticmethod
    def put_post(post_id, data):
        response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=data)
        return response
