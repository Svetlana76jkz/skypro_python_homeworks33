from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_card_counter():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    main_pages = MainPage(browser)
    main_pages.set_cookie_policy()
    main_pages.search("python")

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_cart_counter()

    assert as_is == to_be
    browser.quit()


def test_empty_search_result():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    main_pages = MainPage(browser)
    main_pages.set_cookie_policy()
    main_pages.search("no book search term")
  
    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_massage()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()
