from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

divs = driver.find_elements(By.CSS_SELECTOR, "div")

div = divs[6]
#запрашиваем атрибуты и помещаем в переменную css_class:
css_class = div.get_attribute("class")
#выводим в терминал:
print(css_class)