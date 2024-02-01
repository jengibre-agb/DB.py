import random
import requests
import time
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image


def brush_teeth():
  counter = 0
  while counter < 5:
    try:
        poke_mons = 'path/Teeth/poke_list.txt'
        
        with open (poke_mons, 'r') as file:
            #print('Poke list open')
            pokemon = [word.strip() for word in file.readlines()]
        
        poke_choice = random.choice(pokemon)
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)

        driver.get(f'https://bulbapedia.bulbagarden.net/wiki/{poke_choice}_(Pok%C3%A9mon)')
        #print("Page retrieved")
        time.sleep(3)
        #don't delete the sleep time, this page quickly flags it as a bot if done too fast
        #wait = WebDriverWait(driver, 5)
        poke_image = driver.find_element(By.XPATH, '//td[@colspan="2"]')
        poke_image.screenshot('/path/Teeth/pokemon_image.png')
        image_poke_image = Image.open('/path/Teeth/pokemon_image.png')
        #print("Screenshot done")
        time.sleep(3)
        driver.quit()
        
        return '/path/Teeth/pokemon_image.png'
    
    except NoSuchElementException:
        #print("Element not found. Retrying...")
        counter += 1
        time.sleep(1)

  #print("5 failed attempts, quitting")
  return None

        
#brush_teeth()
