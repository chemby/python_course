from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_story_api():
    params = {
        'title': 'api add',
        'username': "test api",
        'content': 'api story aaaaaaaaaaaaaaaaaaaaaaaa',
    }
    response = client.post('/api/add_story', json=params)
    assert response.status_code == 201
    assert "title" in response.json()


def test_get_stories():
    response = client.get('/api/get_stories')
    assert response.status_code == 200
    assert response.json()[0]['username'] == 'test api'


def test_get_stories_post():
    response = client.post('/api/get_stories')
    assert response.status_code == 200


def test_get_stories_by_title():
    params = {
        'query_str': 'wekoewnrkewrjlew'
    }
    response = client.get('/api/search_stories', params=params)
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_get_stories_by_title_success():
    params = {
        'query_str': 'api'
    }
    response = client.get('/api/search_stories', params=params)
    assert response.status_code == 200
    assert response.json()
