from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_ITEM = (By.CSS_SELECTOR, '#basket_formset .basket-items .row')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form button')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages  .alert-success')
    SUCCESS_MESSAGE__ITEM_NAME = (By.CSS_SELECTOR, '#messages  .alert-success .alertinner strong')
    INFO_MESSAGE__PRICE = (By.CSS_SELECTOR, '#messages  .alert-info .alertinner strong')
