# matrix additon by first pricipal
dim=3
# dim is the order of matrix 

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

a=[]
# a is our first matrix
a.append(r1)
a.append(r2)
a.append(r3)

b=[]
# b is our another matrix
b.append(s1)
b.append(s2)
b.append(s3)

print(a)
print(b)

# we need to add to matrix

c=[[0,0,0],[0,0,0],[0,0,0]]
# if dim chages we need to reaarange c according to dim 
for i in range(dim):
    for j in range(dim):
        c[i][j]=a[i][j]+b[i][j]
print(c)