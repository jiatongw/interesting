def factor(x):
    ll=[]
    sum = 0
    for i in range (1,x+1):
        if x%i == 0 and i%2 != 0 :
            ll.append(i)
            sum+=i
    print(ll)
    return sum

l = [3,12,15,21,55,1009]


s = 0
for i in l:
    s += factor(i)
print(s)