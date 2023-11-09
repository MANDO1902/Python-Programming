# we use bracet like dicitonary 
# we wrriten in the format of list 
# set is unorderded quantity 
# set discarded the rpeated values 
s = {1,2,4,5,3,1,4,2,6,9,7,6,5,}
print(s)
# it is inmutable or in hasable 
 
# some set methods 
a = {1,5,7}
b = {1,2,3,4,5,67,8,9}
c= {2,4,56,78,} 

print(a.issubset(b))
print(b.issuperset(a))
print(b.union(c))
print(a.intersection(c))
