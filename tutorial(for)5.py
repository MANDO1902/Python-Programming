num = int(input("Enter a number "))
strnum = str(abs(num))
rev=''
for i in strnum:
    rev = i + rev
    # here we put i + rev because rev + 1 give the same value as input
    # but this give the revrse beacuse thnis is a string and order of addition matter for a string
if (num>0):
    print(rev)
else:
    print("-"+rev)    