from colorama import Fore, Style, init

init(convert= True)

class UI:
    @classmethod
    def banner(cls):
        logo =f'''{Fore.LIGHTMAGENTA_EX} 
                             ·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ 
                             ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀ ▪▀▄.▀·•█▌▐█
                             ▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
                             ██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▄▄▌██▐█▌
                             ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀▀▀ ▀▀ █▪  
                                                                    by Nightfall#2512{Style.RESET_ALL}
        '''
        print(logo)   

    @classmethod
    def start_menu(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                  [1] Start
                                                  [2] Exit 
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 

    @classmethod
    def menu2(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                 [1] Threading
                                                 [2] No Threading
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 


        