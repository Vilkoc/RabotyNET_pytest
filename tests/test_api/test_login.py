import requests
import pytest
import allure
from data_tests.auth import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP


@allure.feature('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'ROLE_ADMIN'),
    ('user@gmail.com', 'user', 'ROLE_USER'),
    ('cowner@gmail.com', 'cowner', 'ROLE_COWNER')
    ])
def test_login(user, password, expected):
    session = requests.Session()
    response = session.post('http://localhost:8080/RabotyNET/login', auth=(user, password))
    assert response.status_code == 200, "Wrong status code"
    data = response.json()
    assert data['username'] == user, "Wrong username"
    assert data['authorities'][0]['authority'] == expected, "Wrong user role"
    session.get('http://localhost:8080/RabotyNET/logout')

def test_sign_up():
    session = requests.Session()
    data = {
      "login": USERNAME_SIGNUP,
      "matchingPassword": PASSWORD,
      "password": PASSWORD
    }
    response = session.post('http://localhost:8080/RabotyNET/users/auth', data)
    assert response.status_code == 200, "Wrong status code"
    data = response.json()
    assert data['username'] == user, "Wrong username"
    assert data['authorities'][0]['authority'] == expected, "Wrong user role"
    session.get('http://localhost:8080/RabotyNET/logout')

