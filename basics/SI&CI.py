# write a program to calculate simple interest and compound interest 
P=int(input("Enter the principle amount : "))
N=int(input("Enter the No of years : "))
R=float(input("Enter the rate of interest in % : "))
SI=(P*N*R)/100
print("The value of SI is:",SI)
CI= P*(1+(R/100))**N-P
print("The value of CI is:",CI)