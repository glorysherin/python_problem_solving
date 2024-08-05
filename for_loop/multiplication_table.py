# write a program to print the multiplication table of n, where n is entered by the user.
n= int(input("Enter a number : "))
print("The multiplication table of",n, "is :")
for i in range(1,11):
    tab= n*i
    print(n ,"X",i,"=",tab)