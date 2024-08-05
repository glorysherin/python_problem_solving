# write a program to enter a decimal number.calculate and display the binary equivalent of this number.
deci_num = int(input("Enter a decimal number : "))
bin_num=0
i=0
num=deci_num
while(deci_num!=0):
    remainder=deci_num%2
    bin_num =bin_num+remainder*(10**i)
    deci_num//=2
    i+=1
print("the binary num equivalent to decimal number",num,"is",bin_num)

