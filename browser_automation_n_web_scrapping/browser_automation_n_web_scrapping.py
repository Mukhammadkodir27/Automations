from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    #! Had to comment those options because new version raised errors
    # # Set options to make browsing easier
    # options = webdriver.ChromeOptions()
    # # good for disable unecessary bars
    # options.add_argument("disable-infobars")
    # # chrome will start at maximum size
    # options.add_argument("start-maximized")
    # options.add_argument("disable-dev-shm-usage")  # good for linux os
    # options.add_argument("no-sandbox")
    # # some browsers do not like automation scripts, so here we enable them
    # options.add_experimental_option("exludeSwitches", ["enable-automation"])
    # options.add_argument("disable-blink-features=AutomationControlled")

    # # here options is default and after '=' we are assigning our options variable
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    # # here you need to paste the web address of scapping web-page
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    return element


print(main())
