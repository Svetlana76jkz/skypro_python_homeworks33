from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


cookie = {
    "name": "cookie_policy",
    "value": "1"
    }
browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))


def test_open_labirint():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def test_search(term):
    # Найти все книги по слову python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def test_add_book():
    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter


def go_to_cart_test():
    # Переходим в корзину
    browser.get("https://www.labirint.ru/cart/")


def test_get_cart_counter():
    # Проверяем счетчик книг. Должен быть равен числу нажатий
    txt = browser.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)


def test_close_driver():
    # Закрываем браузер
    browser.quit()


def test_card_counter():
    open_labirint()
    search("Python")
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    assert added == cart_counter


# def test_empty_search():
#    open_labirint()
#    serch("no book search term")
#    txt = browser.find_element(
#        By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
#    assert txt == "Мы ничего не нашли по вашему запросу! Что делать?"
#    close_driver()
