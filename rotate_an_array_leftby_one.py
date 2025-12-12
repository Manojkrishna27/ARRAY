def rotate_left_by_one(arr):

    first=arr[0] # take an element which we want to rotate to left          

    for i in range(len(arr)-1):
        arr[i]=arr[i+1]       # traversal the array

    arr[-1]=first            # insert the taken element of to last
 

    return arr
arr=[1,2,3,4]
print(rotate_left_by_one(arr))
 
