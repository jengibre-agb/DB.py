import random
import time
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#avoid nsfw games in the dictionary as they require logging in
#fixed on up-to-date version


def ss_steam_review():
    steamgames = '/path/SteamR/steamgames.txt'
    
    with open(steamgames, 'r') as file:
        #print("steamgames_read")
        steamgames = [word.strip().lower() for word in file.readlines()]
        
    steamgame = random.choice(steamgames)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    #Don't delete the window size, the ss are taken awkwardly without it

    #Get a game ID from the dictionary
    driver.get(f'https://steamcommunity.com/app/{steamgame}/reviews/')
    time.sleep(1)

    game_name_elements = driver.find_elements(By.CLASS_NAME, 'apphub_AppName')
    app_name = game_name_elements[0].text

    reviews = driver.find_elements(By.CLASS_NAME, 'apphub_Card.modalContentLink.interactable')
    random_review = random.choice(reviews)
    #apphub_CardContentMain, both these work, just in a different way
    #apphub_UserReviewCardContent
    #print(f'Game: {app_name}')
    
    driver.execute_script("arguments[0].scrollIntoView();", random_review)
    time.sleep(1)
    random_review.screenshot('/path/SteamR/steam_screenshot.png')
    #time.sleep(1)
    driver.quit()
    
    return app_name

#ss_steam_review()


