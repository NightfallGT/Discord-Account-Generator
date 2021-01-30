# Discord-Account-Generator
Automate creating discord accounts

## NEW VERSION RELEASED
- Added threading
- Added proxy support
- Auto-verify email 

## About

A script that automates creating discord accounts.

## How to use

- You can customize usernames by editing the usernames in discord_usernames.txt.
- Run the file and use normal mode if you are a beginner/inexperienced with proxies and theading.

## Picture
![Picture](https://i.ibb.co/yPpLGJD/Screenshot-15.png)

### Get Python
If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

### Run via Exe Version
- Extract the .rar file
- Run the exe file 
- Do not take out the program out of the folder

### Run via Python
- install the required modules
```
pip install selenium
pip install colorama
pip install bs4
pip install lxml
```

- to run the script..
```
python discordgenerator.py
```
#### Proxy support
If you want to use proxies, simply paste the proxies in config/proxies.txt. HTTP proxies are only supported as of now.

#### Threading mode 
- Uses multiple chrome windows
- Only run this when you have proxies or else one of you Chrome windows will get rate limited.
- Do put more than 6 threads unless you think your PC can handle it. I recommend using 2-3 threads.

#### No Threading
- This only uses one chrome window. 


### TROUBLESHOOT
ONLY IF IT NOT WORKING
- Make sure your chromedriver.exe file is the same version as your Chrome web browser version
- Download the latest version chromedriver.exe: https://chromedriver.chromium.org/downloads

Then replace the chromedriver.exe file in the folder.

Where can i found my generated accounts?

It is located in the output folder. Open up login.txt to see the accounts 
that has been generated.

