# write a program to print 
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *



def sqrPattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()


sqrPattern(5)
