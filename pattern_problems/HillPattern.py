# write a program to print 

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


def hillPattern(n):
    for i in range(n):
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")

        for j in range(i+1):
            print("*",end=" ")
        print()

hillPattern(5)