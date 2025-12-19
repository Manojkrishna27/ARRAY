def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target: ## if this satisy it will return mid (index of target) and stop
            return mid
        elif arr[mid]>target:
            high=mid-1      # move left
        else:
            low=mid+1   # move right
    return -1   # if while loop not work return -1
arr=[1,2,4,5,6]
target=1
print(binarysearch(arr,target))