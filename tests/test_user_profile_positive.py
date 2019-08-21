import pytest
import allure
from data_tests.user_data import user_data_rab_19 as entry


@allure.feature('Login all users')
@pytest.mark.parametrize('field', entry)
def test_all(app, get_to_user_profile, field):
    with allure.step('Click log in'):
        valid_entry = app.user_profile_page.enter_data_textbox(field, entry[field])
        app.user_profile_page.click_update_profile()
        read = app.user_profile_page.read_data_textbox(field)
        assert valid_entry
        assert read == entry[field]
        app.header.select_option('Log out')
