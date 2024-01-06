from qa_guru_diploma.pages.lime_shop import LimeShop

lime_shop = LimeShop()


def test_lang(open_main_page):
    # WHEN
    lime_shop.click_language_selector()
    lime_shop.select_kazakhstan_language()

    # THEN
    lime_shop.check_browser_url('https://lime-shop.com/kz_ru')
