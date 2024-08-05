from utils.py import *
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
    if(choice==2):
       subtraction()
    if(choice==3):
       multilication()
    if(choice==0):
        break


