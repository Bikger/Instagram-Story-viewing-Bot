from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(username, password):
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://instagram.com/")

    # login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    # login_link.click()

    sleep(2)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR,"input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    sleep(4)
    print("Report: ")
    try:
        not_now_button = driver.find_element(By.XPATH, "//button[text()='Ne sada']")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(not_now_button)).click()
    except:
        print("'not now' button not found.")

    sleep(2)

    try:
        notifications_button = driver.find_element(By.XPATH,'//button[text()="Ne sada"]')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(notifications_button)).click()
    except:
        print("Didn't find notifications button")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Priča')]"))).click()

    try:
        while True:
            try:
                NextStory = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'FhutL')]")))
                NextStory.click()
            except:
                break
    except:
        print("Did not click on next")

    unixTimeStamp = time.time()
    driver.quit()
    print(unixTimeStamp, "\nNo issues encountered.")
login("username", "password")
