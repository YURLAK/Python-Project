import random
import sys
import time
from colorama import Fore

i=1 #init time
r=0 #correct
f = True
ask = input(str("What's your name:"))
time.sleep(1)
print("ok,start after 3 second")
time.sleep(1)
num=3
for b in range(3):
    print(num)
    num -= 1
    time.sleep(1)
print(Fore.GREEN+"***********************")
for i in range(10):
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    anwser = input(Fore.YELLOW+f"{num1} + {num2} = ")
    try:
        if int(anwser) == int(num1+num2):
            print(Fore.LIGHTGREEN_EX+"Right!")
            r += 1
        else:
            print(Fore.LIGHTRED_EX+"Cross!")
    except ValueError:
        print(Fore.RED+"input number!")
        f = False
        break
time.sleep(1)
if f == True:
    c = r/10*100
    print(Fore.BLUE+"你的口算正确率是 ",c,"%")
    with open('算正确率.txt',"a") as file:
        file.write(ask)
        file.write(" ")
        file.write(str(c))
        file.write("%")
        file.write("\n")
else:
    sys.exit()
