# Always-Look-On-The-Bright-Side-Of-Life-Player

automatically searches for the song, clicks youtube link, skips ad (using adblocker), maxes youtube volume, and puts video in fullscreen
<br>
<br>
NOTE: ONCE IN FULLSCREEN, PRESS "=" TO EXIT CODE AND VIDEO
<br>
<br>
# How To Run
download code into your own repo
<br>
<br>
run commands seperately in project terminal
```
pip install keyboard
pip install selenium
```

install chrome driver and extract zip into driver folder (whatever version of chrome you have, download that version): https://chromedriver.chromium.org/downloads
<br>
<br>
follow "Method 1: Repack the installed Chrome extension into the CRX file" on https://techpp.com/2022/08/22/how-to-download-and-save-chrome-extension-as-crx/ for this extension https://getadblock.com/en/, and move the crx file to the driver folder
<br>
<br>
run `main.py` and enjoy the music
<br>
<br>
if wait times for "switching tabs and searching" and "waiting for tab to load to click fullscreen button" are too short/long, change them in `main.py` at the top of the code
```
switchTabsAndSearchTime = [YOURTIMEHERE]
waitForTabToLoadForFullscreen = [YOURTIMEHERE]
```
