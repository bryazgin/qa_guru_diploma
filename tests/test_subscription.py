from selene import browser, be, command


def test_modal_after_clicking_subscription(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('[href="#subscribe"]').perform(command.js.scroll_into_view)
    browser.element('[href="#subscribe"]').click()

    browser.element('[class="ViewModal add-scrollbar"]').should(be.visible)


def test_email_is_required_for_subscription(open_main_page):
    browser.element('.l-accept-cookies').element('.l-btn').click()
    browser.element('[href="#subscribe"]').perform(command.js.scroll_into_view)
    browser.element('[href="#subscribe"]').click()

    browser.element('.checkbox__label').click()
    browser.element('[class="FormGroup mb-0"]').element('[class="checkbox__indicator"]').click()

    browser.element('[class="btn btn-block"]').should(be.disabled)
