# here we get to know some more feature of print statement

#use of end opreator in print 
'''
for i in range(1,11,1):
    print(i, end=" ")
# here end opreator simpily end value ofi with a backspace 
# i a single line output only 
'''

#use of sep opreator in print 
'''
d = 27
m = 11
y = 2004
print("My date of birth is " , end=' ')
print(d,m,y,sep="/")
'''

# diffrent type of format priniting 
'''
num = int(input("Enter a number")) 
for i in range(1,11):
   # print(num,"x",i,"=",num*i)
   # print(f'{num} x {i} = {num*i}')
   # print('{0} x {1} = {2}'.format(num,i,num*i))
    print('%d x %d = %d'%(num,i,num*i))
'''    


# another example of format printing 
# we want only upto two decimal digit value of pi
'''
pi = 22/7
print(f'{pi:.2f}')
print('{0:.2f}'.format(pi))
print('%.2f'%(pi))   
'''

# a example of align format printing
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
# here d is use for integer 
#and 5 represent the max charcter to align