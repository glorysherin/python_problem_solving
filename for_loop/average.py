# write a program using for loop to calculate the average of first n natural numbers.
n=int(input("Enter a number : "))
sum=0
for i in range(n+1):
    sum+=i
average=sum/n

print("Sum of",n,"numbers is :",sum)
print("Average of",n,"numbers is :",average)