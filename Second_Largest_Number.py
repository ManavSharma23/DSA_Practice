arr=[1,2,3,10,5,6,9,10]

n=len(arr)
largest=float("-inf")
second_largest=float("-inf")


for i in range(0,n):
  if arr[i]>largest:
    second_largest=largest
    largest=arr[i]

  elif arr[i]>second_largest and arr[i]!=largest:
    second_largest=arr[i]

  else:
    pass

print(largest)
print(second_largest)
  