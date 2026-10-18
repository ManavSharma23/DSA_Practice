arr1=[1,1,2,2,3,3,4,6]
arr2=[1,1,1,3,4,5,5,7,7,8,9]

result=[]

n=len(arr1)
m=len(arr2)

i,j=0,0

while i<n and j<m:
    if arr1[i]<=arr2[j]:
        if len(result)==0 or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i+=1
            
    else:
        if len(result)==0 or result[-1]!=arr2[j]:
            result.append(arr2[j])
        j+=1
            
            
while i<n:
    if len(result)==0 or result[-1]!=arr1[i]:
        result.append(arr1[i])
    i+=1
            
while j<m:
    if len(result)==0 or result[-1]!=arr2[j]:
        result.append(arr2[j])
    j+=1
        
        
print(result)
    
    
    