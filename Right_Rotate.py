arr=[1,2,3,4,5,6,7]

n=len(arr)

def right(arr,k):
  rotation=k%n

  if rotation == 0:
    return arr 
    
  for i in range(k):
    last_value=arr.pop()
    arr.insert(0,last_value)

  return arr

print(right(arr,5))
  

