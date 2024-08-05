# write a program to print 

#   * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *

def reverseHillPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")

        for j in range(i,n-1):
            print("*",end=" ")


        for j in range(i,n):
            print("*",end=" ")
        print()

reverseHillPattern(5)

# ------------(or)-----------



# def reverseHillPattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(" ",end=" ")

#         for j in range(i,n):
#             print("*",end=" ")


#         for j in range(i+1,n):
#             print("*",end=" ")
#         print()


# reverseHillPattern(5)