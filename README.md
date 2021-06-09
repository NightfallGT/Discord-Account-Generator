# Discord-Account-Generator
Proof of concept of how the creation of Discord accounts can be automated without the need to type/click buttons on browser.

## About
A script that automates creating discord accounts. It shows how accounts can be created automatically without the user typing unless there is a captcha (h-Captcha just needs to be clicked) . It automatically verifies your Discord account via email for you and automatically saves login info in `login.txt` in `email:password:token` format. This is used for educational purposes only.

## Chromedriver Fix
If Chrome doesn't open/crashes, try getting the latest version of chromedriver.exe here > https://chromedriver.chromium.org/downloads. Replace the current chromedriver.exe in the folder with the latest version you have downloaded

Make sure your chromedriver.exe file is the same version as your current Chrome web browser version. To check your current Chrome version,
paste chrome://settings/help in chrome.

## Account Disable Bypass 
Reason: **Temporary email detected when joining a server**

There is a 99% chance that your account will get disabled when you try joining a server.
This happens because Discord detects suspicious activity when a temporary email is used. 

To bypass this, you should not join any server using a temporary email to make the account look authentic as possible.

After running Discord Account Generator and verifying your email, go to your Discord account settings and temporarily change the generated account's email to a legitimate one. (a real gmail account will do; temporary only) After doing so, join any server of your choice. (Remember that you cannot join any server using a temporary email or else it will get disabled). After that change back to the temporary email before, and to re-verify again, go to `https://www.gmailnator.com/#` `+` `the email that was used previously` . For example, to access the temp email, you do `https://www.gmailnator.com/#ran.do.me.mail@gmail.com`. 

## Features
- Auto scrape email
- Random username from list
- Random password
- Random date
- Auto-email-verify
- Automatically get Discord token and other login info
- Proxy support
- Multi-threading

## Preview
![Picture](https://i.ibb.co/SvsPwrD/Screenshot-525.png)

## Usage
1. You can customize usernames by editing the usernames in discord_usernames.txt.
2. Run the file and use normal mode if you are a inexperienced with proxies and theading.

### Get Python
If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

### Run via Python
1. install the required modules
```
pip install selenium
pip install undetected-chromedriver
pip install colorama
pip install bs4
pip install lxml
pip install requests
```

2. To run the script..
```
python discordgenerator.py
```

#### Proxy support
- If you want to use proxies, simply paste the proxies in config/proxies.txt.  If you want to stop using proxies, just remove all the proxies from the .txt file. The script automatically checks for proxies on startup. HTTP proxies are only supported as of now. If the proxies are not alive, the script will throw a WebDriver error.

#### Threading mode 
- Uses multiple chrome windows
- Only run this when you have proxies or else one of you Chrome windows will get rate limited.
- Do put more than 6 threads unless you think your PC can handle it. I recommend using 2-3 threads.

#### No Threading
- This only uses one chrome window. 

#### FAQ
Where can i found my generated accounts?

1. It is located in the output folder. Open up login.txt to see the accounts 
that has been generated.

