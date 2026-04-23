def reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    return arr
arr=[int(x) for  x in input("enter the number").split()]
print(arr)
print(reverse(arr))
