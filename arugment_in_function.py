# there are bascially three type of argument 
# 1 poisitional argument
def add(c,a,d,b):
    return(a+b-c+d) 
print(add(10,20,30,50,))
# in this arugment the poisition of input is fixed 


# 2 keyword argument 
print(add(a=10,b=20,c=30,d=50))
# in this arfument we assign value to input


# 3 defalut argument
def sub(c=30,a=10,d=50,b=20):
    return (a+b-c+d)

print(40,10)
 # in this argument we assign a default value to input if we can give input valude to thode argument there defalut value is taken to excecute the code 
 