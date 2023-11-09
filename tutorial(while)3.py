'''# we have to find the reverse of the number 
num = int (input("Enter a number"))
absnum = abs(num)
if(num>=0):
    rev = num % 10
    num = num//10
    while(num>0):
        r=num%10
        num=num//10
        rev=(rev*10)+r
    
    print(rev)    

else:
    rev = absnum % 10
    absnum = absnum//10
    while(absnum>0):
        r=absnum%10
        absnum=absnum//10
        rev=(rev*10)+r
    
    print(rev - (rev*2))'''
     
# short method 
num = int(input("Enter a number "))
absnum = abs(num)
rev = absnum % 10     
absnum = absnum//10
while(absnum>0):
    r = absnum % 10
    absnum = absnum//10
    rev = (rev*10)+r
if(num>0):
    print(rev) 
else:
    print(rev-(2*rev))              