#中缀表达式转后缀表达式

#操作符有+-*/()
#操作数由大写字母表示

#对转换后的后缀表达式用列表储存

#对要进行转换的字符串进行遍历
#1.如果是操作数,则直接添加到列表的末尾
#2.如果是(则压入stk内
#3.如果是)则反复弹出stk内元素直至弹出匹配的(
#4.如果是操作符则压入stk,但先要做一步判断
#如果栈顶的操作符优先级高于或等于当前操作符,则先进行反复弹出stk内元素,直至栈顶操作符优先级低于当前操作符时,再压入栈内
#否则直接压入栈内
#扫描结束后一次弹出stk内元素并添加到列表末尾

from stack import stack

def infixToPostfix(infixexpr):
    #规定算符优先级,用字典    
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1

    stk=stack()
    postfixList=[]
    
    tokenList=list(infixexpr)

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            stk.push(token)
        elif token ==')':
            topToken=stk.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken=stk.pop()
        else:
            while (not stk.isempty()) and (prec[stk.peek()]>=prec[token]):
                postfixList.append(stk.pop())
            stk.push(token)
        
    while not stk.isempty():
        postfixList.append(stk.pop())
    return "".join(postfixList)
