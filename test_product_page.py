import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_item()
    basket_page.should_be_empty_basket_text()


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                          pytest.param(
                              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                              marks=pytest.mark.xfail(reason='bug')),
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    price = page.get_item_price()
    name = page.get_item_name()
    page.should_be_info_message_with_price(price)
    page.should_be_succes_message_with_item_name(name)


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_disappear_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        main_page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = f'test{int(time.time())}@fakemail.org'
        login_page.register_new_user(email, 'QWEqwe123!')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_item_to_cart()
        price = page.get_item_price()
        name = page.get_item_name()
        page.should_be_info_message_with_price(price)
        page.should_be_succes_message_with_item_name(name)

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()
