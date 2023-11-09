import random
l = []
for i in range(1,1000):
    l.append(random.randint(1,1000))
# how to found a prictular elemnt in alist 

n=0
while(n>-1):
    n=int(input("Enter a number:"))
    print("Type -1 to exist") 
    flag = 0
    for i in range(len(l)):
        if(n==l[i]):
            print("Hip Hip hurray , we found the number ")
            flag=1

    if(flag==0):
        print("there is no such number in the list ")
 # according to me i cant understand the puporse of while loop here 
 