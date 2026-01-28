def rotatearr(arr,k):
    
    n=len(arr)-1
    k=k%n
    for i in range(k):
        last=arr[n-1]
        for j in range(n-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=last
    return arr
arr=[1,2,3,4,5]
k=3
print(rotatearr(arr,k))