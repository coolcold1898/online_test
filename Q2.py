n = eval(input())
l = []
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0 :
        l.append(i)    
    elif i%3 == 0 :
        continue
    elif i%5 == 0 :
        continue
    else :
        l.append(i)     
print(len(l))
         