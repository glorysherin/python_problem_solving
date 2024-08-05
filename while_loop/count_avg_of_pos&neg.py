# write a program to read the numbers until -1 is encountered. Find the average of positive and negative numbers entered by the user.
print("Enter -1 to exit!!")
pos_count=neg_count=0
pos=neg=0
num= int(input("Enter a number"))

while(True):

    if(num == -1):
        break
    elif(num>=0):
        pos_count+=1
        pos+=num
    else:
        neg_count+=1
        neg+=num
    
    num= int(input("Enter a number"))

avg_pos=float(pos/pos_count)
avg_neg=float(neg/neg_count)
print("The avg of pos =",avg_pos)
print("The avg of pos =",avg_neg)
    