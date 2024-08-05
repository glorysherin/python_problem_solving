# write a program to enter a binary number and convert it into decimal number.
bin_num = int(input("Enter a binary number : "))
bnum= bin_num
i=0
decimal=0
while bin_num!=0 :
    remainder =bin_num%10
    decimal = decimal +remainder *(2**i)
    bin_num //=10
    i+=1
print("The decimal number equivalent to binary number",bnum,"is :",decimal)