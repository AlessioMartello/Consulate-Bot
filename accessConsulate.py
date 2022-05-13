from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

load_dotenv()

# Hide the window as it progresses
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--kiosk");

today = date.today()
now = today.strftime("%d_%m_%Y")

def login():
    """Log into the Consulate website and proceed"""
    s = Service(os.getenv("PATHTOCHROMEDRIVER"))
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get("https://prenotami.esteri.it/")
    emailBar = driver.find_element(By.ID, "login-email")
    passwordBar = driver.find_element(By.NAME, "Password")
    emailBar.send_keys(os.getenv("MYEMAIL"))
    passwordBar.send_keys(os.getenv("MYPASSWORD"))

    form = driver.find_element(By.ID, 'login-form')
    form.submit()
    return driver

def navigate(driver, n):
    """ Move through the pages towards Passport booking. Select the relevant buttons on each page"""
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    if n ==0:
        driver.find_element(By.ID, 'advanced').click()
    elif n==1:
        driver.find_element(By.XPATH, "/html/body/main/div[3]/div/table/tbody/tr[5]/td[4]").click()
    elif n==2:
        driver.find_element(By.NAME, "PrivacyCheck").click()
    elif n == 3:
        driver.find_element(By.ID, "btnAvanti").click()
    elif n == 4:
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
    elif n==5:
        try:
            message = driver.find_element(By.CLASS_NAME, "jconfirm-content").text
            return message
        except NoSuchElementException:
            message = "No lack of dates pop-up, see if you can book!"
            return message
    return driver


def takeScreenshot(driver):
    name = f"screenshot_{now}.png"
    driver.save_screenshot(name)
    return name


if __name__ == "__main__":
    driver = login()
    for i in range(6):
        if i == 5:
            message = navigate(driver, i)
        else:
            new_driver = navigate(driver, i)
        time.sleep(3)


