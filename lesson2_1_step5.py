import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link) 
    x = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element(By.ID, "answer").send_keys(calc(x))
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox").click()
    robotRadio = browser.find_element(By.ID, "robotsRule").click()
    btn = browser.find_element(By.CLASS_NAME, "btn").click() 

finally: 
    time.sleep(5)
    browser.quit()
