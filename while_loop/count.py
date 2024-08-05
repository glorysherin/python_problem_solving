# write a program to read the numbers until -1 is encountered.Also count the negative,positive and zeroes entered by the user.
neg=pos=zero=0
print("Enter -1 to exit!")
while(1):
    num=int(input("Enter any number : "))
    if(num==0):
        zero+=1
    elif(num==-1):
        break
    elif(num>0):
        pos+=1
    else:
        neg+=1
print("The count of positive numbers entered :",pos)
print("The count of negative numbers entered :",neg)
print("The count of zeros entered :",zero)
    
