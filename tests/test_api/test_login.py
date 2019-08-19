import requests

def test_login():
    session = requests.Session()
    response = session.post('http://localhost:8080/RabotyNET/login', auth=('admin@gmail.com', 'admin'))
    assert response.status_code == 200, "Wrong status code"
    data = response.json()
    assert data['username'] == 'admin@gmail.com', "Wrong username"
    assert data['authorities'][0]['authority'] == 'ROLE_ADMIN', "Wrong user role"
    
