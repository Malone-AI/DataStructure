#后缀表达式求值

#由于操作符在操作数之后,必须知道操作符以后才能进行运行,所以用栈寄存操作数

#但是需要注意的是,先弹出的是右操作数,后弹出的是左操作数,这对+和*没有影响,但对-和/有影响

from stack import stack

def postfix_calculate(postfix):
    operandStack=stack()
    tokenList=list(postfix)

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op,op1,op2):
    if op =='*':
        return op1*op2
    elif op == '+':
        return op1+op2
    elif op == '-':
        return op1-op2
    else:
        return op1/op2
