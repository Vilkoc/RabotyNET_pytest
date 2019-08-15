import pytest
from data_tests.user_data import user_data_rab_26 as entry


@pytest.mark.parametrize('field', entry.keys())
def test_all(app, get_to_user_profile, field):
    valid_entry = app.user_profile_page.enter_data_textbox(field, entry[field])
    button_disabled = app.user_profile_page.disabled_update_profile_button()
    assert not valid_entry
    assert button_disabled
    app.header.select_option('Log out')
