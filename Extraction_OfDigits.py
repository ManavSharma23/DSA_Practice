from math import sqrt

# Counting Number Of Digits                   TC=o(log n)

def counting_number():
    number=8945
    count=0
    while number!=0:
        count=count+1
        number=number//10
    print(f"Number of Digits are : {count}")

# Palindrome                            TC = o ( log n )

def palindrome():
    no=110011
    num=no
    checking_no=0
    while num>0:
        last_digit=num%10
        checking_no=(checking_no*10)+last_digit
        num=num//10
    if checking_no==no:
        print("True")
    else:
        print("False")

# Amstrong Number               TC= o(log n)

def armstrong():
    n=153
    temp=n
    nod=0
    total=0
    for i in str(n):
        nod+=1
    while temp>0:
        digit=temp%10
        total+=digit**nod
        temp=temp//10
    if total==n:
        print("Armstrong Number")
    else:
        print("Not A Armstrong Number")

# Factors                           TC= o(root n ) + o ( n log n )

def factor():
    num=100
    result=[]
    for i in range(1,int(sqrt(num)+1)):
        if num%i==0:
            result.append(i)
            if num//i !=i:
                result.append(num//i)

    result.sort()
    print(result)

# Store Frequency in a dictionary                TC=o(n)

def frequency_map_way1():
    list1=[1,2,3,4,3,2,1,2,3,4,5,6,4,2,3,4,1,6]
    frequency_dict={}

    for i in range(0,len(list1)):
        if list1[i] in frequency_dict:
            frequency_dict[list1[i]] += 1
        else:
            frequency_dict[list1[i]] = 1

    print(frequency_dict)

def frequency_map_shortestWay():
    list1 = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 4, 2, 3, 4, 1, 6]
    hash_map={}
    length=len(list1)

    for i in range(0,length):
        hash_map[list1[i]]=hash_map.get(list1[i],0)+1

    print(hash_map)


frequency_map_shortestWay()
frequency_map_way1()
counting_number()
palindrome()
armstrong()
factor()
