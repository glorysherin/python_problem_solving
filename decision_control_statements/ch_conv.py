#write a program to enter any character.if the entered character is in lowercase then convert it into uppercase and if it is an uppercase character,then convert it into lowercase.
ch=input("Enter any character : ")
if(ch>='a' and ch<='z'):
    print("The character",ch,"in uppercase is",ch.upper())
elif(ch>='A' and ch<= 'Z'):
    print("The character",ch,"in lowercase is",ch.lower())
else:
    print("Please enter a alphabetical character!")