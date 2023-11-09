# find the factorial of number using while loop 
# we have already done this using while loop in tutorial(while)1.py
num = int(input("Enter the number "))
fact = 1
for i in range(1,num+1 ,1):
    fact = fact *i
    
if num > 0 :
    print(fact) 

else:
    print("Not Defined")      