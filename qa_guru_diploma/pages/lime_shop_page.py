import allure
from selene import browser, have, be, command


class LimeShop:

    @allure.step('Открыть модальное окно авторизации')
    def open_authorization_modal(self):
        browser.element('.columns [href="/ru_ru#lk"] .SvgIcon').click()
        browser.element('.btn.btn-block.btn-outline.btn-primary').click()

    @allure.step('Ввести email')
    def type_email(self, email):
        browser.element('.Inputbox__input').send_keys(email)

    @allure.step('Ввести пароль')
    def type_password(self, password):
        browser.element('.Inputbox__input.passwordInput').send_keys(password)

    @allure.step('Нажать кнопку войти')
    def submit_authorization(self):
        browser.element('[type="submit"]').click()

    @allure.step('Проверить, что авторизация прошла успешно')
    def check_successful_authorization(self):
        browser.element('.FormGroup.FormGroupSubmit .FormGroup__control button').should(
            have.text('ИЗМЕНИТЬ ПАРОЛЬ'))

    @allure.step('Проверить отображение ошибки авторизации')
    def check_authorization_error_message_is_visible(self):
        browser.element('.App_Message .snack-bar-wrap .snack-bar').should(be.visible)

    @allure.step('Закрыть модальное окно авторизации')
    def close_authorization_modal(self):
        browser.element('.SvgIcon.IButtonIcon').click()

    @allure.step('Проверить, что кнопка личного кабинета отображается')
    def personal_area_button_is_visible(self):
        browser.element('.columns [href="/ru_ru#lk"] .SvgIcon').should(be.visible)

    @allure.step('Принять куки')
    def accept_cookies(self):
        browser.element('.l-accept-cookies').element('.l-btn').click()

    @allure.step('Нажать кнопку "Подписаться" в футтере')
    def click_subscription_button(self):
        browser.element('[href="#subscribe"]').perform(command.js.scroll_into_view)
        browser.element('[href="#subscribe"]').click()

    @allure.step('Проверить, что отображается модальное окно "подписаться"')
    def check_subscription_modal_is_visible(self):
        browser.element('.ViewModal.add-scrollbar').should(be.visible)

    @allure.step('Нажать чек-бокс согласия на получение маркетинговых коммуникаций')
    def click_marketing_checkbox(self):
        browser.element('.checkbox__label').click()

    @allure.step('Выбрать раздел каталога для подписки')
    def select_catalog_checkbox(self):
        browser.element('.FormGroup.mb-0').element('.checkbox__indicator').click()

    @allure.step('Проверить, что кнопка "подписаться" в модальном окне неактивна')
    def check_subscribtion_button_in_modal_is_disabled(self):
        browser.element('.btn.btn-block').should(be.disabled)

    @allure.step('Нажать селект выбора языка')
    def click_language_selector(self):
        browser.element('.Lang.LanguageSelector.btn-control').click()

    @allure.step('Выбрать казахский язык')
    def select_kazakhstan_language(self):
        browser.element('.menu.open').all('ul li [data-v-ba5fc516]').second.click()

    @allure.step('Проверить открывшийся url в браузере')
    def check_browser_url(self, url):
        browser.should(have.url(url))


lime_shop = LimeShop()