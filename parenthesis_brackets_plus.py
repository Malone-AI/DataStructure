#括号匹配问题,处理三种括号
from stack import stack

def match(s):
    stk=stack()
    balanced =True
    index=0

    while index<len(s) and balanced:
        symbol=s[index]
        if symbol in ['(','{','[']:
            stk.push(symbol)
        else:
            if stk.isempty():
                balanced=False
            else:
                top=stk.pop()
                if not matches(top,symbol):
                    balanced=False
        index=index+1

    if balanced and stk.isempty():
        return True
    else:
        return False

def matches(open,close):
    opens='({['
    closers=')}]'
    return opens.index(open)==closers.index(close)
