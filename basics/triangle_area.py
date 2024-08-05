#area= sqrt(s*(s-a)*(s-b)*(s-c))
a=float(input("Enter a value:"))
b=float(input("Enter b value:"))
c=float(input("Enter c value:"))
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is :",str(area))
