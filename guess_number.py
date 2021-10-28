import random
computer=random.randint(1,100)
while True:
    number=int(input("请输入100以内的整数："))
    if(number>computer):
        print("大了")
    elif(number<computer):
        print("小了")
    else:
        print("恭喜你赢了")
        break
