#write a program to take input from the user and check whether it is a number or a character.If it is a character,determine whether it is in uppercase or lowercase
ch= input("Enter a character : ")
if(ch>='a'and ch<='z'):
    print("lowercase character was entered")
elif(ch>='A' and ch<='Z'):
    print("uppercase character was entered")
elif(ch>='0' and ch<='9'):
    print("number was entered")