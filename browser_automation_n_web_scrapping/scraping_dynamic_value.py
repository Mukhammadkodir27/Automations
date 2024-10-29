from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    # extract only the temperature from text
    # ? if you split a text, it will give you a list [value1, value2] in this context
    output = float(text.split(": ")[1])
    # output = float(output[1])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())


#! what you found out is that, when xpath copy does not work, you can manually look for location of that variable or text using indexing technique.
#! also, learnt how to use split() method to get the output we want
