# write a program to swap two numbers using a temporary variable

A= input("Enter the first value : ")
B= input("Enter the second value : ")
print("The first value before swapping is :",A)
print("The second value before swapping is :",B)
Temp=A
A=B
B=Temp
print("The first value after swapping is :",A)
print("The second value after swapping is :",B)
print(Temp)