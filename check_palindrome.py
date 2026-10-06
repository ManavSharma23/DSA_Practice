n=123443212


def palindrome(n):
    temp=n
    palindrome_number=0
    while temp>0:
        last_digit=temp%10
        palindrome_number=(palindrome_number*10)+last_digit
        temp=temp//10
    
    return palindrome_number==n

print(palindrome(n))
