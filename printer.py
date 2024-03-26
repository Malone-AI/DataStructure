#模拟算法:打印任务

#一个实验室,在任意一个小时内,大约有10名学生在场
#这一个小时中,每人会发起2次左右的打印,每次1~20页

#打印机的性能
#草稿模式:每分钟10页
#正常模式:打印质量好,但速度下降为每分钟5页

#问题是:
#怎么设定打印机模式让大家都不会等太久的前提下尽量提高打印质量

#抽象问题,进行建模
#打印队列FIFO
from Queue import Queue
import random

class Printer:
    def __init__(self,ppm):
        #打印速度 单位:页/分钟
        self.pagerate=ppm
        #是否有打印任务
        self.currentTask=None
        #打印任务倒计时(单位:秒)
        self.timeRemaining=0

    def tick(self):
        #打印
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None
    
    def busy(self):
        #判断打印是否繁忙
        if self.currentTask!=None:
            return True
        else:
            return False
    
    def startNext(self,newtask):
        #开始打印新作业
        #newtask是作业对象
        self.currentTask=newtask
        #页数直接除以速度得到分钟,再乘以60是秒
        self.timeRemaining=newtask.getPages()*60/self.pagerate

#打印作业对象类型
class Task:
    def __init__(self,time):
        #初始化记录生成时间
        self.timestamp=time
        #打印页数
        self.pages=random.randint(1,21)

    #作业生成的时间
    def getTimestamp(self):
        return self.timestamp

    #返回作业的页数
    def getPages(self):
        return self.pages
    
    #等待时间
    def waitTime(self,currentTime):
        return currentTime-self.timestamp

#模拟生成打印作业任务
def newPrintTask():
    #每小时会有20个作业请求被提交,换算一下就是每180秒会有一个作业请求被提交,也就是每个时间点有作业请求被提交的概率为1/180
    num=random.randint(1,181)
    #当num==180时,才生成一个作业,即返回True
    if num==180:
        return True
    else:
        return False

#模拟打印函数
def simlation(numSeconds,pagesPerMinute):#第一个参数模拟的时长,第二个参数时打印速度即打印模式
    #打印机对象
    labprinter=Printer(pagesPerMinute)
    #打印队列
    printQueue=Queue()
    #生成的每个打印作业的等待时间
    waitingtimes=[]

    for currentSecond in range(numSeconds):

        if newPrintTask():#为真即在1/180的概率下有打印任务生成
            #生成打印作业并加入打印队列
            task=Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.empty()):
            #打印机不处于繁忙状态并且打印队列不为空,则从打印队列中取出一个任务给打印机执行
            nextTask=printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)

        labprinter.tick()
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))


#模拟打印10次
for i in range(10):
    #打印1个小时,每分钟打印5页
    simlation(3600,5)