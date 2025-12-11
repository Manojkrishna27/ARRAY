def removeduplicate(arr):
    n=len(arr)
    res=set([]) # with use of set we can remove the duplicate because set does not contain any duplicates values
    
    for i in range(n):

        res.add(arr[i])

    return res
arr=[1,2,3,4,6,6,4]
print(removeduplicate(arr))




