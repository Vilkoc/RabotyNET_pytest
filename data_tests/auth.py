"""Thia module contains user data for sign up/sign in/log out methods"""
from base64 import b64decode as decode

EMAIL_SIGNUP = "rabotynet.test@gmail.com"
FROM_SIGNUP = decode(b'cm9tYV9leHBlcnQ=').decode()

EMAIL_FORGOT_PASSWORD = "rabotynet.test.fp@gmail.com"
FROM_FORGOT_PASSWORD = decode(b'cm9tYV9leHBlcnQ=').decode()

EMAIL_SUBJECT_SIGNUP = "Registration on website RabotyNet"
USERNAME_SIGNUP = 'rabotynet.test@gmail.com'
USER_MAIL = "user@gmail.com"
WRONG_MAIL = "user@gmail"
PASSWORD = 'Qdrwbj!23'
PASSWORD_INCORRECT = "yneoi"

EMAIL_SUBJECT_PASSW_RECOVERY = 'Restore password on website RabotyNet'
USERNAME_PASSW_RECOVERY = 'rabotynet.test.fp@gmail.com'
OLD_PASSWORD = 'Qdrwbj!23'
NEW_PASSWORD = 'Qdrwbj1@3'

LOGIN = [
    ('admin@gmail.com', 'admin', 'Сompanies'),
    ('user@gmail.com', 'user', 'Create company'),
    ('cowner@gmail.com', 'cowner', 'My companies')
]

IS_LOGINED = 'Log out'
IS_CONFIRMATION_SENT = 'User has been created successfully. Confirm your email and login into site!'
IS_INSTRUCTION_SENT = 'Please check mail for further instructions!'
