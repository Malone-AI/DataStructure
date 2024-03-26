#括号匹配问题,只能处理圆括号
from stack import stack

def match(s):
    stk=stack()
    balanced =True
    index=0

    while index<len(s) and balanced:
        symbol=s[index]
        if symbol=='(':
            stk.push(symbol)
        else:
            if stk.isempty():
                balanced=False
            else:
                stk.pop();
        index=index+1

    if balanced and stk.isempty():
        return True
    else:
        return False
