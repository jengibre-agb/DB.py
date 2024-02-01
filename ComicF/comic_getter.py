import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from PIL import Image
import io

def comic():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    #Don't delete the window size, the ss are taken awkwardly without it (idk if this is true for this script too)

    driver.get(f'https://explosm.net/rcg')
    
    generate_button = driver.find_element(By.CLASS_NAME, "RandomComicGenerator__Button-sc-xb0zoq-0.eJtqax")
    generate_button.click()
    #print('button clicked')
    time.sleep(3)
    
#SS each panel, one for image (3)
    panels = driver.find_elements(By.CLASS_NAME, "Panel__Container-sc-16olx3c-0.cZrqvb")
    for i, pannel in enumerate(panels):
        comic_path = f'ComicF/comic_{i + 1}.png'
        pannel.screenshot(comic_path)
    #print('comic found')                         

    panel1 = Image.open('ComicF/comic_1.png')
    panel2 = Image.open('ComicF/comic_2.png')
    panel3 = Image.open('ComicF/comic_3.png')

    width, height = panel1.size
    
#Template with the dimensions
    combined_image = Image.new('RGB', (width * 3, height))

#Merged panels
    combined_image.paste(panel1, (0, 0))
    combined_image.paste(panel2, (width, 0))
    combined_image.paste(panel3, (2 * width, 0))

#Whole 1x3 panel
    combined_image.save('ComicF/comic_panel.png')
    
    driver.quit()

    return ('ComicF/comic_panel.png')

#comic()
