from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

#поместили элемент в переменную div
div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

#поместили вложенный элемент в переменную a
a = div.find_element(By.CSS_SELECTOR, "a")

print(a.get_attribute("href"))
