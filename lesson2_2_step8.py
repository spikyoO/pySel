import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Wasd")
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Dasw")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("asw@wasd.ru") 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally: 
    time.sleep(10)
    browser.quit()

