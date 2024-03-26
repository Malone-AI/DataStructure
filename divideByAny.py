#十进制转换十六以下任意进制

from stack import stack

def baseConverter(number,base):
    digits="0123456789ABCDEF"

    remstack=stack()

    while number>0:
        rem=number%base
        remstack.push(rem)
        number=number//base

    binstring=""
    while not remstack.isempty():
        binstring=binstring+digits[remstack.pop()]

    return binstring
