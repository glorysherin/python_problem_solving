# write a program to find the greatest number from three numbers.
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
if(a>b and a>c):
    print("a is greater than b and c")
elif(b>a and b>c):
    print("b is greater than a and c")
else:
    print("c is greater than a and b")
