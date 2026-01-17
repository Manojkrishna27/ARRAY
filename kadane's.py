"""Kadane’s algorithm finds the maximum subarray sum by keeping a running sum and resetting it whenever it becomes negative."""

def kadane(arr):
    current_sum=0
    max_sub=arr[0]
    for i in arr:
        current_sum+=i # add each element
        max_sub=max(current_sum,max_sub) # take max value

        if current_sum<0: # check negative 
            current_sum=0 # if negative reset
    return max_sub
arr=[1,-2,3,4,-8]
print(kadane(arr))