from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get("http://inventwithpython.com")

button = browser.find_element(By.ID, "mc-embedded-subscribe")

button.click()