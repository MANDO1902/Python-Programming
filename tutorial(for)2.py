'''
for i in range(a , b , c)
'''
# here we already know a represent the starting range 
# b represent the ending range plus one 
# but there c represent the step (that exactlly mean if setps are positive it jump the value over and negativeit jup down the value )


# let see a example 

'''
for i in range ( 1, 11 , 2):
    print(i) 
# here we get simple value by step = 2 
# it first print 1 then 3 by skipping the 2 between them 
'''  


# let see another example by priting the range i9n reverse order
'''
for i in range(10 , -1 , -1 ):
    print(i)
# here we see we get reverse output because setp id -1 
# we took ending point -1 because step are following reverse order 
# if we want to get zero so we have put ending point -1 like  in previous 
# example we put range 11 to get up the value upto 11
'''   
# lets write a coomman code for it 
a = int(input("Enter starting range "))
b = int(input("Enter ending range  "))
c = int(input("Enter the step"))

for i in range(a , b, c):
    print(i)