import os
import time 
import requests
import random
import string
import sys
import threading
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

init(convert=True)

class DiscordGen:
    def __init__(self, email, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

        self.email= email
        self.username = username
        self.password = password

        self.register()

    def register(self):
        self.driver.get('https://discord.com/register')

        print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Webdriver wait")
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.email)                          
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.email)

        print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.username)
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(self.username)

        print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.password)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password)

        print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL}" +' Random Date')
        self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div').click()

        actions = ActionChains(self.driver)

        actions.send_keys(str(random.randint(1,12)))# Month
        actions.send_keys(Keys.ENTER)
        actions.send_keys(str(random.randint(1,28))) #Day
        actions.send_keys(Keys.ENTER)

        random_year = [1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]

        actions.send_keys(str(random.choice(random_year))) #Year
        actions.perform()
        #Submit form
        try: 
            self.driver.find_element_by_class_name('inputDefault-3JxKJ2').click() # Agree to terms and conditions
        except:
            print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Could not find button. Ignoring..")
            pass

        print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Submit form')
        input(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Press ENTER to create account.')
        self.driver.find_element_by_class_name('button-3k0cO7').click() # Submit button        

        while True:
            checker = input(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Have you solved the captcha and submit? [y/n] > ")
            if checker == "y":
                break
                return True
            elif checker =="n":
                sys.exit()
        return False

    def close_driver(self):
        self.driver.close()
class GmailScrape:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
        self.driver.minimize_window()
        self._get()
        self.emails = self._scrape(self.driver.page_source)

    def _get(self):
        self.driver.get('https://www.gmailnator.com/bulk-emails')
        print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Webdriver wait.')

        try:
            self.driver.find_element_by_xpath('/html/body/section/div[1]/div/div[2]/div/div[2]/div/form/div[1]/label').click()     
        except:
            pass

        self.driver.find_element_by_xpath('//*[@id="generate_button"]').click()

    def _scrape(self, source):
        print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Scraping..')
        soup = BeautifulSoup(source,'lxml')
        emails = []
        anchor_tags = soup.find_all('a')

        for x in anchor_tags:
            emails.append(x.string)
        emails = emails[14:-10]

        return emails

    def get_list(self):
        return self.emails

    def close_driver(self):
        self.driver.close()

def menu():
    os.system('cls')
    os.system('title Discord Generator ^| coded by Nightfall#2512')
    logo =f'''{Fore.LIGHTMAGENTA_EX} 
                            ·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ 
                            ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀ ▪▀▄.▀·•█▌▐█
                            ▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
                            ██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▄▄▌██▐█▌
                            ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀▀▀ ▀▀ █▪  
                                                                  by Nightfall#2512
    '''
    menu =f'''
                                            ╔══════════════════════════════╗
                                                     [1] Start
                                                     [2] Exit 
                                            ╚══════════════════════════════╝    {Style.RESET_ALL}
    '''

    print(logo)
    print(menu)
    try:
        user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
        print('\n\n')
    except:
        user_input = 0
    return user_input

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(length))  

def verify_account(email):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    url = "https://www.gmailnator.com/inbox#" + email
    driver.get(url)
    while True:
        answer = input(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Have you verified your account? [y/n] > ")
        if answer == 'y':
            driver.close()
            break
    return True


def minute_timer():
    while True:
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start))
        os.system(f'title Discord Generator ^| Rate Limit Timer ^| Time Elapsed {elapsed}')
        time.sleep(0.05)
        if elapsed == '00:01:00':
            print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Timer finished.")
            break


if __name__ == '__main__':
    if menu() == 1:
        #Email Method
        print(f"{Fore.LIGHTMAGENTA_EX}[MESSAGE]{Style.RESET_ALL} Please do not close or touch the chrome tab. ")
        print(f"{Fore.LIGHTMAGENTA_EX}[MESSAGE]{Style.RESET_ALL} Login details are saved in output/login.txt")

        g = GmailScrape()
        email_list = g.get_list()
        g.close_driver()

        discord_usernames = []
        with open('config/discord_usernames.txt', 'r', encoding='UTF-8') as username_txt:
            lines = username_txt.readlines()
            for line in lines:
                discord_usernames.append(line.replace('\n', ''))
 
        account_num = 0
        for email in email_list:
            #New instance; create new discord account.
            os.system(f'title Discord Generator ^| Accounts Generated: {account_num}')
            password = password_gen()
            username = random.choice(discord_usernames)
            with open('output/login.txt', 'a', encoding='UTF-8') as login_file:
                login_file.write(email + ':' + password +'\n')            
            d = DiscordGen(email, username, password)

            d.close_driver()
            #Make user verify
            verify_account(email)

            account_num += 1
            os.system(f'title Discord Generator ^| Accounts Generated: {account_num}')

            print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Please wait 1 minute to avoid being rate limited by Discord.")
            start = time.time()
            minute_timer()

            os.system('title Discord Generator ^| coded by Nightfall#2512')

            
