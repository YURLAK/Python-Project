#Import
import time
#Def
def add_p(information):
    with open("People.txt","a") as file:
        file.write(information+"\n")
        time.sleep(2)
        print("...Done...")
print("*********File v1.0*********")
print(" 1.Use p.add to add file.")
print(" 2.Use p.exit to over the code.")
#The main
while True:
    i = input(str(">>>"))
    if i == "p.add":
        information = input("Information:")
        add_p(information)
    elif i == "p.exit":
        break
    else:
        print("SyntaxError")
