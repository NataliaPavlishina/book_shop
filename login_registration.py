# Регистрация аккаунта

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("marknat1@hotmail.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("2614Februar")
register = driver.find_element_by_name("register")
register.click()
driver.quit()

# Логин в систему

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
my_account_menu = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((
    By.CLASS_NAME, "woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"
), "Logout"))
driver.quit()


