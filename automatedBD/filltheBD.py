import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random as r
import script as s

games = s.getGames()

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://127.0.0.1:8000/admin/")

username = driver.find_element_by_id("id_username")
username.send_keys("wajdy")
password = driver.find_element_by_id("id_password")
password.send_keys("wajdy2020")
password.send_keys(Keys.RETURN)

time.sleep(1)
add = driver.find_element_by_link_text('Gamess')
add.click()





for i in range(2, len(games) + 1 ):
    time.sleep(1)
    print("Adding to the data base this game : ",games[i])
    addGames = driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a')
    addGames.click()
    time.sleep(1)
    inputs = driver.find_elements_by_tag_name("input")

    for j in range(1,19):
        if j == 3:
            inputs[j].send_keys(15)
        else:
            inputs[j].send_keys(games[i])

    save = driver.find_element_by_xpath('//*[@id="games_form"]/div/div/input[1]')
    save.click()
    time.sleep(1)