from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.labirint.ru/")
       
    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
            }
        self._driver.add_cookie(cookie)

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
