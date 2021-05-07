import undetected_chromedriver as uc
uc.install()

import os
import time 
import requests
import random
import string
import sys
import threading
import datetime
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init 
from bs4 import BeautifulSoup as soup
from sys import stdout
from src import UI
from src import GmailnatorRead, GmailnatorGet, dfilter_email, pfilter_email, find_email_type

init(convert=True)

lock = threading.Lock()

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(length))  

# def minute_timer():
#     while True:
#         elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start))
#         os.system(f'title Discord Generator ^| Rate Limit Timer ^| Time Elapsed {elapsed}')
#         time.sleep(0.05)
#         if elapsed == '00:01:00':
#             print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Timer finished.")
#             break

def gather_proxy():
        proxies = []
        with open('config/proxies.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            for line in lines:
                proxies.append(line.replace('\n', ''))
        return proxies

def free_print(arg):
    lock.acquire()
    stdout.flush()
    print(arg)
    lock.release()   

class DiscordGen:
    def __init__(self, email, username, password, proxy=None):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if proxy:
            options.add_argument('--proxy-server=%s' % proxy)

        self.driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

        self.email= email
        self.username = username
        self.password = password


    def register(self):
        self.driver.get('https://discord.com/register')

        free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Webdriver wait")
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.email)                          
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.email)

        free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.username)
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(self.username)

        free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} " +self.password)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password)

        free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL}" +' Random Date')

        dateWorking = False

        #sometimes different discord languages have different xpath locations

        try: #if date could not be found via divs
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
            dateWorking = True
                              
        except:
            free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} " + 'Error in typing date. Please type the date manually.')
            input(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Submit your form manually. Have you solved captcha? [y/n] > ")
            dateWorking = False

        if dateWorking:
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
                free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Could not find button. Ignoring..")
                pass

            #input(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Press ENTER to create account.')
            self.driver.find_element_by_class_name('button-3k0cO7').click() # Submit button        
            free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Submit form')

        while True:
            lock.acquire()
            checker = input(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Have you solved the captcha and submit? [y/n] > ")
            lock.release()
            if checker == "y":
                self.token = self.driver.execute_script("let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token")
                break
                return True
            elif checker =="n":
                sys.exit()

        return False

    def verify_account(self,link):
        self.driver.get(link)
        free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Task complete")

    def close_driver(self):
        self.driver.close()

def start_verify(email, email_type):  #email, 'dot'/'plus'
    free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Checking email inbox.')
    raw_email = email

    if email_type == 'dot':
        email = dfilter_email(raw_email)


    if email_type == 'plus':
        email = pfilter_email(raw_email)

    g = GmailnatorRead(email, raw_email, email_type)

    retry_count = 1

    while retry_count <= 6:
        gmailnator_inbox = g.get_inbox()
        for x in range(len(gmailnator_inbox)):  # for each email
            discord_keywords = re.findall('Discord', gmailnator_inbox)

            if 'Discord' in discord_keywords:
                #retrive messages from inbox
                bs = soup(gmailnator_inbox[x], 'html.parser')
                href_links = [a['href'] for a in bs.find_all('a')]

                first_message = href_links[0] #get first message which is most likely from Discord verify.

                remove = re.compile('(^.*?(?=[#])[#])') #only get id; remove unnecessary stuff
                first_id = remove.sub('', first_message)
                
                message_html = g.get_single_message(first_id)
                content_html = soup(message_html, 'html.parser')

                message_links = [a['href'] for a in content_html.find_all('a')]

                try:
                    discord_verify = message_links[1]
                    free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Extracted discord link.')
                except IndexError:
                    free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} List index out of range.')
                    discord_verify = None

                return discord_verify

            else:
                free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Discord keyword not found in that email. Trying an other one...')
        free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Inbox empty. Retry count: {retry_count}')
        free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Sleeping for 15 seconds. Waiting for Discord email.')
        time.sleep(15)
    free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Discord keyword not found. Unable to verify account via email.')
    return False  # cant find any email with the word discord in it

def worker(proxy=None):
    if proxy:
        free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Proxy used {proxy} ")
    free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Scraping email. ")

    g = GmailnatorGet()
    new_email = g.get_email()
    
    free_print(f"{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} Scraped {new_email}")
 
    email_type = find_email_type(new_email)

    if email_type =='dot':
        filtered_email = dfilter_email(new_email)

    if email_type == 'plus':
        filtered_email = pfilter_email(new_email)

    discord_usernames = []
    with open('config/discord_usernames.txt', 'r', encoding='UTF-8') as username_txt:
        lines = username_txt.readlines()
        for line in lines:
            discord_usernames.append(line.replace('\n', ''))

    username = random.choice(discord_usernames)
    password = password_gen()

    if not proxy:
        d = DiscordGen(new_email, username, password)

    if proxy:
        d = DiscordGen(new_email, username, password, proxy = proxy)

    try:
        d.register()
        token = str(d.token)
        lock.acquire()
        with open('output/login.txt', 'a', encoding='UTF-8') as login_file:
            login_file.write(new_email + ':' + password + ':' + token + '\n')      
        lock.release()
        try:
            verify_link = start_verify(new_email, email_type)
            if verify_link:
                d.verify_account(verify_link)
                os.system('pause>nul')
                d.close_driver()

            else:
                d.verify_account('https://www.gmailnator.com/inbox/#' + new_email)
                os.system('pause>nul')

        except Exception as e:
            print('some error occured')
            print(e)
            d.verify_account('https://www.gmailnator.com/inbox/#' + new_email)
            os.system('pause>nul')
            d.close_driver()   
                     
    except WebDriverException:
        free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Webdriver Error. Unable to continue.")

    free_print(f"{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Worker task ended.")
    
def menu():
    proxies = gather_proxy()

    os.system('cls')

    if len(proxies) != 0:
        os.system('title Discord Generator ^| coded by NightfallGT ^| PROXY LIST DETECTED')

    else:
        os.system('title Discord Generator ^| coded by NightfallGT ')
    UI.banner()
    UI.start_menu()

    try:
        user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
        print('\n\n')
    except ValueError:
        user_input = 0

    if user_input == 1:
        os.system('cls')
        UI.banner()
        UI.menu2()

        try:
            user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
            print('\n\n')
        except ValueError:
            user_input = 0

        if user_input == 1:
            return 2

        elif user_input == 2:
            return 1

        else:
            return None
            
def main():
    continue_program = True

    m = menu()

    if m == 1:
        user_thread= True
    elif m == 2:
        user_thread = False
    else:
        continue_program = False

    if continue_program:
        if user_thread:
            print(f"{Fore.LIGHTMAGENTA_EX}[WARNING]{Style.RESET_ALL} Do not put a lot of threads or you will crash. 2 threads is decent. (chrome windows)")
            num_thread = int(input(f"{Fore.LIGHTMAGENTA_EX}[>]{Style.RESET_ALL} Enter number of threads [eg. 3] > "))
        
        proxies = gather_proxy()

        os.system('cls')
        UI.banner()
        print('\n\n')

        if user_thread:

            threads = []

            if len(proxies) != 0:
                os.system('title Discord Generator ^| Proxy: True ^| Threading: True')

                for i in range(num_thread):
                    t = threading.Thread(target=worker, args= (random.choice(proxies), ))
                    threads.append(t)
                    t.start()
            else:
                os.system('title Discord Generator ^| Proxy: False ^| Threading: True')

                for i in range(num_thread):
                    t = threading.Thread(target=worker)
                    threads.append(t)
                    t.start()
        else:
            if len(proxies) != 0:
                os.system('title Discord Generator ^| Proxy: True ^| Threading: False')
                worker(random.choice(proxies))

            else:
                os.system('title Discord Generator ^| Proxy: False ^| Threading: False')
                worker()    

if __name__ == '__main__':
    main()
