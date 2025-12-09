def second_large(arr):
    large=arr[0]
    second=arr[0]
    
    # if new large found
    for num in arr:
        if num>large:
            second=large # second becomes old large
            large=num

         # if num is between largest and second  and  NUM is  not equal to largest
        elif num>second and num!=large:
              second=num
        
    return second

arr=[1,2,3,4,5]
print(second_large(arr))
