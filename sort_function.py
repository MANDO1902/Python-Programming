'''l=[1,3,34,6,8,456,90]
def obvious_sort(l):
    c=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if(l[i]<mini):
                mini=l[i]
        c.append(mini)  
        l.remove(mini) 
    return c 

print(obvious_sort(l))           '''

l = [1,4,67,23,5,78,3]

def list_mini(l):
    mini=l[0]
    for i in range(len(l)):
        if(l[i]<mini):
            mini = l[i]
    return mini   

def obvious_sort(l):
    x=[]
    while(len(l)>0):
        mini= list_mini(l)
        x.append(mini)
        l.remove(mini)

    return x  

print(obvious_sort(l))