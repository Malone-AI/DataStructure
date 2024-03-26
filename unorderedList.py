#链表对象类型的实现

#结点类
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext;

#链表类
class UnorderedList:
    def __init__(self):
        self.head=None

    def add(self,item):
        #头插法
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    
    def empty(self):
        if self.head==None:
            return True
        else:
            return False

    def size(self):
        cur=self.head
        count=0
        while cur!=None:
            cur=cur.getNext()
            count+=1
        return count
    
    def search(self,item):
        cur=self.head
        found=False
        while cur!=None and not found:
            if cur.getData()==item:
                found=True
            else:
                cur=cur.getNext()
        return found
    
    def remove(self,item):
        cur=self.head
        pre=None
        found=False

        while not found:
            if cur.getData()==item:
                found=True
            else:
                pre=cur
                cur=cur.getNext()
        
        if pre==None:
            self.head=cur.getNext()
        else:
            pre.setNext(cur.getNext())
    
    #def append(self,item):
    #    #尾插法
    #    cur=self.head
    #    while cur!=None:
    #        cur=cur.getNext()
    #    temp=Node(item)
    #    cur.setNext(temp)
    #    del temp

    #def pop(self,index=None):
    #    if index==None:
    #        cur=self.head
    #        pre=None
    #        while cur!=None:
    #            pre=cur
    #            cur=cur.getNext()

    #        if pre==None:
    #            self.head=cur.getNext()
    #        else:
    #            pre.setNext(cur.getNext())
    #    elif self.size()>=index+1:
    #        count=0
    #        pre=None
    #        cur=self.head
    #        while cur!=None and count!=index:
    #            pre=cur
    #            cur=cur.getNext()
    #            count+=1
    #        if pre==None:
    #            self.head=cur.getNext()
    #        else:
    #            pre.setNext(cur.getNext())
    #    else:
    #        return False
            

    def Print(self):
        cur=self.head
        while cur!=None:
            print(cur.getData())
            cur=cur.getNext()

mylist=UnorderedList()
