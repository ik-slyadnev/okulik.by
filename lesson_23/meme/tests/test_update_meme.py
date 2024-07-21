import pytest


class TestUpdateMeme:
    def test_update_existing_meme(self, meme_endpoint, auth_token, create_meme):
        meme_id, _, _, _, _ = create_meme
        new_text = "Updated meme"
        new_url = "http://example.com/updated_meme.jpg"
        new_tags = ["updated", "meme"]
        new_info = {"author": "Updater"}

        meme_endpoint.update_meme(meme_id, new_text, new_url, new_tags, new_info, auth_token)
        meme_endpoint.check_response_status_is_ok()

        meme_endpoint.get_meme(meme_id, auth_token)
        meme_endpoint.check_meme_data_same_as_sent(new_text, new_url, new_tags, new_info)

    def test_update_non_existing_meme(self, meme_endpoint, auth_token):
        non_existing_id = 9999999
        text = "Test meme"
        url = "http://example.com/meme.jpg"
        tags = ["test", "meme"]
        info = {"author": "Tester"}

        meme_endpoint.update_meme(non_existing_id, text, url, tags, info, auth_token)
        assert meme_endpoint.status == 404

    def test_update_meme_without_auth(self, meme_endpoint, create_meme):
        meme_id, text, url, tags, info = create_meme
        meme_endpoint.update_meme(meme_id, text, url, tags, info, token=None)
        assert meme_endpoint.status == 401
