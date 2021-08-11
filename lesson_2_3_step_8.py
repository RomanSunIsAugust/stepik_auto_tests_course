from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    option1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1 = browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    y = calc(x)

    answer_form = browser.find_element_by_css_selector(".form-group>#answer[type='text']").send_keys(y)

    button2 = browser.find_element_by_css_selector(".btn-primary[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           button2)  # скролим страницу, до тех пор, пока не станет видимым элемент
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
