l = [1,1,1,1,1,2,3,4]

res=[]
for i in range(len(l)-1,0,-1):
    if l[i] not in res:
        res.append(l[i])
print(res)