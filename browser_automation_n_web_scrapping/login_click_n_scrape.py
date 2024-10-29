from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    driver = webdriver.Chrome()
    # website address that we are trying to access or scrap
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    driver.find_element(
        by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(
        by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)

    # Click on Home link and wait 2 sec
    driver.find_element(
        by=By.XPATH, value="/html/body/nav/div/a").click()
    time.sleep(2)

    # * scrapte the temperature value
    text = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/h1[2]").text
    return clean_text(text)


print(main())


#! initially, i got an error simply because i did not write time.sleep()
#! to freeze the time to get the temperature value
