# largest element in array

def largest_element_array(arr):
    largest=arr[0] # simple loop
    for num in arr:
        if num>largest:
            largest=num
    return largest
arr=[2,1,3,5]
print(largest_element_array(arr))

# build in function
arr=[2,1,3,5]
print(max(arr))