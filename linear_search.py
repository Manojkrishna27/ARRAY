def linearsearch(arr,target): # linear search 
    for i in range(len(arr)):
        if arr[i]==target:  # element equal target element return that index of that
            return i  # so use return i
    return -1        # if target element is not there then return -1

arr=[1,2,4,5,5]
target=5
print(linearsearch(arr,target))