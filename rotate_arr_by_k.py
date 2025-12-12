def rotate_a_array_by_k(arr,k):
    n=len(arr)  # taking the lenght of array

    k=k%n     # doing modulus for handling large k rotate
    for i in range(k):    # loop run k time

        first=arr[0]   # take first
        for j in range(n-1):
            arr[j]=arr[j+1] # traversal 
        arr[n-1]=first  # add first
    return arr
arr=[1,2,4,3,5,6]
print(rotate_a_array_by_k(arr,2))