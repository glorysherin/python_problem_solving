# print("Hello World!!")
# print("hlo")
# from utils.py import *

def Addition():
    result= a+b
    print(result)

def subtraction():
    result=a-b
    print(result)

def multilication():
    result=a*b
    print(result)



a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
while(True):
    print("choose 1 for Addition")
    print("choose 2 for subtraction")

    print("choose 3 for multilication")

    print("choose 0 for exit")


    choice=int(input(':'))
   
    if(choice==1):
        Addition()
    elif(choice==2):
       subtraction()
    elif(choice==3):
       multilication()
    elif(choice==0):
        break
    else:
        print("wrong input choose another operation")
