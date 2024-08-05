def largest(num):
    large=num[0]
    for i in num:
        if i>large:
            large=i
    return large
    
number=[2,45,1,76,2]
largest_num=largest(number)
print(largest_num)