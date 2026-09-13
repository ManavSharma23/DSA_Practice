# Reversing An Array 

array_1=[1,2,3,4,5,6,7,8,9]

def reverse(array_1,left,right):
    if left>=right:
        return array_1
    
    array_1[left],array_1[right]=array_1[right],array_1[left]
    
    return reverse(array_1,left+1,right-1)
    
print(reverse(array_1,0,len(array_1)-1))

# Palindrome of String 

word="abba"

def palindrome(word,left,right):
    
    if left>=right:
        return True
    
    if word[left]!=word[right]:
        return False
    
    return palindrome(word,left+1,right-1)
    
print(palindrome(word,0,len(word)-1))