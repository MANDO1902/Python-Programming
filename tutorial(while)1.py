# we have to find the factorial of positive integers 
num = int(input("Enter the number"))

i = 1 
answer = 1
if (num>=0):
    while(i<=num):
        answer=answer*i
        i=i+1
    
    print(answer)    
    
else:
    print("Not Defined")    