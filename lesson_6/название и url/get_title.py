from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://www.selenium.dev/documentation/")
browser.title #сбор названия вкладок

current_title = browser.title
print(current_title)

browser.quit()
