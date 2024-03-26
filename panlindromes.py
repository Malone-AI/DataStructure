from Deque import Deque

def palchecker(aString):
    chardeque=Deque()

    for ch in aString:
        chardeque.addRear(ch)

    flag=True
    
    while chardeque.size()>1 and flag:
        if chardeque.removeFront()!=chardeque.removeRear():
            flag=False
    
    return flag

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("山外山"))