"""This module allows you to automate creation of claim"""


def test_admin_create_claim(app, make_screen):
    """ Test-case that create claim to company"""
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')
    app.companies_page.view_detail_about_co()

    app.company_details_page.create_claim()
    app.company_details_page.select_title_of_claim()
    app.company_details_page.set_description_of_claim()
    app.company_details_page.send_claim()
    app.header.move_to_companies()

    assert app.companies_page.view_warning_status_of_co()
