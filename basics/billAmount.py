# write a program to calculate the bill amount for an item given its quatity sold,value,discount, and tax.
Quantity = float(input("Enter the number of items sold : "))
Value = float(input("Enter the Value of the item : "))
Discount = float(input("Enter the Discount percentage : "))
Tax = float(input("Enter the Tax : "))
total=Quantity*Value
discount_amt = (total*Discount)/100
sub_total = total-discount_amt
taxAmount = (sub_total*Tax)/100
totalAmount = sub_total+taxAmount
print("*****Bill******")
print("Quantity sold:",Quantity)
print("price per item:",Value)
print("----------------")
print("Amount:",total)
print("Discount: -",discount_amt)
print("----------------")
print("Discountes Total: -",sub_total)

print("taxAmount:+",taxAmount)
print("----------------")

print("totalAmount to be paid is:",totalAmount)


