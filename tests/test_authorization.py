from selene import browser, have, be


def test_successful_authorization(open_main_page):
    browser.element('[class ="columns"] > a[href="/ru_ru#lk"] >[class ="SvgIcon"]').click()
    browser.element('[class="btn btn-block btn-outline btn-primary"]').click()
    browser.element('[class="Inputbox__input"]').send_keys('woodst@gmail.com')
    browser.element('[class="Inputbox__input passwordInput"]').send_keys('12345678')
    browser.element('[type="submit"]').click()

    browser.element('[class="FormGroup FormGroupSubmit"] > [class="FormGroup__control"] > button').should(have.text('ИЗМЕНИТЬ ПАРОЛЬ'))


def test_wrong_password_authorization(open_main_page):
    browser.element('[class ="columns"] > a[href="/ru_ru#lk"] >[class ="SvgIcon"]').click()
    browser.element('[class="btn btn-block btn-outline btn-primary"]').click()
    browser.element('[class="Inputbox__input"]').send_keys('woodst@gmail.com')
    browser.element('[class="Inputbox__input passwordInput"]').send_keys('1234567822')
    browser.element('[type="submit"]').click()

    browser.element('[class="App_Message"] > [class="snack-bar-wrap"] > [class="snack-bar"]').should(be.visible)


def test_wrong_login_authorization(open_main_page):
    browser.element('[class ="columns"] > a[href="/ru_ru#lk"] >[class ="SvgIcon"]').click()
    browser.element('[class="btn btn-block btn-outline btn-primary"]').click()
    browser.element('[class="Inputbox__input"]').send_keys('woodset@gmail.com')
    browser.element('[class="Inputbox__input passwordInput"]').send_keys('12345678')
    browser.element('[type="submit"]').click()

    browser.element('[class="App_Message"] > [class="snack-bar-wrap"] > [class="snack-bar"]').should(be.visible)


def test_close_authorization_modal(open_main_page):
    browser.element('[class ="columns"] > a[href="/ru_ru#lk"] >[class ="SvgIcon"]').click()
    browser.element('[class="SvgIcon IButtonIcon"]').click()
    browser.element('[class ="columns"] > a[href="/ru_ru#lk"] >[class ="SvgIcon"]').should(be.visible)