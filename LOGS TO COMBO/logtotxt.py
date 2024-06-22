import easygui,os,re,colorama,ctypes
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
if os.path.exists(os.path.join(os.getcwd(),"Result")):
    pass
else:
    os.mkdir("Result")
class EVO:
    def ui(self):
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'LOG TO TXT  - MADE BY @BINARY_THUG') 
        text = '''    
██╗      ██████╗  ██████╗ ███████╗    ████████╗ ██████╗     ████████╗██╗  ██╗████████╗
██║     ██╔═══██╗██╔════╝ ██╔════╝    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝╚██╗██╔╝╚══██╔══╝
██║     ██║   ██║██║  ███╗███████╗       ██║   ██║   ██║       ██║    ╚███╔╝    ██║   
██║     ██║   ██║██║   ██║╚════██║       ██║   ██║   ██║       ██║    ██╔██╗    ██║   
███████╗╚██████╔╝╚██████╔╝███████║       ██║   ╚██████╔╝       ██║   ██╔╝ ██╗   ██║   
╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝   ╚═╝   
                                                                                                                                                                                                 
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
    def get_path_pass(self,path):
        patho=[]
        for root,dirs,files in os.walk(path):
            for file in files:
                if 'pass' in str(file).lower():
                    passw=os.path.join(root,file)
                    patho.append(passw)
        return set(patho)
    def extract_lines(self, keyword,fi):
        return_list=[]
        with open(fi, "r",errors="ignore",encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if keyword in line:
                if i + 2 < len(lines):
                    captured_lines = lines[i:i + 3]
                    wiscodes=''.join(captured_lines)
                    return_list.append(wiscodes)
                else:
                    continue
        return return_list
    def getinformat(self,list):
        mayat=[]
        
        for lines in list:
            matches = re.findall(r'\w+: (.*?)\n', lines)
            maza=':'.join(matches)
            mayat.append(maza)
        return mayat
    def datetimefolder(self,path):
        current_datetime = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
        shia = os.path.join(path, current_datetime)
        os.mkdir(shia)
        return shia
    def main_converter(self,path,dt):
        try:
            some=self.extract_lines("URL",path)
            if some==[]:
                some=self.extract_lines("url",path)
                if some==[]:
                    some=self.extract_lines("Host",path)
                    
            else:
                pass
            mose=self.getinformat(some)
            op=os.path.join(dt,f"url_pass_log.txt")
            with open(op,'a',errors='ignore',encoding='utf-8') as fuck:
                for lines in mose:
                    clean_lines=str(lines).replace("https://","").replace("http://",'')
                    fuck.write(clean_lines+"\n")
            print(colorama.Fore.GREEN+"[*]"+colorama.Fore.RESET+f"WORKER COMPLET AT {path}")
        except Exception as e:
            print(f"{e}")
            return None
    def runner(self,path,dt):
        with ThreadPoolExecutor(max_workers=5) as meiN_tera:
            for lines in self.get_path_pass(path):
                try:
                    meiN_tera.submit(self.main_converter,lines,dt)
                except:
                    continue
    def main(self):
        self.ui()
        if os.path.exists(os.path.join(os.getcwd(),"Result")):
            pass
        else:
            os.mkdir("Result")
        logs=easygui.diropenbox(title="Select log folder")
        s=self.datetimefolder(os.path.join(os.getcwd(),"Result"))
        self.runner(logs,s)
run=EVO()
run.main()
