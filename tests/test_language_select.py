import allure
from allure_commons.types import Severity
from qa_guru_diploma.pages.lime_shop_page import lime_shop


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_language_select(open_main_page):
    # WHEN
    lime_shop.click_language_selector()
    lime_shop.select_kazakhstan_language()

    # THEN
    lime_shop.check_browser_url('https://lime-shop.com/kz_ru')
