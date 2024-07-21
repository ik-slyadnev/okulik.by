import pytest


class TestDeleteMeme:
    def test_delete_existing_meme(self, meme_endpoint, auth_token, create_meme):
        meme_id, _, _, _, _ = create_meme

        meme_endpoint.delete_meme(meme_id, auth_token)
        meme_endpoint.check_response_status_is_ok()

        meme_endpoint.get_meme(meme_id, auth_token)
        assert meme_endpoint.status == 404

    def test_delete_non_existing_meme(self, meme_endpoint, auth_token):
        non_existing_id = 9999999
        meme_endpoint.delete_meme(non_existing_id, auth_token)
        assert meme_endpoint.status == 404

    def test_delete_meme_without_auth(self, meme_endpoint, create_meme):
        meme_id, _, _, _, _ = create_meme
        meme_endpoint.delete_meme(meme_id, token=None)
        assert meme_endpoint.status == 401
