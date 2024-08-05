# write a program to calculate salary of an employee given his basic pay(to be entered by the user), HRA= 10 percent of basic pay,TA = 5 percent of basic pay .define HRA and TA as constants and use then to calculate the salary of the employee

HRA=10
TA=5
basicpay= int(input("Enter the basic pay of the employee : "))
TotalHRA=(HRA*basicpay)/100
TotalTA=(TA*basicpay)/100
totalsalary=basicpay+TotalHRA+TotalTA
print("Total salary of the employee is",totalsalary)