# leader in a array is nothing An element is a leader if
#it is greater than all elements to its right

def leader(arr):
    leader=[]
    max_leader=arr[-1]
    leader.append(max_leader)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max_leader:
            leader.append(arr[i])
            max_leader=arr[i]

    return leader[::-1]
arr=[16,17,4,3,5,2]
print(leader(arr))