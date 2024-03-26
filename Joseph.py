#热土豆问题即约瑟夫问题

#将土豆传递的方向上的人从队首排到队尾
#队首永远是持有土豆的人

#将队首的人出队再入队,算作一次土豆的传递

#传递num次后将队首的人移除

from Queue import Queue

def hotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())#算作一次土豆的传递
        #土豆传递一轮结束后移除持有土豆的人即队首的人
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(['Bill','David','Susan','Jane','Kent','Brad'],6))