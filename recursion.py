# printing number
# n=15
# upto=0
# def count(n, upto):
#     if n ==upto:
#         return
#     else:
#         upto+=1
#         print(upto)
#         count(n, upto)
#
# count(n,upto)

# printing sum

# def sum(total_sum,i,n):
#     if i>n:
#         print(total_sum)
#         return
#
#     sum(total_sum+i,i+1,n)
#
# sum(0,1,20)

# sum with different

# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# print(sum(20))

# factorial

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))

# reversing an array

# def func(arr, left, right):
#     if left>=right:
#         return arr
#     arr[left], arr[right]= arr[right], arr[left]
#     return func(arr, left + 1, right - 1)
#
# nums=[1,2,4,5,6,7,8]
# result=func(arr=nums,left=0,right=6)
# print(result)

# palindrome of a sttring

# s='nitin'
# right=len(s)-1
# left=0
# def palindrome(l,r):
#     while l<r:
#         if s[l]!=s[r]:
#             return False
#         else:
#             l+=1
#             r-=1
#         return True
#
# result=palindrome(left,right)
# print(result)

# using recursion

# def palindrome(s,l,r):
#     if l>r:
#         return True
#     else:
#         pass
#     if s[l]!=s[r]:
#         return False
#     return palindrome(s,l+1,r-1)
#
# s='awdfvghuhjk'
# l=0
# r=len(s)-1
# print(palindrome(s,l,r))


# fibionacci series

def fibionaaci(n):
    if n==0 or n==1:
        return n
    else:
        return fibionaaci(n-1)+fibionaaci(n-2)

print(fibionaaci(5))



























