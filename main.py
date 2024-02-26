from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from time import sleep
import os

from dotenv import load_dotenv

# .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']; before that pip install python-dotenv
load_dotenv()  # take environment variables from .env.


my_email = "jobs.email.israel@gmail.com"
my_password = os.environ['FB_PASS']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = "https://tinder.com/"

driver.get(url)
sleep(3)
log_in_btn = driver.find_element(By.LINK_TEXT,"Log in")
log_in_btn.click()
sleep(2)
facebook_btn = driver.find_element(By.XPATH, '//*[@id="c-1177047094"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_btn.click()

sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_input.send_keys(my_email)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(my_password)

log_in_btn = driver.find_element(By.NAME,"login")
log_in_btn.click()

sleep(6)
#print(driver.title)

# continue_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
# continue_btn.click()
#
# sleep(2)

driver.switch_to.window(base_window)
print(driver.title)

allow_btn = driver.find_element(By.XPATH, '//*[@id="c-1177047094"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_btn.click()

miss_out_btn = driver.find_element(By.XPATH, '//*[@id="c-1177047094"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
miss_out_btn.click()

accept_btn = driver.find_element(By.XPATH, '//*[@id="c-1398387530"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_btn.click()


sleep(5)

for i in range(10):
    try:
        swipe_no_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
        swipe_no_btn.click()
        sleep(4)
    except:
        try:
            swipe_no_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
            swipe_no_btn.click()
            sleep(4)
        except ElementClickInterceptedException:
            print("click intercepted")
            pop_up = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]')
            pop_up.click()
    print(i)
    sleep(1)

