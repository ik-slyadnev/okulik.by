import pytest


class TestCreateMeme:
    @pytest.mark.usefixtures("create_meme")
    def test_create_meme(self, meme_endpoint, auth_token):
        text = "Test meme"
        url = "https://images.app.goo.gl/mb6KFGLYZwmhx57T9"
        tags = ["test", "meme"]
        info = {"author": "Tester"}

        meme_endpoint.create_meme(text, url, tags, info, auth_token)
        meme_endpoint.check_response_status_is_ok()
        meme_endpoint.check_meme_id_is_not_empty()
        meme_endpoint.check_meme_data_same_as_sent(text, url, tags, info)

    @pytest.mark.usefixtures("create_meme")
    def test_create_meme_without_auth(self, meme_endpoint):
        text = "Test meme"
        url = "https://images.app.goo.gl/uZgZxhwg1c9my92V7"
        tags = ["test", "meme"]
        info = {"author": "Tester"}

        meme_endpoint.create_meme(text, url, tags, info, token=None)
        assert meme_endpoint.status == 401
