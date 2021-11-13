l = [4,2,6,3,8,10]
for i in range (0,len(l)-1):
    for j in range (i+1,len(l)):
        if l[i] > l[j]:
            max = l[i]
            l[i]= l[j]
            l[j] = max
print (l)





