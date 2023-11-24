import time 
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser.get(link)
    y = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(10)
    browser.quit()