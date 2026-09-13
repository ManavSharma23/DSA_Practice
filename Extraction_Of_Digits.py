# to get the last digit we use %

n=45789

temp=n
while temp>0:
    last_digit=temp%10
    temp=temp//10
    print(last_digit)
    