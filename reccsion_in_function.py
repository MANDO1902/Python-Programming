
# here we use new prperty recession 
# we use same function into function
def sum(n):
    if(n==1):
        return 1
    else:
        return (sum(n-1)+n)  
# code verified    


# define fuction for compound intrest
# p denotes the principal amount
# t denotes the time 
# r denotes the rate of intrest 
def comp(p,t,r):
    if(t==1):
        return (p*(1+(r/100)))
    else:
        return comp(p,t-1,r)*(1+(r/100))
# code verified


# define functuin for factorial
def fact(n):
    if(n==1):
        return 1
    else:
        return (fact(n-1)*n)
# code verified    


       


