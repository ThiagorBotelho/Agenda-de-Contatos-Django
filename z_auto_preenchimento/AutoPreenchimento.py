from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import random


def xpathclick(driver, xpath):
    driver.find_element(By.XPATH, f'{xpath}').click()


def xpathsend(driver, send, var):
    driver.find_element(By.XPATH, f'{send}').send_keys(var)


def ApagarContatos(driver, quantidade):
    for c in range(0, quantidade):
        xpathclick(driver, '/html/body/div/div[3]/div/div[1]/div/div/div/form/div[4]/table/tbody/tr[1]/td[2]/a')
        xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/p/a')
        xpathclick(driver, '/html/body/div/div[3]/div/div[1]/form/div/input[2]')


driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8000/admin/')
sleep(1)
driver.find_element(By.NAME, 'username').send_keys('thiagorbotelho')
driver.find_element(By.NAME, 'password').send_keys('123456')
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
xpathclick(driver, '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/th/a')

# Para apagar contatos:
# ApagarContatos(driver, 36)


xpathclick(driver, '/html/body/div/div[3]/div/div[1]/div/ul/li/a')

file = open('nomesMas.txt', encoding='utf-8', mode='r')
lista = file.readlines()
lista_homem = []
file.close()

file = open('nomesFem.txt', encoding='utf-8', mode='r')
lista2 = file.readlines()
lista_mulher = []
file.close()

lista_email = ['@gmail.com', '@hotmail.com', '@yahoo.com']

for n in lista:
    lista_homem.append(n.replace('\n', ''))

for m in lista2:
    lista_mulher.append(m.replace('\n', ''))

for c in range(0, 150):
    num_escolha = random.randint(1,2)
    if num_escolha == 1:  # É homem
        nome1_homem = random.choice(lista_homem)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input', nome1_homem)
        nome2_homem = random.choice(lista_homem)
        while nome2_homem == nome1_homem:
            nome2_homem = random.choice(lista_homem)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input', nome2_homem)
        num = random.randint(900000000,999999999)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[3]/div/input', num)
        email = random.choice(lista_email)
        email_completo = nome1_homem + nome2_homem + email
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[4]/div/input', email_completo)
        xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[7]/div/div/select')

    else:
        nome1_mulher = random.choice(lista_mulher)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input', nome1_mulher)
        nome2_mulher = random.choice(lista_mulher)
        while nome2_mulher == nome1_mulher:
            nome2_mulher = random.choice(lista_mulher)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input', nome2_mulher)
        num = random.randint(900000000, 999999999)
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[3]/div/input', num)
        email = random.choice(lista_email)
        email_completo = nome1_mulher + nome2_mulher + email
        xpathsend(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[4]/div/input', email_completo)
        xpathclick(driver, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[7]/div/div/select')

    num1 = random.randint(1,2)

    if num1 == 1:
        sleep(0.5)
        pyautogui.click(x=564, y=906)
    else:
        sleep(0.5)
        pyautogui.click(x=564, y=922)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]').click()

    driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/ul/li/a').click()







