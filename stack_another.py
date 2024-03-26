#列表的首端作为栈顶的栈类

class stack():
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return (len(self.items))
