def movezero(arr):
    j=0   # two pointer technique 
    for i in range(len(arr)):
        if arr[i]!=0:  
            arr[j],arr[i]=arr[i],arr[j]  # i swap non zero to front
            j+=1   #moves to next position
    return arr
arr=[0,1,0,3,0,4]
print(movezero(arr))