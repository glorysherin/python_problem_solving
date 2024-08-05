#write a program to calculate roots of a quadratic equation
#-b +-root(b2-4ac)/2a
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
d=(b**2)-(4*a*c)
deno=2*a
if(d>0):
    root1=(-b +d**0.5)/deno
    root2=(-b -d**0.5)/deno
    print("Root1 =",root1,"Root2 =",root2)
elif(d==0):
    print("Equal roots")
    root1=(-b/deno)
    print("Root1 and Root2 =",root1)

else:
    print("Imaginary Roots")
    
    

