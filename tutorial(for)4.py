# find the no of digits in a number using for each 
num= abs(int(input("Enter a number ")))
strnum = str(num)
digits = 0
for i in strnum:
    digits = digits + 1
print(digits)      