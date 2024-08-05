# write a program to print 
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def IncreasingIncrementingColumn(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()

IncreasingIncrementingColumn(5)



#----------(or)--------------

def IncreasingIncrementingColumn(n):
    for i in range(n):
        p=1
        for j in range(i+1):
            print(p,end=" ")
            p+=1
        print()

IncreasingIncrementingColumn(5)