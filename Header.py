from requests import head, get, post
from pystyle import Colorate, Colors
import sys
from os import system

system('cls || clear')


print(Colorate.Horizontal(Colors.red_to_blue, '  Created By Laster ', 1))


method = input(Colorate.Horizontal(Colors.red_to_blue, '\n  Method => ', 1))
url = input(Colorate.Horizontal(Colors.red_to_blue, '\n  Url => ', 1))


if method == 'head':
    res = head(url)
elif method == 'get':
    res = get(url)
elif method == 'post':
    res = post(url)


with open('info.txt', 'w') as f:
    sys.stdout = f  
    print(res.headers)
    sys.stdout = sys.__stdout__  

print("saved to 'info.txt'")
