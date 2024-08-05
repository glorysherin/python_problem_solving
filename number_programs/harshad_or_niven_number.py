# harshad number or niven number is the number which is divisible by sum of its digits
#eg: 156 = 1+5+6=12 -->156/12

n=int(input("Enter a number : "))
m=n
sum=0

while(m!=0):
    r = m%10
    sum+=r
    m//=10
if(n%sum==0):
    print("it is a harshad or niven number")
else:print("not")