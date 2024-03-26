#变位词的第三中解法 算法效率最高

#把两个字母中的26个字母分别计数，再比较每个字母出现的个数是否相同

def anagramSolution(s1,s2):
    c1=[0]*26
    c2=[0]*26

    #统计每个单词中26个字母出现的次数
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]=c2[pos]+1

    i=0
    stillOk=True
    while i<26 and stillOk:
        if c1[i]==c2[i]:
            i=i+1
        else:
            stillOk=False
    return stillOk
