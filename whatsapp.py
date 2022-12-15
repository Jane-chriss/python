from os import environ
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

       

WP_LINK = 'https://web.whatsapp.com'
NEW_CHAT = '//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div/div[2]/div[1]/div[1]/span' 
SEND = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'

driver = webdriver.Chrome()
driver.get(WP_LINK)

def enviar(nome):
    try:
       mensagem = driver.find_element(By.XPATH, MESSAGE_BOX)
       mensagem.click()
       mensagem.send_keys(f'Ola, *{nome}*, tudo bem?')
       mensagem.send_keys(Keys.CONTROL, Keys.RETURN)
       mensagem.send_keys(f'Esta é uma mensagem de *teste*.')
       sleep(3)
       botao = driver.find_element(By.XPATH, SEND)
       botao.click()
       return 'Enviado'
       
    except Exception as e:
        return 'sem whatsapp'

listadetelefone = ['5518991226146','5518997117528']
listanome = ['Pamela', 'Gustavo']


contador = True
while contador:
    sleep(3)
    try:
        driver.find_element(By.XPATH, NEW_CHAT)
        contador = False
    except:
        print(f'Por favor scaneie o QR Code')
        contador = True

envio = []
for nome, telefone in zip (listanome, listadetelefone):
    try:
        sleep(10)
        url = f'https://web.whatsapp.com/send?phone={telefone}'
        driver.get(url)
        sleep(10)
        status = enviar(nome)
        print(f'telefone: {telefone} - {nome} | {status}')

    except Exception as e:
        driver.execute_script("window.stop();")
        print(f'Telefone: {telefone} | ERRO AO ENVIAR')
        status = 'Erro ao enviar'
    envio.append(status)

    print(envio)
    sleep(10)
    driver.close()

