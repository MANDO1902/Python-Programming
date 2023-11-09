# list are mutable 
# tuple is inmutable or not modify value in it 

t = 1 ,2 ,3 
print(t,type(t))
# here we are apcking integer value to tuple

x , y ,z = t 
print(x,y,z)
# here we are unpacking the tuple values to inteager 


x = (10)
print(x,type(x))
#  here we got type int because single value tuple considerd as integer 

t =([1,2],['a','m'])
t[0][0]=10
print(t)
# this is called hesshable 
# we can value of a list stored in tuple because list is mutable 
