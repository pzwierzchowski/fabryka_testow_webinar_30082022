from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def check_current_url(driver_instance, url):
    current_url = driver_instance.current_url
    if current_url == url:
        return True


def save_window_after(driver_instance):
    window_after_click = driver_instance.window_handles[1]
    driver_instance.switch_to.window(window_after_click)
