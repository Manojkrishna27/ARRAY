"Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. "
"If the target is not found, return -1."

#binary search 
def binarysearch(arr,target):
    high=len(arr)-1 
    low=0
    while low <=high:
        mid=(low+high)//2 

        if arr[mid]==target:  # checking if mid is equal to target
            return mid
        elif arr[mid]<target: # if mid is less than target then low =mid+1
            low=mid+1
        else:                 # else high=mid-1
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7]
target=6
print(binarysearch(arr,target))