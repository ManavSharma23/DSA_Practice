arr=[1,3,5,6,4,0]

n=len(arr)

real_sum=n*((n+1)/2)

arr_sum=0

for i in range(n):
    arr_sum=arr_sum+arr[i]
    
print(int(real_sum-arr_sum))

    