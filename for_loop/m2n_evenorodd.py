# write a program using for loop to print all the numbers from m-n thereby classifying them as even or odd.
m= int(input("Enter m value : "))
n = int(input("Enter n value : "))
for i in range(m,n+1):
    if(i%2==0):
        print(i,"is even number")
    else:
        print(i,"is odd number")