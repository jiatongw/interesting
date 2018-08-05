def merge(aList, bList):
    newList = []
    while (aList or bList): # single empty list won't stop the loop
        if not bList or (aList and aList[0] < bList[0]):
            # either bList is empty, or aList has next item
            newList.append(aList.pop(0))
        else:
            # bList has next item
            newList.append(bList.pop(0))
    return newList

list1 = [3, 4, 8, 9]
list2 = [1, 2, 5, 8]

print(merge(list1, list2))
print(list1)
print(list2)