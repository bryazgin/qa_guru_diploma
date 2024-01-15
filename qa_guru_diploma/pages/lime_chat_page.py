import allure
from selene import browser, be, have


class LimeChat:

    @allure.step('Открыть чат')
    def open_chat(self):
        browser.element('.l-jivo-wrap').click()

    @allure.step('Закрыть чат')
    def close_chat(self):
        browser.element('.notranslate').element('.closeButton_ed11').element('.closeIcon_e25f').click()

    @allure.step('Проверить, что кнопка "Чат" отображается')
    def check_chat_button_is_visible(self):
        browser.element('.l-jivo-wrap').should(be.visible)

    @allure.step('Проверить, что модальное окно чата отображается')
    def check_chat_modal_is_visible(self):
        browser.element('.notranslate').should(be.visible)

    @allure.step('Вписать имя пользователя в окно чата')
    def type_name_into_chat(self, chat_name):
        browser.element('[placeholder="Ваше имя"]').send_keys(chat_name)

    @allure.step('Вписать email пользователя в окно чата')
    def type_email_into_chat(self, chat_email):
        browser.element('[placeholder="Ваш e-mail*"]').send_keys(chat_email)

    @allure.step('Проверить, что имя пользователя в окне чата пустое')
    def check_chat_name_is_blank(self):
        browser.element('[placeholder="Ваше имя"]').should(have.value(''))

    @allure.step('Проверить, что email пользователя в окне чата пустой')
    def check_chat_email_is_blank(self):
        browser.element('[placeholder="Ваш e-mail*"]').should(have.value(''))

    @allure.step('Нажать кнопку эмодзи в чате')
    def click_emoji_button(self):
        browser.element('[class="emojiWrap_bf0d"]').click()

    @allure.step('Проверить отображение popup выбора эмодзи')
    def check_emoji_pop_up(self):
        browser.element('[class="popup_edeb show_f40a"]').should(be.visible)

    @allure.step('Нажать кнопку "три точки" в чате')
    def click_three_dots_button(self):
        browser.element('[class ="menuWrap_b00c"]').click()

    @allure.step('Проверить отображение кнопки "скачать историю"')
    def check_download_history_button(self):
        browser.element('[class="menuItem_a572"]').should(be.visible)


lime_chat = LimeChat()
