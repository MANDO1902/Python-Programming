import random
l = []
for i in range(1,1000):
    l.append(random.randint(1,1000))
# how to found a prictular elemnt in alist 
a=365
# a is the number that we have to found in the l
flag = 0
for i in range(len(l)):
    if(a==l[i]):
        print("Hip Hip hurray , we found the number ")
        flag=1
if(flag==0):
    print("there is no such number in the list ")

    
 