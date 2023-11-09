# we are going to define new function 
# we define addition function

'''def add(a,b):
    ans=a+b
    return ans

x=int(input("Enter first number: "))
y=int(input("Enter second number:"))

print("The sum of two no is:",add(x,y))'''

# now we define discount function 
def discount(cost,disc):
    ans = cost-(cost*(disc/100))
    return ans

a = float(input("Enter the cost:"))
# we put float input because cost of product csn be in decimnal
b = float(input("Enter the percentage of discount"))
# we put float here because discount given on product can be in decimal
print("The coustomer need to pay after discout:",discount(a,b))

