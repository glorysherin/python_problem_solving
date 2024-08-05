# write a program to determine whether the character entered is a vowel or not.
ch= input("Enter a character : ")
vowels=['a','e','i','o','u','A','E','I','O','U']
if(ch in vowels):
    print("It is a vowel")
else:
    print("It is not a vowel")