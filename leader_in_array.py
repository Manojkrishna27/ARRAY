# leader in a array is nothing An element is a leader if
#it is greater than all elements to its right

def leader(arr):
    n=len(arr)-1
    res=[]

    max_so_far=arr[-1]
    res.append(max_so_far)

    for i in range(n-1,-1,-1):
        if arr[i]>=max_so_far:
            max_so_far=arr[i]
            res.append(arr[i])

    return res[::-1]
arr=[16,17,4,3,5,2]
print(leader(arr))