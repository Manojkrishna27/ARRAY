def check(arr):
    n=len(arr)
    for i in range(n-1):
            if arr[i]>arr[i+1]:  # comparing the array is sorted or not if greater then next to it become false and stop the loop
                  return False
        
    return True
arr=[1,2,3,4]
print(check(arr))