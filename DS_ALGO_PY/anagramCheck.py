
def anagramCheck1(str1,str2):
    '''
    This method will take two strings and compares matching characters in both strings.
    If they were getting matched it will return True else False
    '''

    s1 = str1.replace(' ','').lower()
    s2 = str2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)


x=anagramCheck1(str1="dog",str2="help")
print(x)

def anagramCheck2(str1,str2):
    '''
    This method will take two strings and compares matching characters in both strings.
    If they were getting matched it will return True else False.
    This code have not used any built in functions.
    '''
    s1 = str1.replace(' ','').lower()
    s2 = str2.replace(' ','').lower()
    #edge case check
    if len(s1) != len(s2):
        return False
    
    count = {}

    for i in s1:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    for i in s2:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    return True

y=anagramCheck2(str1="danl",str2="land")
print(y)