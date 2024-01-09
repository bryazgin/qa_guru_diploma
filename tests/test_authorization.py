from qa_guru_diploma.pages.lime_shop import LimeShop
import os

lime_shop = LimeShop()


def test_successful_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(os.getenv('login_auth'))
    lime_shop.type_password(os.getenv('password_auth'))
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_successful_authorization()


def test_wrong_password_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email('woodst@gmail.com')
    lime_shop.type_password('1234567822')
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_authorization_error_message_is_visible()


def test_wrong_login_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email('woodset@gmail.com')
    lime_shop.type_password('12345678')
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_authorization_error_message_is_visible()


def test_close_authorization_modal(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.close_authorization_modal()
    # THEN
    lime_shop.personal_area_button_is_visible()