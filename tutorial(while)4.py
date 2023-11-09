# to check weather number is plaindrome or not
num = abs(int(input("Enter a number ")))
rev = num % 10     
num = num//10
while(num>0):
    r = num % 10
    num = num//10
    rev = (rev*10)+r
rev = int(rev)    
if(rev!=num):
    print("Plaindrome") 
else:
    print("Not a Plaindrome")  
print(rev)                