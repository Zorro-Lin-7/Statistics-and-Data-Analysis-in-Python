# 检索tip: √ 标注 表示重点

# √ 计算思维的本质：抽象化（Abstraction) + 自动化(Automation) 
# √ 自顶向下的设计：一个问题分解成多个小问题来解决。具体步骤：
  1.将算法表达为一系列小问题；
  2.为每个小问题设计接口；
  3.细化算法——通过将算法表达为接口关联的多个小问题；
  4.为每个小问题重复上述过程
# √ 自底向上的执行：自底层模块开始一个一个进行测试
# √ 单元测试：
* 小规模程序：
     直接运行
* 中等规模：
     结构图底层开始，逐步上升；
     先运行每个基本函数，再测试整体函数
* 较大规模：
    高级软件测试方法

# √ 敏捷开发： 关键词“任务看板”。http://www.icourse163.org/learn/BIT-268001#/learn/content?type=detail&id=1003121208&cid=1003698576
# √ 面向过程的程序设计：以程序执行过程为设计流程的思想，最自然而然。OOP的过程中也会用到该方法。步骤
    0.分解问题，将一个全局过程分解为一系列局部问题
    1.分析程序从输入到输出的各步骤
    2.按照执行过程从前到后编写程序
    3.将高耦合部分封装成模块或函数
    4.输入参数，按照程序执行过程调试

print(value,...,sep=' ', end='\n')

input() # 产出的是string, 若输入数字，需要 int(input()); 

# 连续input 2个以上的值可以用:
import ast
ast.literal_eval(input('输入2个数'))


# Python读取文件夹下的所有文件
# os.listdir(path)是得到在path路径下所以文件的名称列表。
#     
# open(path)是打开某个文件。
#    
# iter是python的迭代器。    
#    
# 所以读取某文件夹下的所有文件如下：
import os  
path = "D:/Python34/news" #文件夹目录  
files= os.listdir(path) #得到文件夹下的所有文件名称  
s = []  
for file in files: #遍历文件夹  
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
          f = open(path+"/"+file); #打开文件  
          iter_f = iter(f); #创建迭代器  
          str = ""  
          for line in iter_f: #遍历文件，一行行遍历，读取文本  
              str = str + line  
          s.append(str) #每个文件的文本存到list中  
print(s) #打印结果  

# 字符串操作
str.join(sequence)
str.count(sub, start= 0,end=len(string))
str.isalpha()
str.replace()
str.split() # 返回列表

>>>str = "-"
>>>seq = ("a", "b", "c")
>>>print(str.join( seq ))
a-b-c
>>>' '.join('abc') # 需要加括号
a b c

# 列表操作
l.remove(x) # 删除列表中第一次出现的元素x
l.index(x)  # 返回第一次出现元素x的索引值
l.count(x)  # 列表中x的个数
l.reverse() # 倒序

# pyton 的math, random 库可用numpy代替
# math:
np.pi 
np.e
np.log()
np.cos()

# random: http://blog.csdn.net/unin88/article/details/50570196

# 字符串格式化方法 http://www.icourse163.org/learn/BIT-268001#/learn/content?type=detail&id=1003121179&sm=1
'{0:*>20.2f}'.format(3.14159)

# 布尔值：空串、零值、零序列都为False，其他为True

# 函数定义
# 可以没有return语句。被调用时，执行函数body，比如print语句。 √
# 无return语句 等价于 return None √
# 函数接口：input——参数、output--return

# 函数调用过程的树状解析：
def main():
    sing('Mike')    -----> def sing(person):
    print()                    print('Happy birthday, dear', person+'.')  # +连接字符串没有空格
                               happy()            -----> def happy():
                                                             print("Happy birthday to you!')
