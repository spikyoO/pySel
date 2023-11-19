import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"
i = 1
try:
    browser.get(link)
    fields = browser.find_elements(By.TAG_NAME, "input")
    for field in fields:
        field.send_keys("Answer" + str(i))
        i += 1
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

