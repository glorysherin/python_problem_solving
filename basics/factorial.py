num=int(input("Enter a number : "))
fact=1
if num==0:
    fact=1

if num>1:
    for i in range(2,num+1):
        fact= fact*i
    print(fact)