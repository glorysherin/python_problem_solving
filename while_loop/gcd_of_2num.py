# write a program to calculate GCD of two numbers.
def gcd(a,b):
    if(a>b):
        print (b)
    elif(a%b !=0):
        r=a%b
        print(gcd(a,r))
gcd(2,3)