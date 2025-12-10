def removeduplicate(arr):
    n=len(arr)
    result=set([]) # with use of set we can remove the duplicate because set does not contain any duplicate
    
    for i in range(n):

        result.add(arr[i])

    return result
arr=[1,2,3,4,6,6,4]
print(removeduplicate(arr))




