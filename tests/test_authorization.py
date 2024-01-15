from allure_commons.types import Severity
from qa_guru_diploma.pages.lime_shop_page import lime_shop
import os
import allure

login_auth = os.getenv('login_auth')
password_auth = os.getenv('password_auth')
wrong_password = os.getenv('wrong_password_auth')
wrong_login = os.getenv('wrong_login_auth')


@allure.tag("Diploma")
@allure.severity(Severity.CRITICAL)
@allure.feature("Дипломный проект")
def test_successful_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(login_auth)
    lime_shop.type_password(password_auth)
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_successful_authorization()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_wrong_password_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(login_auth)
    lime_shop.type_password(wrong_password)
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_authorization_error_message_is_visible()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_wrong_login_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(wrong_login)
    lime_shop.type_password(password_auth)
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_authorization_error_message_is_visible()


@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_close_authorization_modal(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.close_authorization_modal()
    # THEN
    lime_shop.personal_area_button_is_visible()
