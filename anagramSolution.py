def anagramSolution(s1, s2):
    # 将一个单词中的字母位置进行变换,这个字母和变换后的字母就是一对变位词

    # 字符串是不可变类型,将其拷贝到一份列表中,方便标记
    alist = list(s2)
    stillOk = True
    pos1 = 0
    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found=False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOk=False
        pos1 = pos1 + 1
    return stillOk

print(anagramSolution('earth','heart'))
