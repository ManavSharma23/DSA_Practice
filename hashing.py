def hashing_usingList():          #given that data is betweeen 0 to 10       
    data_list=[1,2,1,3,4,6,7,8,9,0,7,6,4,3,5,7,8,9,1,2,3,3,4,5,6,7,8,0,0]
    counting_list=[1,4,7,11,2,3,6,-5,10,99]

    frequency_list=[0]*11

    for i in data_list:
        frequency_list[i]+=1

    for j in counting_list:
        if j<0 or j>10:
            pass
        else:
            print(j,":",frequency_list[j])


def hashing_usingDict():

    data_list=[1,2,3,4,5,6,7,8,9,0,87,4,3,2,5,7,8,9,33,2,22,3,45]
    counting_list=[1,2,3,4,56,7,89,9,0]
    freq_dict={}

    for i in range(0,len(data_list)):
        freq_dict[data_list[i]]=freq_dict.get(data_list[i],0)+1

    print(freq_dict)
    for i in counting_list:
        if i in freq_dict:
            print(i,":",freq_dict[i])
        else:
            print(i, ":", 0)


def hashing_characters_usingList():
    word='abcshgvbwefpoeqfohefvbeqbvenvkearbewrkvaberioavbreqaaiugavewbv'
    target_list=['a','b','c','h','p']
    hash_list=[0]*26
    for i in word:
        ascii_value=ord(i)-97
        hash_list[ascii_value]+=1

    for j in target_list:
        ascii_value2=ord(j)-97
        print(j,": ",hash_list[ascii_value2])

def hashing_characters_usingDict():
    word='kjnrhjbrweniytfghjkjnvycrtxerxtcvybuniuytyrtketxrctvbcrtxwertyuizasdfglhj'
    target_list=['a','h','j','k','l','z']
    freq_dict={}

    for i in word:
        freq_dict[i]=freq_dict.get(i,0)+1

    print(freq_dict)

    for j in target_list:
        if j in freq_dict:
            print(j,":",freq_dict[j])

        else:
            print(j,":",0)



hashing_characters_usingDict()
hashing_characters()
hashing_usingDict()
hashing_usingList()
