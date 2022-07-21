from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

servico =  Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

browser.get("https://www.studiomfotografia.com.br/api/scripts/get-contatos&passwd=a)()8***0--asf")

time.sleep(2)
browser.close()

os.system(r"cd C:\\Users\\Studio M\\Desktop\\contatos\\download.py")
os.system(r"python save-contatos.py")

os.remove(r"C:\\Users\\Studio M\\Downloads\\contatos.csv")



