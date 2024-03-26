#十进制转换二进制

from stack import stack

def divideBy2(number):
    remstack=stack()

    while number>0:
        rem=number%2
        remstack.push(rem)
        number=number//2

    binstring=""
    while not remstack.isempty():
        binstring=binstring+str(remstack.pop())

    return binstring

print(divideBy2(34))
