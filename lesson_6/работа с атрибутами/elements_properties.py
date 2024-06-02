from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru") #переход на сайт

# Метод "#text"
usd = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]')
txt = usd.text #в переменную с методом text соберется информация об элементе

#Можно сократить:
#txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text

print(txt) #запрос выведет информацию из переменной в терминал
driver.quit() #закрываем драйвер


# метод tag_name
#tag = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name #собираем информацию о теге в переменную

#print(tag) #выводим информацию из переменной в терминал
#driver.quit()

# Метод id
#здесь по умолчанию идут команды для импорта драйвера, класса By и т.д.

#driver.get("https://ya.ru")

#id = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').id #собираем информацию об идентификаторе

#print(id) #выводим информацию из переменной в терминал

#driver.quit()

# Метод get_atribute
#driver.get("https://ya.ru")

#href = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').get_attribute("href")

#print(href)

#driver.quit()

# Метод value_of_css_property
#ff = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("font-family")

#print(ff)

#driver.quit()


