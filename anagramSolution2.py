#变位词的第二种解法
#把两个字符排序后对应位置的字母进行比较

def anagramSolution(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    
    alist1.sort()
    alist2.sort()
    pos=0
    matches=True
    while pos<len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches
