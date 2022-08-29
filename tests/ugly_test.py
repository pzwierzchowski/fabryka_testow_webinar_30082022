from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://fabrykatestow.pl')

window_before = driver.window_handles[0]
driver.find_element_by_link_text('ZAPISZ MNIE NA NEWSLETTER!').click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
url = 'https://fabrykatestow.pl/ciekawostki/'
current_url = driver.current_url


if current_url == url:
    print('OK - you are on the proper page')
else:
    print(current_url)
    print('NOT OK - you are on the wrong page')

driver.find_element_by_css_selector('input[aria-label="name"]').send_keys('test')
driver.find_element_by_css_selector('input[aria-label="email"]').send_keys('pawel_test@fabrykatestow.pl')
driver.find_element_by_css_selector('button[type="submit"]').click()

if "Super!" in driver.page_source:
    print('Found it!')
else:
    print('Did not find it.')


driver.quit()
