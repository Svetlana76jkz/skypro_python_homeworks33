from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://ya.ru")
browser.set_window_size(1000, 600)

sleep(10)

browser.maximize_window() #развернуть окно под размер экрана
browser.minimize_window() #свернуть окно
browser.fullscreen_window() #развернуть окно на весь экран (аналог клавиши F11)

