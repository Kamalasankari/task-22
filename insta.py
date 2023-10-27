from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Insta:
    def __init__(self):
        self.url = "https://www.instagram.com/guviofficial/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def insta_follow(self):
        try:
            sleep(4)
            self.driver.maximize_window()
            sleep(4)
            self.driver.get(self.url)
            sleep(4)
            followers = self.driver.find_element(by= By.XPATH, value='.//*[contains(text(), "followers")]/span')
            num1 = followers.text
           #print(followers)
            print("Number of followers in Guvi Insta is :",num1)
            following = self.driver.find_element(by= By.XPATH, value='.//*[contains(text(), "following")]/span')
            num2 = following.text
            print("Number of following in Guvi Insta is :", num2)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.close()
i = Insta()
i.insta_follow()