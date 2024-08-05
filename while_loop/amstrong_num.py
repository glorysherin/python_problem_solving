# write a program to find whether the given number is an amstrong number or not.
n=int(input("Enter a number:"))
s=0
num=n
while(n>0):
    r=n%10
    s+=r**3
    n=n//10
if(s==num):
    print("It is an amstrong number")
else:
    print("It is not an amstrong number")