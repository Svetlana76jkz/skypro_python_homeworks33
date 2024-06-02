from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_card_counter(driver):
    main_pages = MainPage(driver)
    main_pages.set_cookie_policy()
    main_pages.search("python")

    result_page = ResultPage(driver)
    to_be = result_page.add_books()

    cart_page = CartPage(driver)
    cart_page.get()
    as_is = cart_page.get_cart_counter()

    assert as_is == to_be


def test_empty_search_result(driver):
    main_pages = MainPage(driver)
    main_pages.set_cookie_policy()
    main_pages.search("no book search term")

    result_page = ResultPage(driver)
    msg = result_page.get_empty_result_massage()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()
