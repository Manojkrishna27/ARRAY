"""Binary Search"""
def roated_sorted(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        
        # left half sorted
        if arr[left]<arr[mid]:

            if arr[left]<=target<arr[mid]:
                right=mid-1
            else:
                left=mid+1
        # right half sorted
        else:

            if arr[right]<arr[mid]:

                if arr[right] <=target<arr[mid]:
                    left=mid+1
                else:
                    right=mid-1
    
    return -1
arr=[4,5,6,7,0,1,2]
print(roated_sorted(arr,target=0))
