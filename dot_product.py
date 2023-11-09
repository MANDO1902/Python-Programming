# this is for the dot product 
# it does not work when both list have deffrent length
x=[1,2,3,4,11]
y=[1,2,3,4,10]
dot_product=0
for i in range(len(x)):
    dot_product=dot_product+(x[i]*y[i])  
print(dot_product)