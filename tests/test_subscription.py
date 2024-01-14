import allure
from allure_commons.types import Severity
from qa_guru_diploma.pages.lime_shop import LimeShop

lime_shop = LimeShop()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_modal_after_clicking_subscription(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_shop.click_subscription_button()

    # THEN
    lime_shop.check_subscription_modal_is_visible()


@allure.tag("Diploma")
@allure.severity(Severity.NORMAL)
@allure.feature("Дипломный проект")
def test_email_is_required_for_subscription(open_main_page):
    # WHEN
    lime_shop.accept_cookies()
    lime_shop.click_subscription_button()

    lime_shop.click_marketing_checkbox()
    lime_shop.select_catalog_checkbox()

    # THEN
    lime_shop.check_subscribtion_button_in_modal_is_disabled()
