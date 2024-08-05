n=int(input("Enter a num:"))

sum=0
num=n
while n>0:
    remainder=n%10
    sum+=(remainder**len(str(n)))
    n//=10
if sum==num:
    print("Amstrong")
else:
    print("not")