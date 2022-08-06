import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')
import selenium
PATH = '/users/maddiemeyers/Desktop/Programming/Program Files/chromedriver'
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(PATH)

driver.get("https://www.siteToLogInto.com")
LOGIN = driver.find_element(By.ID,"login")
LOGIN.click()

ACCOUNTTYPE = driver.find_element(By.XPATH,"//div/select")
ACCOUNTTYPE.click()
ACCOUNTTYPE.send_keys(ENTER)

USERNAME = driver.find_element(By.XPATH, "//div/input")
USERNAME.click()
USERNAME.send_keys("usernamehere")

PASSWORD = driver.find_element(By.XPATH, "//div/input[@type='password']")
PASSWORD.click()
PASSWORD.send_keys("passwordhere")

BUTTON = driver.find_element(By.XPATH, "//div/button")
BUTTON.click()


SUM = driver.find_element(By.XPATH, "//div/div/p")
print(SUM)
                               
