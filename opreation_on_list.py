l1 = [1,2,3]
l2 =[10,100,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12)
print(l21)

# they are diifrent but we can add list like that but we have to rember the order of adding 

# multiplication opreator on list 
l1 = [1,2]*10
print(l1)
# in ouput we get 1,2 10 times continously 

# comparsion in list 
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
l4 = l1
print(l1==l2)
print(l2==l3)
# length and order both matter 
print(l1 is l2)
print(l1 is l4)


l= [1,2,3,4]

l.insert(3,7)
print(l)
# here we append 9 at l[3] at list 

l.reverse()
print(l)
# here we got complete list reversed 

l.pop(4)
print(l)
# it remove the l[4] elemnt from the list 