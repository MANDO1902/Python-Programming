import random
l = []
# we create a empty list 
for i in range(30):
    # here we add data of 30 random pepole
    l.append(random.randint(1,365))
    # here numbers reprsent the birthday date of pepol
l.sort()
print(l)
# let check that two person have same birth date or not 
i = 0
flag=0
# this mean two pepole does not have same bithday
while(i<=len(l)-2):
    if(l[i]==l[i+1]):
        print("two pepolr have same bithday",l[i],l[i+1])
        flag = 1
    i = i+1    
if (flag==0):
    print("not have same birthday ")

