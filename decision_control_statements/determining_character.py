# write a program to determine the character entered by the user.
ch = input("Enter a charcter or press any key : ")
if(ch.isalpha()):
    print("The character entered by the user is alphabetic character!!")
elif(ch.isdigit()):
        print("The character entered by the user is a number/numeric!!")
elif(ch.isspace()):
          print("The character entered by the user is whitespace!!")
else:
           print("The character entered by the user is a special character!!")


