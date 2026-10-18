arr=[1,2,3,4,5]

n=len(arr)

def sorted(array):
  for i in range(n-1):
    if arr[i]>arr[i+1]:
      return False

  return True

print(sorted(arr))


  
