# Momentum is calculated as e = mc**2 , where m is the mass of the object and c is its velocity. write a program that accepts an object's mass (in kilograms) and velocity (in meters per second) and displays its momentum.
m = float(input("Enter the mass of the object in kilograms : "))
c = float(input("Enter the velocity in meters per second : "))
e= m*(c**2)
print("The Momentum of the object with mass",str(m)+"kg and velocity",str(c)+"meter per second is :",str(e))