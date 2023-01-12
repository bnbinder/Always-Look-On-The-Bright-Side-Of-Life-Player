from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import keyboard
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import ctypes

switchTabsAndSearchTime = 2
waitForTabToLoadForFullscreen = 2
MAXVOLUME = 1;

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


# Using Chrome to access web

chrome_options = Options()
chrome_options.add_extension('driver/5.3.3_0.crx')
chrome_options.add_argument("start-maximized");

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=chrome_options)

print("DRIVER INITIALIZED")


# Open the website and search for video

driver.get('https://www.google.com')
searchBox = "gLFyf"
title = "Always Look on the Bright Side of Life"
driver.switch_to.window(driver.window_handles[0])
time.sleep(switchTabsAndSearchTime)
id_box = driver.find_element(By.CLASS_NAME, searchBox)
for i in title:
    id_box.send_keys(i)
id_box.submit()

print("VIDEO SEARCHED")


# Find first result of video title and link

text = driver.find_elements(By.XPATH, '//h3[@class="H1u2de"]/a/h3')
video = driver.find_elements(By.XPATH,'//h3[@class="H1u2de"]/a/h3')

if "always look on the bright side of life" in text[0].text.lower():
    video[0].click()
    print("VIDEO CLICKED")
else:
    print("VIDEO NOT FOUND")


# Find and click fullscreen button 

time.sleep(waitForTabToLoadForFullscreen)

fullscreen = driver.find_element(By.XPATH, '//*[@class="ytp-fullscreen-button ytp-button"]')

element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@class = 'ytp-fullscreen-button ytp-button']")))

if fullscreen.get_attribute("title") == "Full screen (f)":
    fullscreen.click()
    print("CLICKED FULL SCREEN")
else:
    print("IN FULL SCREEN ALREADY")


# Turn youtube volume to max

volumeButton = driver.find_element(By.XPATH, '//*[@class="ytp-mute-button ytp-button"]')
if volumeButton.get_attribute("data-title-no-tooltip") == "Unmute":
    volumeButton.click()

volumeMeter = driver.find_element(By.XPATH, '//*[@class="ytp-volume-area"]/div')

player = driver.find_element_by_id('movie_player')

while int(volumeMeter.get_attribute("aria-valuenow")) < 100:
    player.send_keys(Keys.ARROW_UP) 
    print(str(int(volumeMeter.get_attribute("aria-valuenow")))+" VOLUME")

print("VOLUME AT MAX")


# Press any key to exit

def on_press(key):
    # Record the key pressed
    # if keyboard.is_pressed(' '):
    #  key = " "
    recorded_keys.append(key)


# Start listening for key presses
keyboard.on_press(on_press)

recorded_keys = []

while True:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # If they try to lower or mute youtube volume, raise it up
    if volumeButton.get_attribute("data-title-no-tooltip") == "Unmute":
        volumeButton.click()
    if int(volumeMeter.get_attribute("aria-valuenow")) < 100:
        player.send_keys(Keys.ARROW_UP) 
        print(str(int(volumeMeter.get_attribute("aria-valuenow")))+" VOLUME")
    try:
        if volume.GetMasterVolumeLevel() < MAXVOLUME:
            volume.SetMasterVolumeLevelScalar(MAXVOLUME, None)
    except:
        print("COM ERROR, IDK WHY")
        
    if keyboard.is_pressed("="):
        break

driver.close()
print("SCRIPT ENDED")