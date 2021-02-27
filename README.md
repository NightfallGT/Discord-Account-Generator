# Discord-Account-Generator
Proof of concept of how Discord accounts can be created without the need to type/ click buttons on a browser.

### NEW VERSION 
1. Added threading
2. Added proxy support [HTTP] (username and password proxies not supported yet)
3. Auto-verify email 

## About

A script that automates creating discord accounts. It shows how accounts can be created automatically without the user typing unless there is a captcha. This is used for educational purposes only

## Preview
![Picture](https://i.ibb.co/yPpLGJD/Screenshot-15.png)

## Usage

1. You can customize usernames by editing the usernames in discord_usernames.txt.
2. Run the file and use normal mode if you are a beginner/inexperienced with proxies and theading.

### Get Python
If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

### Run via Python
1. install the required modules
```
pip install selenium
pip install colorama
pip install bs4
pip install lxml
pip install requests
```

2. To run the script..
```
python discordgenerator.py
```

### Run via Exe Version
1. Extract the .rar file
2. Run the exe file 
3. Do not take out the program out of the folder


#### Proxy support
If you want to use proxies, simply paste the proxies in config/proxies.txt.  If you want to stop using proxies, just remove all the proxies from the .txt file. The script automatically checks for proxies on startup. HTTP proxies are only supported as of now.

#### Threading mode 
- Uses multiple chrome windows
- Only run this when you have proxies or else one of you Chrome windows will get rate limited.
- Do put more than 6 threads unless you think your PC can handle it. I recommend using 2-3 threads.

#### No Threading
- This only uses one chrome window. 


#### TROUBLESHOOT
ONLY IF IT IS NOT WORKING
1. Make sure your chromedriver.exe file is the same version as your Chrome web browser version
2. Download the latest version chromedriver.exe: https://chromedriver.chromium.org/downloads

Then replace the chromedriver.exe file in the folder.

Where can i found my generated accounts?

It is located in the output folder. Open up login.txt to see the accounts 
that has been generated.

