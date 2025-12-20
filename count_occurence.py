"""You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr."""
def countoccurence(arr,target):
    low=0
    n=len(arr)
    lb=n
    high=n-1
    # lower bound
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
     # checking the edge if target not found       
    if lb==n or arr[lb]!=target:
        return 0 
    # reset the element
    #upper bound
    low=0
    n=len(arr)
    high=n-1
    ub=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub-lb # ub-lb =count here ub is 3 index(4) and lb is 2 index(1) 4-1 =count 3
arr=[1,2,2,2,3]
target=2
print(countoccurence(arr,target))


