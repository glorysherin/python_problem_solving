# write a program to determine whether a person is eligible to vote.
age= int(input("enter your age : "))
if(age>=18):
    print("you're eligible to vote!!")
else:
    years= 18-age
    print("you're not eligible to vote,you have to wait for",years,"years to vote!!")