from json import dump, load
from selenium import webdriver
from time import sleep
from os.path import exists
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InstaBot:
    '''Set driverpath to geckodriver file path to be able to use Firefox'''
    driverpath = None

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, username, password):
        self.driver.get("https://instagram.com/")
        self.driver.implicitly_wait(7)
        if not exists("./Cookies/ig.json"):
            try:
                os.makedirs('Cookies')
            except:
                print("File 'Cookies' exists. ")
            try:
                username_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
                password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
                username_input.send_keys(username)
                password_input.send_keys(password)

                login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
                login_button.click()
                not_now_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Ne sada']")))
                not_now_button.click()
                notifications_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Ne sada"]')))
                notifications_button.click()
                
                cookie = self.driver.get_cookies()
                with open("Cookies/ig.json", "w") as file:
                    dump(cookie, file)
                print("Cookies saved!")

                self.driver.refresh()

            except:
                raise KeyError("Error! Login failed.")
        else:
            '''
            '''
            with open("./Cookies/ig.json", "r") as _file:
                for i in load(_file):
                    self.driver.add_cookie(i)

                sleep(1)
                self.driver.refresh()

                try:
                    username_input = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
                    password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
                    username_input.send_keys(username)
                    password_input.send_keys(password)
                    
                    login_button = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
                    login_button.click()
                    not_now_button = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Ne sada']")))
                    not_now_button.click()
                    notifications_button = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[text()="Ne sada"]')))
                    notifications_button.click()
                except:
                    raise Exception("Login failed! ")

                print("Login successful")


    def cycle_stories(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Priča')]"))).click()
        try:
            while True:
                try:
                    NextStory = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'FhutL')]")))
                    NextStory.click()
                except:
                    break
        except:
            print("Did not click on next")

instance = InstaBot()
instance.login(username, password)
instance.cycle_stories() 
