from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

WP_LINK = 'https://web.whatsapp.com'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
driver = webdriver.Chrome()
driver.get(WP_LINK)
while True:
    sleep(30)
    break

contador = True
while contador:
    sleep(3)
    try:
        driver.find_element(By.XPATH, NEW_CHAT)
        contador = False
    except:
        print(f'Por favor scaneie o QR Code')
        contador = True