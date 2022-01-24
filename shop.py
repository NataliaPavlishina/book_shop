
           # Отображение страницы товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("marknat1@hotmail.com")
password = driver.find_element_by_id("password")
password.send_keys("2614Februar")
login = driver.find_element_by_name("login")
login.click()
driver.find_element_by_id("menu-item-40").click()
html5 = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']")
html5.click()
title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"),
                                                                         "HTML5 Forms"))
driver.quit()

           # Количество товаров в категории

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("marknat1@hotmail.com")
password = driver.find_element_by_id("password")
password.send_keys("2614Februar")
login = driver.find_element_by_name("login")
login.click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_link_text("HTML").click()
quantity = driver.find_elements_by_class_name(
               "button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
if len(quantity) == 3:
    print("На странице отбражаются 3 товара")
else:
    print("Неверное количество товаров на странице")
driver.quit()

   # Сортировка товаров
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("marknat1@hotmail.com")
password = driver.find_element_by_id("password")
password.send_keys("2614Februar")
login = driver.find_element_by_name("login")
login.click()
driver.find_element_by_id("menu-item-40").click()
sorting = driver.find_element_by_css_selector(".orderby >option[value='menu_order']")
sorting_check = sorting.get_attribute("value")
assert sorting_check == "menu_order"
sorting_menu = driver.find_element_by_class_name("orderby")
select = Select(sorting_menu)
select.select_by_value("price-desc")
sorting_menu = driver.find_element_by_css_selector(".orderby >option[value='price-desc']")
sorting_menu_get_text = sorting_menu.text
assert sorting_menu_get_text == "Sort by price: high to low"
driver.quit()

      # Отображение, скидка товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("marknat1@hotmail.com")
password = driver.find_element_by_id("password")
password.send_keys("2614Februar")
login = driver.find_element_by_name("login")
login.click()
driver.find_element_by_id("menu-item-40").click()
android_book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
android_book.click()
old_price = driver.find_element_by_css_selector("del >span.woocommerce-Price-amount.amount")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector("ins >span.woocommerce-Price-amount.amount")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
pretty_photo = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                           ".woocommerce-main-image.zoom img")))
pretty_photo.click()
close_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
driver.quit()

                   # Проверка цены в корзине

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(5)
quantity_at_cart = driver.find_element_by_css_selector("span.cartcontents")
quantity_at_cart_get_text = quantity_at_cart.text
assert quantity_at_cart_get_text == "1 Item"
sum_at_cart = driver.find_element_by_css_selector("span.amount")
sum_at_cart_get_text = sum_at_cart.text
assert sum_at_cart_get_text == "₹180.00"
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                             "tr.cart-subtotal"), "₹180.00"))
total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                "tr.order-total"), "₹189.00"))
driver.quit()

                   # Работа в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0,300);")
driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(3)
driver.find_element_by_css_selector("a[data-product_id='180']").click()
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
remove = driver.find_element_by_css_selector("td.product-remove >a[data-product_id='182']")
remove.click()
time.sleep(3)
driver.find_element_by_link_text("Undo?").click()
quantity = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity.clear()
quantity.send_keys("3")
driver.find_element_by_css_selector(".button[name='update_cart']").click()
quantity = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity_check = quantity.get_attribute("value")
assert quantity_check == "3"
time.sleep(5)
coupon = driver.find_element_by_css_selector("input[name='apply_coupon']")
coupon.click()
time.sleep(3)
error = driver.find_element_by_css_selector(".woocommerce-error >li")
error_get_text = error.text
assert error_get_text == "Please enter a coupon code."
driver.quit()

               # Покупка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0,300);")
driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(3)
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
time.sleep(5)
proceed = WebDriverWait(driver, 5).until(EC.element_to_be_clickable
                                          ((By.CSS_SELECTOR, "a.checkout-button.button.alt.wc-forward"))).click()

first_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                             ((By.ID, "billing_first_name")))
first_name.send_keys("Natalia")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Pav")
e_mail = driver.find_element_by_id("billing_email")
e_mail.send_keys("marknat1@hotmail.com")
tel = driver.find_element_by_id("billing_phone")
tel.send_keys("12037846537")
driver.execute_script("window.scrollBy(0,300);")
country = driver.find_element_by_css_selector("div#s2id_billing_country")
country.click()
country_input = driver.find_element_by_css_selector("input.select2-input")
country_input.send_keys("United States")
US = driver.find_element_by_css_selector("span.select2-match")
US.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("37 Greenwich Ave")
city = driver.find_element_by_id("billing_city")
city.send_keys("Stamford")
state = driver.find_element_by_css_selector("div#s2id_billing_state")
state.click()
state_input = driver.find_element_by_css_selector("input#s2id_autogen389_search")
state_input.send_keys("Conn")
CT = driver.find_element_by_css_selector("span.select2-match")
CT.click()
zip = driver.find_element_by_id("billing_postcode")
zip.send_keys("06902")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
thank_message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
    ((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
    ((By.CSS_SELECTOR, "tfoot :nth-child(3)"), "Check Payments"))
payment_method_2 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
    ((By.CSS_SELECTOR, "li.method"), "Check Payments"))
driver.quit()






