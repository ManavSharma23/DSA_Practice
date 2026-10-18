arr=[1,1,2,2,3,3,4,4,4,5,6,6,12]
# return no of distinct values 

n=len(arr)

def distinct(array):
  if n ==1 :
    return n
  
  i=0
  j=i+1
  
  while j<n:
    if arr[i]!=arr[j]:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
    j+=1
  
  return i+1,arr

print(distinct(arr))