# write a program to calculate the sum and average of first 10 numbers.
i=0
sum=0
while(i<=10):
    sum +=i
    i +=1
print("sum =",str(sum))
avg=float(sum)/10

print("average =",str(avg))