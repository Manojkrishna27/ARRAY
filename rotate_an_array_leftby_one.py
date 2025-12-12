def rotate_left_by_one(arr):

    first=arr[0] # take an element which we want to rotate to left          

    for i in range(len(arr)-1):
        arr[i]=arr[i+1]       # traversal the array

    arr[-1]=first            # insert the taken element of to last
 

    return arr
arr=[1,2,3,4]
print(rotate_left_by_one(arr))
 
# super short technique but not recommended for the interview
arr1=[1,4,2,3]
arr1.append(arr1.pop(0))  # pop is removing the index 0 element and that element is append to the last of a list
print(arr1)
