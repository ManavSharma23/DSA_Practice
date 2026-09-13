n=154

def armstrong(n):
    temp=n
    length=len(str(n))
    sum=0
    while temp>0:
        last_digit=temp%10
        sum=last_digit**length+sum
        temp=temp//10
        
    return n==sum
    
print(armstrong(n))