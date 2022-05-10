import urllib
import requests
import sys
from colorama import Fore
def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
def chat():
    msg = input().rstrip()
    print("你>", msg)
    res = qingyunke(msg)
    print("青云客>", res)
def main():
    print("*****聊天机器人*****")
    print(" 1.聊天")
    print(" 2.退出")
    choice = input(">>>")
    if choice == 1:
        chat()
    elif choice == 2:
        sys.exit(0)
