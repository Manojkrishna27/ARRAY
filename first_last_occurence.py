"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1]."""
def firstlast_occurence(arr,target):
    low=0
    n=len(arr)
    high=n-1
    lb=n
    #lower bound
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    # if lower bound not found [-1,-1]
    if lb==n or arr[lb]!=target:
        return [-1,-1]
    # reset the position
    low=0
    high=n-1
    ub=n
    # upper Bound
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return [lb,ub-1] # -1 for last occurence
arr=[5,7,7,8,8,10]
target=8
print(firstlast_occurence(arr,target))
