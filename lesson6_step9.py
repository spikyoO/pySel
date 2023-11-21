from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/registration2.html"

try:
    browser.get(link)
    fname = browser.find_element(By.XPATH, "//form/div[1]/div[1]/input").send_keys("Artem")
    sname = browser.find_element(By.XPATH, "//form/div[1]/div[2]/input").send_keys("Artemov")
    email = browser.find_element(By.XPATH, "//form/div[1]/div[3]/input").send_keys("testqa.artem@mail.com")
    btn = browser.find_element(By.CLASS_NAME, "btn").click()
    welcomeText = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == welcomeText
    
finally:
    time.sleep(5)
    browser.quit()
