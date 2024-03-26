#没有结束条件的无限递归

#Python内置的sys模块中的setrecursionlimit()函数可以获取最大递归深度,没有参数
#setrecursionlimit()调整最大递归深度,参数表示调整的深度
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)
def tell_story(count=0):
    count+=1
    print(count,"从前有座山,山里有座庙,庙里有个老和尚在讲故事,他在讲:")
    tell_story(count)

print("给你讲个故事")
tell_story()