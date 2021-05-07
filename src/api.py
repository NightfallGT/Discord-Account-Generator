import requests
import re
from colorama import Fore, Style, init 

init(convert=True)

class Gmailnator:
    BASE_URL = 'https://www.gmailnator.com/'

    HEADERS = {
        'authority': 'www.gmailnator.com',
        'sec-ch-ua': '^\\^Google',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.gmailnator.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.gmailnator.com/inbox/',
        'accept-language': 'en-US,en;q=0.9,',
        'sec-gpc': '1'
    }
    def __init__(self):
        self.s = requests.Session()      
        self.csrf_token = self.__get_csrf()
  
    def __get_csrf(self):
        response = self.s.get(self.BASE_URL)
        csrf_token = response.cookies.get('csrf_gmailnator_cookie')
        return csrf_token

class GmailnatorRead(Gmailnator):
    def __init__(self, email, raw_email, types):
        super().__init__()

        self.type = types
        self.email = email
        self.raw_email = raw_email

    def __get_email_name(self):
        name_only = '(^.*?(?=[%|@])[%|@])'
        x = re.search(name_only, self.email)
        filter0 = x.group()

        filter1 = filter0.replace('%', '')
        filter2 = filter1.replace('@', '')

        return filter2

    def __requests_mailbox(self):                         
        if self.type == 'dot':
            data= f'csrf_gmailnator_token={self.csrf_token}&action=LoadMailList&Email_address={self.raw_email}'

        if self.type == 'plus':                                                                             
            data= f'csrf_gmailnator_token={self.csrf_token}&action=LoadMailList&Email_address={self.email}'

        r = self.s.post(self.BASE_URL+ 'mailbox/mailboxquery', data=data, headers=self.HEADERS)
        return r

    def get_inbox(self):
        json_inbox = self.__requests_mailbox().json()
        inbox_content = []
        try:
            for email in range(len(json_inbox)):
                inbox_content.append(str(json_inbox[email]['content']))

        except Exception as e:
            print(e)
            inbox_content = ''

        return inbox_content

    def get_single_message(self, msg_id):     
        email_name = self.__get_email_name()
        data= f'csrf_gmailnator_token={self.csrf_token}&action=get_message&message_id={msg_id}&email={email_name}' #176e703fdac43408 #pulltmp

        r = self.s.post(self.BASE_URL + 'mailbox/get_single_message/', data=data, headers=self.HEADERS)

        return r.json()['content']


class GmailnatorGet(Gmailnator):
    def __init__(self):
        super().__init__()
  
    def get_email(self):
        payload = {
            'csrf_gmailnator_token': self.csrf_token,
            'action': 'GenerateEmail',
            'data[]': 1,
            'data[]': 2,
            'data[]': 3,
        }

        r = self.s.post('https://www.gmailnator.com/index/indexquery', data=payload)
        return r.text


def dfilter_email(email):
    at_replace = email.replace('@', '%40')

    dot_replace = at_replace.replace('.', '')

    final = dot_replace.replace('com', '.com')
    return final

def pfilter_email(email):
    at_replace = email.replace('@', '%40')

    plus_replace = at_replace.replace('+', '%2B')

    return plus_replace

def find_email_type(email):
    dot_counter = 0
    for i in email:
        if i == '+':
            return 'plus'
        if i == '.':
            dot_counter += 1
        if dot_counter > 1:
            return 'dot'
