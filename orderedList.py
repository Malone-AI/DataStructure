#有序表
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data=newData
    def setNext(self,newNext):
        self.next=newNext

class OrderedList:
    def __init__(self):
        self.head=None
    
    def add(self,item):
        pre=None
        cur=self.head
        stop=False
        while cur!=None and not stop:
            if cur.getData()>item:
                stop=True
            else:
                pre=cur
                cur=cur.getNext()

        temp=Node(item)
        if pre==None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(cur)
            pre.setNext(temp)
        

    def empty(self):
        if self.head==None:
            return True
        else:
            return False

    def size(self):
        cur=self.head
        count=0
        while cur!=None:
            count+=1
            cur=cur.getNext()
        return count
    
    def search(self,item):
        cur=self.head
        found=False
        stop=False

        while cur!=None and not found and not stop:
            if cur.getData()==item:
                found=True
            else:
                if cur.getData()>item:
                    stop=True
                else:
                    cur=cur.getNext()
        return found

    #def pop():
    #    pass

    def Print(self):
        cur=self.head
        while cur!=None:
            print(cur.getData())
            cur=cur.getNext()