from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime as dt


def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    # * Extract only temperature from text
    output = float(text.split(": ")[1])
    return output


def write_file(text):
    # ? "" if you want smth inside use single quotes '', "''" not """"
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(text)


def main():
    driver = get_driver()
    for i in range(10):
        time.sleep(2)
        element = driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/h1[2]").text
        # ? here we are converting to str because clean_text() returns float
        text = str(clean_text(element))
        write_file(text)


print(main())
