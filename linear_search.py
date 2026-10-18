arr=[1,3,5,34,23,12,89,65]

n=len(arr)
def linear(arr,target):
    for i in range(n):
        if arr[i] == target:
            return i

    return False

print(linear(arr,65))