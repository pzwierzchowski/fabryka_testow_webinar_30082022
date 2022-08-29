newsletter_button = 'ZAPISZ MNIE NA NEWSLETTER!'


def click_newsletter_button(driver_instance):
    elem = driver_instance.find_element_by_link_text(newsletter_button)
    elem.click()
