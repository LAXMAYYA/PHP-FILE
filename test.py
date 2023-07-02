import requests
def test_atg():
    response = requests.get('https://atg.world')
    assert response.status_code == 200
