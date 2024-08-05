# write a program that prompts the user to enter a number between 1-7 and then displays the corresponding day of the week
num= int(input("Enter the number between 1 to 7 : "))
if(num==1):
    print("sunday")
elif(num==2):
    print("monday")
elif(num==3):
    print("tuesday")
elif(num==4):
    print("wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("friday")
elif(num==7):
    print("saturday")
else:
    print("wrong input")
