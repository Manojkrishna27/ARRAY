"""Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array."""

def lowerBound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)

    while low<=high:
        mid=(low+high)//2

        if arr[mid]>=target:
            ans=mid   #store
            high=mid-1 # left
        else:
            low=mid+1  # right
    return ans
arr=[1,2,2,5,6,8]
target=2
print(lowerBound(arr,target))

