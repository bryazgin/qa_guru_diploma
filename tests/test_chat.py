from time import sleep
from qa_guru_diploma.pages.lime_shop import LimeShop, LimeChat

lime_shop = LimeShop()
lime_chat = LimeChat()


def test_open_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_modal_is_visible()


def test_close_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()
    lime_chat.close_chat()

    # THEN
    lime_chat.check_chat_button_is_visible()


def test_delete_name_input_after_closing_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.type_name_into_chat('Сергей')

    lime_chat.close_chat()
    sleep(2)
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_name_is_blank()


def test_delete_email_input_after_closing_chat(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_chat.open_chat()

    lime_chat.type_email_into_chat('mail@mail.com')

    lime_chat.close_chat()
    sleep(2)
    lime_chat.open_chat()

    # THEN
    lime_chat.check_chat_email_is_blank()
