# this is two pointer technique only used for sorted array
def twosum(num,target):

    left=0
    right=len(num)-1

    while left<right:
        s= num[left]+num[right]
        
        if s==target:
            return [left,right]
        elif s<target:
            left+=1
        else:
            right-=1
num=[2,7,11,15]
target=9
print(twosum(num,target))

# this is hashing method can used for all types of array
def twoSum(nums, target):
    hashmap = {}      

    for i in range(len(nums)):
        need = target - nums[i] 

        if need in hashmap:
            return [hashmap[need], i] # it returns the hashvalue and current iteration so that the final output is correct

        hashmap[nums[i]] = i  # storing the element

nums=[2,7,11,15]
target=9
print(twoSum(nums,target))