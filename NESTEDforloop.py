s = "VIBGYOR"
t = "good"
count = 0 
# IT IS AN EXAMPLE OF NESTED LOOP  
for i in range(7):
    for j in range(4):
        print(s[i],t[j])
        count += 1
print(f'total no of combination is {count}')