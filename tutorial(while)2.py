# we have to find the no of digits in a number 
'''num = abs(int(input("Enter a number")))
# abs is absolutue function which takes absolute value of input like negative and postive are same 
a = str(num)
print(len(a))'''

num = abs(int(input("Enter a number")))
digits = 1
while(num>9):
    num=num//10
    digits=digits +1
    
# the above code is also same that is wriiten whitout the while loop
