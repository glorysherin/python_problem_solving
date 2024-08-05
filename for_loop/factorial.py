# write a program using for loop to calculate factorial of a number.

# if(num==0):
#     fact=1
# fact=1
# for i in range(1,num+1):
#     fact= fact*i
# print("The factorial of",num,"is :",fact)
# def fib(n):
#     if n<2:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input("Enter :"))
# # for i in range(n):
# print(fib(n))

n= int(input("Enter num: "))
nle=str(n)
digit=len(nle)
temp=n
sum=0
while n>0:
    rem= n%10
    sum+=rem**digit
    n//=10

if(sum==temp):
    print("Amstr")
else:
    print("Not")



