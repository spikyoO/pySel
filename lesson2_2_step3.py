import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    summary = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(summary))
    browser.find_element(By.CLASS_NAME, "btn").click()


finally: 
    time.sleep(10)
    browser.quit()    