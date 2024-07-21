import requests
from endpoints.endpoints_handler import Endpoint


class MemeEndpoint(Endpoint):
    meme_id = None
    text = None
    url = None
    tags = None
    info = None

    def create_meme(self, text, url, tags, info, token):
        response = requests.post(
            'http://167.172.172.115:52355/meme',
            headers={'Authorization': token},
            json={'text': text, 'url': url, 'tags': tags, 'info': info}
        )
        self.status = response.status_code
        if self.status == 200:
            data = response.json()
            self.meme_id = data['id']
            self.text = data['text']
            self.url = data['url']
            self.tags = data['tags']
            self.info = data['info']
        return response

    def get_meme(self, meme_id, token):
        response = requests.get(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers={'Authorization': token}
        )
        self.status = response.status_code
        if self.status == 200:
            data = response.json()
            self.text = data['text']
            self.url = data['url']
            self.tags = data['tags']
            self.info = data['info']
        return response

    def update_meme(self, meme_id, text, url, tags, info, token):
        response = requests.put(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers={'Authorization': token},
            json={'id': meme_id, 'text': text, 'url': url, 'tags': tags, 'info': info}
        )
        self.status = response.status_code
        return response

    def delete_meme(self, meme_id, token):
        response = requests.delete(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            headers={'Authorization': token}
        )
        self.status = response.status_code
        return response

    def check_meme_data_same_as_sent(self, text, url, tags, info):
        assert self.text == text
        assert self.url == url
        assert self.tags == tags
        assert self.info == info

    def check_meme_id_is_not_empty(self):
        assert self.meme_id is not None and len(str(self.meme_id)) > 0
