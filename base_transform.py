
#递归算法的任意进制转换
def toStr(n,base):
    #n是要转换的数,base是进制
    converString="0123456789ABCDEF"
    if n<base:
        return converString[n]
    else:
        return toStr(n//base,base)+converString[n%base]

print(toStr(256,2))