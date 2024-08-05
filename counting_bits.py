n= int(input("Enter a number"))
bin=0
i=0
index=0
count=[]
while(n!=0):
    remainder= n%2
    bin=bin+remainder*(10**i)
    n //=10
    i=i+1

    

print(bin)
bins=str(bin)
print(type(bins))
for a in bins:
    if a==1:
        print("index = ",a)
    index+=1