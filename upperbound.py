"""Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound of x is defined as the smallest index i such that nums[i] > x.
If no such index is found, return the size of the array."""

def upperbound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)

    while low<=high:
        mid=(low+high)//2

        if arr[mid]>target: # symbol is logic for upper bound
            ans=mid         #store
            high=mid-1      #left
        else:
           low=mid+1        # right
    return ans              # returns index value of first occurence
arr=[1,3,3,5,6,7]
target=2    
print(upperbound(arr,target))