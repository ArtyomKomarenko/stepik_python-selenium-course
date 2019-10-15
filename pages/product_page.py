from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def should_be_info_message_with_price(self, price):
        message_price = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE__PRICE).text
        assert price == message_price, f'Price "{message_price}" in message is not equal to item price "{price}"'

    def should_be_succes_message_with_item_name(self, name):
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE__ITEM_NAME).text
        assert name == message_name, f'Item name "{message_name}" in message is not equal to item name "{name}"'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'
