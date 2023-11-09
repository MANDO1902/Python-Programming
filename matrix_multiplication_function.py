# first we need to initalize c 
# we need to find dot product of two list 
# we need to pick ith row and jth coloum 
# here we assume all the matrix are square matrix

def initalize_mat(dim):
    c=[]
    for i in range(dim):
        c.append([]) 
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)

    return c        

def dot_product(a,b):
    dim=len(a)
    sum=0
    for i in range(dim):
        sum = sum + a[i]*b[i]
    return sum

def row(a,i):
    dim=len(a)
    l=[]
    for k in range(dim):
        l.append(a[i][k])
    return l    

def coloum(a,i):
    dim=len(a)
    l=[]
    for k in range(dim):
        l.append(a[k][i])
    return l
    
def mat_mul(x,y):
    dim=len(a)
    c=initalize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j]=dot_product(row(x,i),coloum(y,j))

    return c        


a = [[1,2,3],[4,5,6],[6,7,8]]
b = [[2,3,4],[4,5,6],[7,8,9]]

print(mat_mul(a,b))