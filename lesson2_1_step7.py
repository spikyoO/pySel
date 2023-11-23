import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser.get(link)
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    answer = browser.find_element(By.ID, "answer").send_keys(calc(x))
    roboCheckbox = browser.find_element(By.ID, "robotCheckbox").click()
    roboRadio = browser.find_element(By.ID, "robotsRule").click()
    btn = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(10)
    browser.quit()