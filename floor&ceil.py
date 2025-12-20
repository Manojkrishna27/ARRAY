"""Given a sorted array nums and an integer x.
 Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1."""
def floor_ceil(arr,x):
    low=0
    high=len(arr)-1
    floor=-1
    #lower bound
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x: 
            floor=arr[mid] # storing the value not index
            low=mid+1
        else:
            high=mid-1
    low=0
    high=len(arr)-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x: # greater than or equal to for ceil
            ceil=arr[mid] #storing value not index
            high=mid-1
        else:
            low=mid+1
    return floor,ceil   # value of floor and ceil
arr=[3,4,4,7,8,10]
x=5
print(floor_ceil(arr,x))