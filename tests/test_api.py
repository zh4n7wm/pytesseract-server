from flask import url_for


def test_about(client):
    assert client.get(url_for('pages.about')).status_code == 200
