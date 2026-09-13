frequency=[1,2,3,4,3,2,1,3,5,6,7]

hash_map={}

for i in frequency:
    hash_map[i]=hash_map.get(i,0)+1
    
print(hash_map)
