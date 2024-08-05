# write a program to print 
#   * 
#   * *
#   * * * 
#   * * * * 
#   * * * * *


def increasingTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="  ")
        print()

increasingTriangle(5)