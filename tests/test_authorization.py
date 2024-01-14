from allure_commons.types import Severity
from qa_guru_diploma.pages.lime_shop import LimeShop
import os
import allure

lime_shop = LimeShop()


@allure.tag("Diploma")
@allure.severity(Severity.CRITICAL)
@allure.feature("Дипломный проект")
def test_successful_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(os.getenv('login_auth'))
    lime_shop.type_password(os.getenv('password_auth'))
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_successful_authorization()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_wrong_password_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(os.getenv('login_auth'))
    lime_shop.type_password(os.getenv('wrong_password_auth'))
    lime_shop.submit_authorization()

    # THEN
    lime_shop.check_authorization_error_message_is_visible()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_wrong_login_authorization(open_main_page):
    # WHEN
    lime_shop.open_authorization_modal()
    lime_shop.type_email(os.getenv('wrong_login_auth'))
    lime_shop.type_password(os.getenv('password_auth'))
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
