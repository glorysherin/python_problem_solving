# write a program to print 
#   * * * * *
#   * * * * 
#   * * * 
#   * * 
#   * 

def decreasingTriangle(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()


decreasingTriangle(5)