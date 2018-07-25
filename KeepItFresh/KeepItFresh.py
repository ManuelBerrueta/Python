import urllib.request
from selenium import webdriver
import time

NumberOfSites = 19
CurrentUrl = 0
SleepTimeinSeconds = 3
NextUrl = 1

myUrls = ['https://www.stackexchange.com/', 'https://security.stackexchange.com/', 'https://reverseengineering.stackexchange.com/',
'https://unix.stackexchange.com/', 'https://serverfault.com/', 'https://superuser.com/', 'https://stackoverflow.com/',
'https://networkengineering.stackexchange.com/', 'https://askubuntu.com/', 'https://scicomp.stackexchange.com/',
'https://softwareengineering.stackexchange.com/', 'https://crypto.stackexchange.com/', 
'https://dba.stackexchange.com/', 'https://math.stackexchange.com/', 
'https://raspberrypi.stackexchange.com/', 'https://iot.stackexchange.com/', 'https://arduino.stackexchange.com/', 
'https://physics.stackexchange.com/', 'https://sqa.stackexchange.com/']

WebBrowserDriver = webdriver.Edge(r"C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftWebDriver.exe")

while CurrentUrl < NumberOfSites:
    WebBrowserDriver.get(myUrls[CurrentUrl])
    time.sleep(SleepTimeinSeconds)
    WebBrowserDriver.refresh()
    CurrentUrl += NextUrl

if CurrentUrl == NumberOfSites:
    WebBrowserDriver.quit()