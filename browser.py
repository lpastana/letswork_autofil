import os
import time
import holidays
import pyautogui
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

class Browser:
    def __init__(self, start_date, end_date):
        self.base_url = "https://app.letswork.com.br"
        self.username = os.environ.get("USERNAME")
        self.password = os.environ.get("PASSWORD")
        self.start_date = start_date
        self.end_date = end_date

    def setup(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.base_url)

    def wait_elem(self, elem):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elem)))

    def login(self):
        self.wait_elem('//input[@name="login"]')
        self.driver.find_element(By.NAME, "login").send_keys(self.cpf)
        self.driver.find_element(By.NAME, "senha").send_keys(self.cpf)
        self.driver.find_element(By.ID, "submit").click()

    def get_holydays(self):
        return holidays.country_holidays("BR")
        

    def fill_missing_days(self, date):
        self.driver.get(f"{self.base_url}/timesheet/index")
        time.sleep(2)

        sunday_pos = (338, 471)
        pyautogui.click(sunday_pos)

        pyautogui.click(x=1056, y=563)

        time.sleep(2)

        start_date_pos = (811, 353)
        pyautogui.click(start_date_pos)
        pyautogui.write(date)

        start_hour_pos = (1066, 357)
        pyautogui.click(start_hour_pos)
        pyautogui.write("08:00")

        end_date_pos = (812, 404)
        pyautogui.click(end_date_pos)
        pyautogui.write(date)

        end_hour_pos = (1065, 407)
        pyautogui.click(end_hour_pos)
        pyautogui.write("17:00")

        project_pos = (984, 435)
        pyautogui.click(project_pos)
        pyautogui.write("a")
        pyautogui.press("enter")

        confirm_pos = (1270, 548)
        pyautogui.click(confirm_pos)  


    def find_element_by_class(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def close(self):
        if self.driver:
            self.driver.close()