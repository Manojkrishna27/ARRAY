def max_min(arr):
    # Two pointer 
    start=0
    end=len(arr)-1
    new_array=[] 
    while start<=end:

        if start!=end:
            new_array.append(arr[end])
            new_array.append(arr[start])
        else:
            new_array.append(arr[start])

        start+=1
        end-=1
       
       
    return new_array
arr=[1,2,3,4,5,6,7]  # output =[7,1,6,2,5,3,4]
print(max_min(arr))
