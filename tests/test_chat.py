import allure
import pytest
from allure_commons.types import Severity
from qa_guru_diploma.pages.lime_shop_page import lime_shop
from qa_guru_diploma.pages.lime_chat_page import lime_chat


@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_open_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_modal_is_visible()


@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_close_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()
    lime_chat.close_chat()

    # THEN
    lime_chat.check_chat_button_is_visible()


@pytest.mark.skip(reason='поведение чата изменилось во время написания диплома')
@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_delete_name_input_after_closing_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.type_name_into_chat('Сергей')

    lime_chat.close_chat()
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_name_is_blank()


@pytest.mark.skip(reason='поведение чата изменилось во время написания диплома')
@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_delete_email_input_after_closing_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.type_email_into_chat('mail@mail.com')

    lime_chat.close_chat()
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_email_is_blank()


@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_show_emoji_popup(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.click_emoji_button()

    # THEN
    lime_chat.check_emoji_pop_up()


@allure.tag("Diploma")
@allure.severity(Severity.MINOR)
@allure.feature("Дипломный проект")
def test_show_download_history_button(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.click_three_dots_button()

    # THEN
    lime_chat.check_download_history_button()
