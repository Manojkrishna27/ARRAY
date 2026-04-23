
# this method only used in duplicates allowed problems
def intersection1(arr1,arr2):
    res=[]
    freq={}

    for num in arr1:
        freq[num]=freq.get(num,0)+1

    for num in arr2:
        if num in freq and freq[num]>0:
            res.append(num)
            freq[num]=-1
    return res
arr1=[1,2,2,1]
arr2=[2,2,4]
print(intersection1(arr1,arr2))

def intersection(nums1, nums2):
    seen = set(nums1)
    res = set()
    
    for num in nums2:
        if num in seen:
            res.add(num)
    
    return list(res)
arr1=[1,2,2,1]
arr2=[2,2]
print(intersection(arr1,arr2))