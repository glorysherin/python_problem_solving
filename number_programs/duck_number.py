# Duck number : A number which has zeros present in it 
# eg: 408, 280
# The same can be used to find other numbers too or can be used to count the number of digits present in the number.


n= int(input("Enter a number :"))
count=0

while(n!=0):
    r= n%10
    if(r==0):
        count+=1
    n//=10
if(count>0):
    print("It is a Duck Number")
else:
    print("NOT")