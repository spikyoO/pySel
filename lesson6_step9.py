from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/registration2.html"

try:
    browser.get(link)
    fname = browser.find_element(By.XPATH, "//div[contains (@class, 'first_block')]/div[contains (@class, 'first_class')]/input[contains (@class, 'first')]").send_keys("wasd")
    sname = browser.find_element(By.XPATH, "//div[contains (@class, 'first_block')]/div[contains (@class, 'second_class')]/input[contains (@class, 'second')]").send_keys("wasd")
    email = browser.find_element(By.XPATH, "//div[contains (@class, 'first_block')]/div[contains (@class, 'third_class')]/input[contains (@class, 'third')]").send_keys("testqa@mail.com")
    btn = browser.find_element(By.CLASS_NAME, "btn").click()
    welcomeText = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == welcomeText
    
finally:
    time.sleep(5)
    browser.quit()
