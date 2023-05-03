from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

MY_EMAIL = "example@gmail.pl"
MY_PASSWORD = "*********"
PHONE = "*********"

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=webdriver.ChromeOptions())
driver.maximize_window()
url = "https://www.linkedin.com/jobs/search/?currentJobId=3577640616&distance=25&f_AL=true&f_E=3&f_JT=F%2CC%2CO&f_T" \
      "=25169%2C24%2C340&f_WT=1%2C2%2C3&geoId=105072130&keywords=Programista%20Python"
driver.get(url)
time.sleep(3)

login = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login.click()
time.sleep(2)

username = driver.find_element(By.NAME, "session_key")
username.send_keys(MY_EMAIL)
passwd = driver.find_element(By.NAME, "session_password")
passwd.send_keys(MY_PASSWORD)
passwd.send_keys(Keys.ENTER)
time.sleep(2)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("apply")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        apply_button.click()
        time.sleep(2)

        phone = driver.find_element(By.CSS_SELECTOR, "div input")
        print(phone.get_attribute("value"))
        if phone.get_attribute("value") == "":
            phone.send_keys(PHONE)

        next = driver.find_element(By.CSS_SELECTOR, "footer button")
        next.click()
        time.sleep(2)
        submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")[1]
        print(submit_button.get_attribute("data-easy-apply-next-button"))
        if submit_button.get_attribute("data-easy-apply-next-button") is None:
            submit_button.send_keys(Keys.ENTER)

        else:
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        time.sleep(3)

        send = driver.find_elements(By.CSS_SELECTOR, "footer button")[1]
        send.send_keys(Keys.ENTER)
        time.sleep(5)

        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No button, skipped...")
        continue

driver.quit()
