from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get("https://hclib.bibliocommons.com/user/login?destination=https%3A%2F%2Fwww.hclib.org%2F")

# find_resources = browser.find_element(By.CSS_SELECTOR,
#                                       ".paragraphs-item-285436 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3) > span:nth-child(1) > a:nth-child(1)")
#
# find_resources.click()

time.sleep(3)

browser.find_element(by=By.XPATH,
        value='/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/form/input[1]').send_keys("22088011182697")

browser.find_element(by=By.XPATH,
                     value='/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/form/input[2]').send_keys("4195")

time.sleep(3)

browser.find_element(by=By.XPATH,
                     value='/html/body/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/form/p[2]/input').click()



