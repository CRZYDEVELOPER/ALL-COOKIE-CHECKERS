import os
os.system("pip install easygui")
os.system("pip install colorama")
from datetime import datetime
import ctypes,colorama
import threading
colorama.init()
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
import easygui
class LOGSTOCOMBOS:
    def __init__(self) -> None:
        pass
    def remove_httpplines(self,txfile):
        CLEAN_TXT=[]
        with open(txfile,'r',errors='ignore',encoding='utf-8') as hunt:
            for lines in hunt.readlines():
                if 'https://' in lines  or 'http://' in lines or 'android://':
                    cleanlines=str(lines).replace('https://','').replace('http://','').replace("android://",'')
                    CLEAN_TXT.append(cleanlines)
        return set(CLEAN_TXT)
    def findkeyword(self,keyword,list,dt):
        
        for lines in list:
            if keyword in str(lines).lower():
                group=str(lines).split(':')
                group.pop(0)
                user_pass=':'.join(group)
                if "\\" or "/" in str(keyword):
                    mkey=str(keyword).replace("/",".").replace("\\",".")
                else:
                    mkey=str(keyword)
                outputpath=os.path.join(dt,f"[{mkey}].txt")
                with open(outputpath,'a',errors='ignore',encoding='utf-8') as neend:
                    neend.write(user_pass)
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'LOGS TO COMBO- MADE BY @BINARY_THUG') 
        text = '''    
██╗      ██████╗  ██████╗ ███████╗    ████████╗ ██████╗      ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ███████╗
██║     ██╔═══██╗██╔════╝ ██╔════╝    ╚══██╔══╝██╔═══██╗    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗██╔════╝
██║     ██║   ██║██║  ███╗███████╗       ██║   ██║   ██║    ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║███████╗
██║     ██║   ██║██║   ██║╚════██║       ██║   ██║   ██║    ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║╚════██║
███████╗╚██████╔╝╚██████╔╝███████║       ██║   ╚██████╔╝    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                                                                                                                                                 
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

def datetimefolder(path):
    current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    shia = os.path.join(path, current_datetime)
    os.mkdir(shia)
    return shia     
sas=LOGSTOCOMBOS()
sas.ui()
#sasi=sas.remove_httpplines("[26.273.160] cleaned_urllogpass.txt")
y=easygui.fileopenbox(title="SELECT URL LOG TXT FILE",filetypes=["*.txt"],multiple=False)
keywordtxfile=easygui.fileopenbox(title="SELECT keyword files",filetypes=["*.txt"],multiple=False)
s=datetimefolder(os.path.join(os.getcwd(),'Result'))
rat=sas.remove_httpplines(y)
with open(keywordtxfile,'r',errors='ignore',encoding='utf-8') as death:
    for keys in death.readlines():
        threading.Thread(target=sas.findkeyword,args=(str(keys).replace('\n',''),rat,s,)).start()
