import request
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_card_counter():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    # Найти все книги по слову python
    search_field = browser.find_element(By.CSS_SELECTOR, "#search-field")
    search_field.send_keys('python')
    search_field.send_keys(Keys.RETURN)

    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
    counter = len(buy_buttons)
    for btn in buy_buttons:
        btn.click()
        sleep(1)  # Подождать немного, чтобы убедиться, что товар добавлен в корзину

    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    cart_count = browser.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart'] b").text
    assert counter == int(cart_count), f"Количество товаров в корзине должно быть {counter}, но оно равно {cart_count}"

    browser.quit()
