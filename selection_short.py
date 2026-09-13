# compare first element with other then switches with the minimum value 

array=[8,3,4,5,1,2,7,9,6]

length=len(array)

for i in range(0,length):
    minimum_value_index=i
    for j in range(i+1,length):
        if array[j]<array[minimum_value_index]:
            minimum_value_index=j 
        
    array[i],array[minimum_value_index]=array[minimum_value_index],array[i]

print(array)