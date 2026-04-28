def Minarray(arr):
    small=arr[0]
    small_index=0
    for i in range(1,len(arr)):
        if arr[i]<small:
            small_index=i
    return small_index

arr=list(map(int,input().split()))
print(Minarray(arr))