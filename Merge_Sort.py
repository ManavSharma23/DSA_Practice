# merge sort = divide and conquer

# function 1 = merge_array will be used to sort to array and combine 
# function 2 = merge_sort will be used to sort and conquer 


array=[3,6,5,4,2,1,7,9,8]

def merge_array(left,right):
    i,j=0,0
    result=[]
    n,m=len(left),len(right)
    
    while i <n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
        
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
                
    return result


def merge_sort(array):
    
    if len(array)==1:
        return array
        
    length=len(array)
    mid=length//2
    
    left_array=array[0:mid]
    right_array=array[mid:]
    
    left=merge_sort(left_array)
    right=merge_sort(right_array)
    
    return merge_array(left,right)
    
    
print(merge_sort(array))
    
    
    
    
    
    
