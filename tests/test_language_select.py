from selene import browser, have


def test_lang(open_main_page):
    browser.element('[class="Lang LanguageSelector btn-control"]').click()
    browser.element('[class="menu open"]').all('ul li [data-v-ba5fc516]').second.click()

    browser.should(have.url('https://lime-shop.com/kz_ru'))
