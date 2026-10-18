arr=[1,1,0,0,1,0,1,1,1,1]

largest=0
current=0

n=len(arr)

for i in range(n):
    if arr[i]==1:
        current+=1
    else:
        largest=max(current,largest)
        current=0

print(max(largest,current))