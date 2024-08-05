#spy number: sum of the digits is equal to the product of the digits


n= int(input("Enter a number :"))
sum=0
prod=1

while n!=0:
    r=n%10
    sum+=r
    prod*=r
    n//=10

    
print(sum)
print(prod)
if(sum==prod):
    print("It is a spy number")
else:
    print("not")