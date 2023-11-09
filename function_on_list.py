# let define some function on the list 

l=[1,2,3,5,34,-34,568]
z=[20,40,50]

#to find the minimum value in a list 
def list_mini(l):
    mini=l[0]
    for i in range(len(l)):
        if(l[i]<mini):
            mini = l[i]
    return mini   

print(list_mini(l))
                   
# to find maximum value in a list 
def list_maxi(l):
    maxi=l[0] 
    for i in range(len(l)):
        if(l[i]>maxi):
            maxi=l[i]
    return maxi 

print(list_maxi(l))   

#to append second list before first list 
# l is first list and z is second list
def list_appendbefore(l,z):
    c=[]
    for i in range(len(z)):
        c.append(z[i])
    for i in range(len(l)):
        c.append(l[i])
    return c    

print(list_appendbefore(l,z))

# to append second list after first list 
def list_appendafter(l,z):
    c=[]
    for i in range(len(l)):
        c.append(l[i])
    for i in range(len(z)):
        c.append(z[i])
    return c 

print(list_appendafter(l,z))   

# to find average of element of list 
def list_average(l):
    sum=0
    for i in range(len(l)):
        sum = sum +l[i]
    sum = sum/len(l)
    return sum    

print(list_average(l))