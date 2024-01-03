from time import sleep

from selene import browser, be, have


def test_open_chat(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('.l-jivo-wrap').click()

    browser.element('.notranslate').should(be.visible)


def test_close_chat(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('.l-jivo-wrap').click()
    browser.element('.notranslate').element('.closeButton_ed11').element('.closeIcon_e25f').click()

    browser.element('.l-jivo-wrap').should(be.visible)


def test_delete_name_input_after_closing_chat(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('.l-jivo-wrap').click()

    browser.element('[placeholder="Ваше имя"]').send_keys('Сергей')

    browser.element('.notranslate').element('.closeButton_ed11').element('.closeIcon_e25f').click()
    sleep(2)
    browser.element('.l-jivo-wrap').click()

    browser.element('[placeholder="Ваше имя"]').should(have.value(''))


def test_delete_email_input_after_closing_chat(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('.l-jivo-wrap').click()

    browser.element('[placeholder="Ваш e-mail*"]').send_keys('mail@mail.com')

    browser.element('.notranslate').element('.closeButton_ed11').element('.closeIcon_e25f').click()
    sleep(2)
    browser.element('.l-jivo-wrap').click()

    browser.element('[placeholder="Ваше имя"]').should(have.value(''))
