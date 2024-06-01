import requests


class CreatePostEndpoint:
    URL = "https://jsonplaceholder.typicode.com/posts"

    @staticmethod
    def create_post(data):
        response = requests.post(CreatePostEndpoint.URL, json=data)
        return response
