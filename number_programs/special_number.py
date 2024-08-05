#special number : sum of the digits is add with the products of the digits
# 59 = 5 + 9 + 5 * 9


n= int(input("Enter a number :"))
m=n
sum=0
prod=1
total=0
 
while m!=0:
    r=m%10
    sum+=r
    prod*=r
    m//=10

total+=sum+prod
if(n==total):
    print("It is a special number")
else:
    print("not")
