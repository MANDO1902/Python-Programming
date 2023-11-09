# matrix multiplication
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


c=[[0,0,0],[0,0,0],[0,0,0]]

# c[i][j] is the dot product of ith row of a and jth coloum of b
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]

print(c)       

'''import numpy

x=numpy.mat(a)
y=numpy.mat(b)
print(x*y'''