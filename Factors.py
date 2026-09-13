n=12

factors=[]

range_last=int(n**1/2)

for i in range(1,range_last+1):
    if n%i==0:
        factors.append(i)
        quotient=n//i
        
        if quotient!=i:
            factors.append(quotient)
            
print(factors)