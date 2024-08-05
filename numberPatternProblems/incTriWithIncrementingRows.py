# write a program to print 


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# def incrementingRows(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(i+1,end=" ")
#         print()

# incrementingRows(5)


#-----------(or)----------


def incrementingRows(n):
    p=1
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
        p+=1
        print()

incrementingRows(5)
