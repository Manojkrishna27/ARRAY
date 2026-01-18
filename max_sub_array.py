# maxsubarray sum

def maxsubarray(arr,k):
    window=sum(arr[:k]) # total sum of subarrays
    max_array=window

    for i in range(k,len(arr)):
        window=window-arr[i-k]+arr[i]  # add next and remove the first element this process goes on
        max_array=max(window,max_array) # it returns the max of subarrays
    return max_array
arr=[2,1,5,1,8,2]
k=3
print(maxsubarray(arr,k))