def product_except_self(nums):
    n=len(nums)
    ans=[1]*n
    
    
    prefix=1   # ans in prefix [1,1,2,6]
    for i in range(n):
        ans[i]=prefix
        prefix*=nums[i]

    suffix=1   # ans in suffix [6,8,12,24]
    for i in range(len(nums)-1,-1,-1):
        ans[i]*=suffix
        suffix*=nums[i]

    return ans
nums=[1,2,3,4]
print(product_except_self(nums))