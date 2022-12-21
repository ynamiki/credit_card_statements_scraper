import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def login(driver, user, password):
    driver.get("https://netanswerplus.resonacard.co.jp/PC-RE/welcomeSCR.do")
    driver.find_element(by=By.NAME, value="inputId").send_keys(user)
    driver.find_element(by=By.NAME, value="inputPassword").send_keys(password)
    driver.find_element(by=By.XPATH, value="//a/img[@alt='ログイン']").click()


def download(driver):
    driver.find_element(by=By.XPATH, value="//a/img[@alt='ご利用明細照会']").click()
    try:
        driver.find_element(by=By.XPATH, value="//a/img[@alt='WEB明細ダウンロード']").click()
    except NoSuchElementException:
        pass


if __name__ == "__main__":
    with open("accounts.csv") as f:
        r = csv.reader(f)
        for a in r:
            driver = webdriver.Chrome()

            login(driver, a[0], a[1])
            download(driver)
            time.sleep(5)

            driver.quit()
