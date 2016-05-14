def merge_sorted_array(myList, aliceList):
    mergedList = []
    l = max(len(myList), len(aliceList))
    i=0
    j=0
    while i < len(myList) and j < len(aliceList):
        if myList[i] < aliceList[j]:
            mergedList.append(myList[i])
            i += 1
        else:
            mergedList.append(aliceList[j])
            j += 1

    if i != len(myList):
        for r in range(i,len(myList)):
            mergedList.append(myList[r])
    elif j != len(aliceList):
        for r in range(j,len(aliceList)):
            mergedList.append(aliceList[r])
    return mergedList

my_list = [3, 4, 6, 10, 11, 13]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_sorted_array(my_list, alices_list)