# write a program to read a character until a * is encountered.Also count the number of uppercase,lowercase,and numbers entered by the users.
ch= input("Enter a character : ")

lower_count=0
upper_count =0
number_count =0
while(ch!='*'):
    if(ch>='a' and ch<='z'):
        lower_count+=1
    elif(ch>='A' and ch<= 'Z'):
        upper_count+=1
    elif(ch>='0' and ch<='9'):
        number_count+=1
    ch =input("Enter another character or enter '*'  to exit : ")
print("Total number of lower characters entered : ",lower_count)
print("Total number of upper characters entered : ",upper_count)
print("Total number of digits entered : ",number_count)
