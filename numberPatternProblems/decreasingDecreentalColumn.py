# write a program to print 

#   1 2 3 4 5 
#     1 2 3 4
#       1 2 3
#         1 2
#           1


def decDecrementalColumn(n):
   
    for i in range(n):
        p=1
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print(p,end=" ")
            p+=1
        print()

decDecrementalColumn(5)