from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_repeat_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_FIELD)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat_field.send_keys(password)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') != -1

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
