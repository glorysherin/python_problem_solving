# write a program to print 
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *


def rightsideddecreasingTriangle(n):
    for i in range(n):

        for j in range(i+1):
            print(" ",end=" ")

        for j in range(i,n):
            print("*",end=" ")

        print()


rightsideddecreasingTriangle(5)