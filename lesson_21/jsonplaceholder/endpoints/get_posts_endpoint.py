import requests


class GetPostsEndpoint:
    @staticmethod
    def get_posts():
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response
