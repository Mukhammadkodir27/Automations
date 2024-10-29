from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    driver = webdriver.Chrome()
    # website address that we are trying to access or scrap
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(
        by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(
        by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    # after login we need to go to HomePage so here we copied xpath of homepage as it does not have id value
    time.sleep(2)
    driver.find_element(
        by=By.XPATH, value="/html/body/nav/div/a").click()
    print(driver.current_url)


print(main())


# ? we can use id of a variable to access it instead of using xpath location address
# + Keys.RETURN does the same function as (we press enter after writing credentials to log in)
# ? .click() function at the end clicks to that url xpath address to enter
