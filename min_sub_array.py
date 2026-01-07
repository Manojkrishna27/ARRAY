def min_sub_array(arr,k):
    window=sum(arr[:k])
    min_array=window

    for i in range(k,len(arr)):
        window=window+arr[i]-arr[i-k]
        min_array=min(window,min_array)

    return min_array
arr=[2,1,5,1,3,2]
k=3
print(min_sub_array(arr,k))