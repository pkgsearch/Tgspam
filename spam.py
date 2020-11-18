 
from telethon import TelegramClient, events, sync
import os
from colorama import Fore, Back, Style

def cls():
    os.system('clear')

api_id = int(input(Fore.MAGENTA + " API ID: "))
api_hash = input(" API Hash: ")

client = TelegramClient('session_name', api_id, api_hash)

client.start()

cls()
      
print(Fore.CYAN + '''
███████  ▒███▒  ▓███▒ █████░   ██   █▒  ▒█
   █    ░█▒ ░█ █▓  ░█ █   ▓█   ██   ██  ██
   █    █▒     █      █    █  ▒██▒  ██░░██
   █    █      █▓░    █   ▓█  ▓▒▒▓  █▒▓▓▒█
   █    █   ██  ▓██▓  █████░  █░░█  █ ██ █
   █    █    █     ▓█ █       █  █  █ █▓ █
   █    █▒   █      █ █      ▒████▒ █    █
   █    ▒█░ ░█ █░  ▓█ █      ▓▒  ▒▓ █    █
   █     ▒███▒ ▒████░ █      █░  ░█ █    █                      
 PKGSEARCH
 
''')
      
print(Fore.GREEN + """
 [1] Бесконечный секс 
 [2] Секс с указанным количеством впихов 
""")


a = input(Fore.YELLOW + ' Выберите способ впиха: ')

if a == "1":
    print(" ")
    print(Fore.BLUE + " ")
    idp = input("Введите id/nick пизды: ")
    mes = input("Текст хуя ")
    print(Fore.RED + '   Секс начат! ')
    while True:

        client.send_message(idp, mes)

elif a == "2":
    print(" ")
    print(" ")  
    px = int(input(Fore.BLUE + " Введите количество впихов: "))
    idp = input("  id/nick пизды: ")
    mes = input(" Текст хуя: ")
    print(Fore.RED + '   Секс начат! ')
    for i in range(px):
        client.send_message(idp, mes)

else:
    print(" Нету такого хуя ")
