def missingnumber(arr):
    n=len(arr)
    excepted=n*(n+1)//2 # just two method to check missing numbers n*(n+1)//2 - sum(arr) (total of array)
    total=0
    for i in range(n):
        total+=arr[i]
    ans=excepted-total
    return ans
arr=[1,2,4,5]
print(missingnumber(arr))