# write a program to print 
# 5 
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

def decRows(n):
    for i in range(n):
        for j in range(i+1):
            print(n,end=" ")
        n-=1
        print()

decRows(5)

#-----------(or)----------

def decRows(n):
    p=5
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
        p-=1
        print()

decRows(5)