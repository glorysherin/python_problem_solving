n= int(input("Enter a number :"))

m=n
sum=0
while(m!=0):
    r=m %10
    sum=sum*10+r
    m//=10
if(sum==n):
    print("PAlindrome")
else:print("not")