num= int(input("Enter a number : "))
n=num
print("The reverse of the number",n,"is :")
while(num!=0):
    temp = num%10
    num//=10
    print(temp,end=" ")