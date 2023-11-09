# to check a number is a plaindrome or not 
num = int(input("Enter a number "))
strnum = str(abs(num))
rev=''
for i in strnum:
    rev = i + rev
if num<0 :
    rev = "-"+rev
if(num == int(rev)):
    print("Plaindrome")
else:
    print("Not a Plaindrome")            