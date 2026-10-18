arr=[1,2,3,10,5,6]

n=len(arr)
largest=float("-inf")
for i in range(0,n):
    largest=max(largest,arr[i])

print(largest)
      