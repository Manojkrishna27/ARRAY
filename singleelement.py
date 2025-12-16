"Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array."
def singleelement(arr):
    result=0
    for num in arr:
        result^=num # Xor method
    return result
arr=[1,2,1,2,5]
print(singleelement(arr))
