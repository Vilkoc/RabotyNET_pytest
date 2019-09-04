"""Perform positive tests for all fields of user profile page"""
import allure
import pytest
from data_tests.user_data import user_data_rab_19 as entry


@allure.feature('Positive test')
@pytest.mark.parametrize('field', entry)
def test_all(app, field):
    """Enters into particular field the valid data, clicks 'Update button', reads submitted data
     from the field and checks for validity"""
    with allure.step('Positive test for user profile data'):
        user_num = entry[field][0]
        app.header.select_option('Log in')
        app.sign_in_page.login('USER_' + str(user_num))
        app.header.select_option('Profile')
        valid_entry = app.user_profile_page.enter_data_textbox(field, entry[field][1])
        app.user_profile_page.click_update_profile()
        read = app.user_profile_page.read_data_textbox(field)
        assert valid_entry
        assert read == entry[field][1]

