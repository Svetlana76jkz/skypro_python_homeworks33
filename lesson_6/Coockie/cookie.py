from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = { #название переменной придумываем сами, открываем скобки
	'name': 'cookie_policy', #ключ
	'value': '1'} #значение, закрываем скобки

driver.get("https://labirint.ru/")
driver.add_cookie(my_cookie) #добавление cookie

driver.refresh() #обновление страницы
driver.delete_all_cookies() #удаление всех cookie

driver.refresh() #обновление страницы


sleep(10)
driver.quit()