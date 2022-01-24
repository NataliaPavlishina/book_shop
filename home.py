
          # Добавление комментария
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
s_ruby = driver.find_element_by_css_selector("img[title='Selenium Ruby']")
s_ruby.click()
reviews = driver.find_element_by_css_selector("li.reviews_tab >a")
reviews.click()
driver.find_element_by_class_name("star-5").click()
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Natalia")
email = driver.find_element_by_id("email")
email.send_keys("marknat1@hotmail.com")
driver.find_element_by_id("submit").click()
driver.quit()

