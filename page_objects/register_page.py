from page_objects import support_functions

register_button = 'mlb2-3239800'
url = 'https://fabrykatestow.pl/ciekawostki/'


def submit_register_to_newsletter_button_visible(driver_instance):
    support_functions.wait_for_visibility_of_element(driver_instance, register_button)
    elem = driver_instance.find_element_by_id(register_button)
    return elem.is_displayed()


def fill_name_and_email(driver_instance):
    name = driver_instance.find_element_by_css_selector('input[aria-label="name"]')
    email = driver_instance.find_element_by_css_selector('input[aria-label="email"]')
    button = driver_instance.find_element_by_css_selector('button[type="submit"]')
    name.send_keys('test')
    email.send_keys('pawel_test@fabrykatestow.pl')
    button.click()


def check_that_registrtation_is_finished(driver_instance):
    if "Super!" in driver_instance.page_source:
        return True
    else:
        return False
