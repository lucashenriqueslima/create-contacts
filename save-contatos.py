from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time
import os
import pyautogui
from datetime import datetime

profile = webdriver.FirefoxProfile(
    'C:/Users/Studio M/AppData/Roaming/Mozilla/Firefox/Profiles/jkbzpsw5.default-release')

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)

driver.get("https://contacts.google.com/")
driver.find_element(By.XPATH, "//*[contains(text(), 'Criar contato')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[contains(text(), 'Criar vários contatos')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(), 'importe os contatos')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(), 'Selecionar arquivo')]").click()
time.sleep(2)
pyautogui.typewrite(f"C:\\Users\\Studio M\\Downloads\\contatos{datetime.today().strftime('%Y-%m-%d')}.csv")
time.sleep(2)   
pyautogui.press('enter')
time.sleep(1)
driver.find_elements(By.XPATH, "//*[contains(text(), 'Importar')]")[3].click()
time.sleep(100)
driver.close()

