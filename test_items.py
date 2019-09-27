def test_find_add_to_cart_button(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button.get_attribute('value') == button.text
