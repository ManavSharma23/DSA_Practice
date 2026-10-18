arr=[1,2,3,4]

n=len(arr)

def zero(array):
  i=0
  while i<n:
      if arr[i]==0:
        break
      i+=1
  
  if i == n:
    return "No zero" 
  
  j=i+1
  
  while j<n:
    if arr[j]!=0:
      arr[i],arr[j]=arr[j],arr[i]
      i=i+1
      
    j+=1
  
  return arr

print(zero(arr))
      
      



