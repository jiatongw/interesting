
l=[2,2]


def balance(l):
    if len(l)==0 or len(l) == 1:
        return 0

    
    for i in range(1,len(l)):
        print(l[:l[i-1]])
        print(l[(i+1):])
        if sum(l[:l[i-1]]) == sum(l[(i+1):]):
            return i
        
    return -1

print(balance(l))
        
