#this code is not right ther is some miskte in it 
# it have to reaarnge the elemnt of i in acesnding order 
#but code is writing reverse of it 

l=[15,6,2,23,345,45,56,278]
# l is the list which we have to reaarnge
x=[]
# x is the empty list
while(len(l)>0):

    min=l[0]
    for i in range(len(l)):
        if(l[i]<min):
            min=l[i]
    x.append(min)
    l.remove(min)
print(l)   
print(x)