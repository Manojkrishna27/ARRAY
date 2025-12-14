def largesmall(arr):
    large=arr[0]
    small=arr[0]
    for i in arr:
        if i>large:
            large=i
        if i<small:
            small=i
    return large,small
arr=[2,1,3,4,5]
print(largesmall(arr))
