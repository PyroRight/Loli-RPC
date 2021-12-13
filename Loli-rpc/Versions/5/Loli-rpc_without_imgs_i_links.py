import time, pypresence, struct, os, colorama

from pypresence import *
from colorama import Fore
from colorama import init
init()

def startup():
    os.system('cls')
    
    print(f"""
    {Fore.RED}                                                                                 
              ██╗      ██████╗ ██╗     ██╗      ██████╗ ██████╗  ██████╗{Fore.YELLOW}  
              ██║     ██╔═══██╗██║     ██║      ██╔══██╗██╔══██╗██╔════╝{Fore.GREEN}
              ██║     ██║   ██║██║     ██║█████╗██████╔╝██████╔╝██║     {Fore.BLUE}
              ██║     ██║   ██║██║     ██║╚════╝██╔══██╗██╔═══╝ ██║     {Fore.CYAN}
              ███████╗╚██████╔╝███████╗██║      ██║  ██║██║     ╚██████╗{Fore.MAGENTA}
              ╚══════╝ ╚═════╝ ╚══════╝╚═╝      ╚═╝  ╚═╝╚═╝      ╚═════╝{Fore.RESET}
    """)

clientidinput = f'[{Fore.BLUE}+{Fore.RESET}] pls say me ur app Client ID: '
rpcstatusinput = f'[{Fore.BLUE}+{Fore.RESET}] pls say me ur app Status: '
rpcdetailsinput = f'[{Fore.BLUE}+{Fore.RESET}] pls say me ur app Details: '
refreshtimeinput = f'[{Fore.BLUE}+{Fore.RESET}] pls say me ur rpc Refresh Time(how fast it need to be updated): '

startup()

clientID = input(f'{clientidinput}')
print(' ')
rpcstatus = input(f'{rpcstatusinput}')
print(' ')
rpcdetails = input(f'{rpcdetailsinput}')
print(' ')
refreshtime = input(f'{refreshtimeinput}')
print(' ')

startup()

print(f'[{Fore.BLUE}+{Fore.RESET}] S-s-senpai ur rpc s-s-started *blushes*')

RPC = Presence(clientID,pipe=1)
RPC.connect()
starttime = int(time.time())

try:
    while True:
        RPC.update(
            state = rpcdetails,
            details = rpcstatus,
            start = starttime,
            buttons = [{"label": button1text, "url": button1link}, {"label": button2text, "url": button2link}]
        )
        time.sleep(int(refreshtime))

except pypresence.exceptions.InvalidPipe as error1:
    print(f"\n[{Fore.RED}!{Fore.RESET}] senpai maybe ur discord not running at the moment sowwy!")
except pypresence.exceptions.InvalidID  as error2:
    print(f"\n[{Fore.RED}!{Fore.RESET}] senpai that client id is not real!")
except struct.error as error3:
    print(f"\n[{Fore.RED}!{Fore.RESET}] Invalid Client ID!")
except pypresence.exceptions.ServerError as error4:
    print(f"\n[{Fore.RED}!{Fore.RESET}] senpai!! make sure u set real link/name/id.")
