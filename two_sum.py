arr=[1,3,5,7,9,11,2,6]
target=17

def two_sum(arr,target):
    hash_map={}
    n=len(arr)
    
    for i in range(n):
        remaining=target-arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        
        hash_map[arr[i]]=i

print(two_sum(arr,target))
      