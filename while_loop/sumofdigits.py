# write a program to enter a  number and then calculate the sum of its digits.
num = int(input("Enter a number : "))
sum_of_digits = 0
while(num!=0):
    temp= num%10
    sum_of_digits+=temp
    num//=10
print(sum_of_digits)