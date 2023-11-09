# To print a multiplication table like the below code output  
'''
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("2 x 5 = 10")
print("2 x 6 = 12")
print("2 x 7 = 14")
print("2 x 8 = 16")
print("2 x 9 = 18")
print("2 x 10 = 20")
'''
a = int(input("Enter startring range "))
# a is the range of indent(i) where it starts from 
n = int(input("Enter the ending range "))
# n is the range of indent(i) where it ends 

for i in range (a,(n+1)):
    # we put n+1 here because if we want to end it on 10 we have to put 11 so it lowyes takes a value more just to comfort our code i write here n +1
    print("2 x",i,"=",2*i)
