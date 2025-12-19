"""Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].
Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number."""

def find_element(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low=mid+1
        else:
            high=mid
    return low # or high both gives same index of value peak value
arr=[1,2,3,4,5,6,7,8,5,1]
print(find_element(arr)) 