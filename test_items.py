from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exist(browser):
    """Тест проверяет, что страница товара
     содержит кнопку добавления в корзину
    """
    browser.get(link)

    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) > 0,\
        "Button 'add-to-basket' does not exist"
