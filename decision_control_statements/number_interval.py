#write a program that prompts the user to enter a number and then print its interval
num = int(input("Enter a number : "))
if(num>=0 and num<10):
    print("The number",num,"lies between the range 0-10")
    
elif(num>=10 and num<20):
    print("The number",num,"lies between the range 10-20")
elif(num>=20 and num<30):
    print("The number",num,"lies between the range 20-30")
else:
    print("The number",num,"is greater than 30")