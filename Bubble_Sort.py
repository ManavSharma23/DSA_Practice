# compare two nearest value and swap accoringlly

array=[3,4,2,1,6,5,8,7,9]

length=len(array)

for i in range(length-2,-1,-1):
    for j in range(0,i+1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]

print(array)