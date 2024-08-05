# write a program to print 
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1

def increasewith1(n):
    for i in range(n):
        for j in range(i+1):
            print("1",end=" ")
        print()

increasewith1(5)