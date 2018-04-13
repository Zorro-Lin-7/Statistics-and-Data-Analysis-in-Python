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
    
# √ 面向对象的程序设计：
真实世界中的object，有【状态】和【行为】，也就是attributes／features 和 methods. 比如：
    * 猫
        状态：名字、颜色
        行为：喵叫、摇尾巴、睡觉
    * 台灯
        状态：开、关
        行为：打开、关闭
  类：某种类型【集合】的描述。例：人
    属性：【类】本身的一些特性，比如身高、体重、名字；具体值根据每个人不同而不同
    方法：【类】所能实现的行为，如吃饭、走路、睡觉
    
面向对象的特点：
  封装：
    从业务逻辑中抽象对象时，赋予对象相关数据与操作，把一些数据和操作打包在一起的过程就是【封装】；
    对象的实现和使用是独立的；
    支持代码复用。
    
# 类的定义    例：找出GPA最高的学生.py：
class Student(object):    # Student 学生的属性和方法封装在类的内部；
    def __init___(self, name, hours, qpoints):
        self.__name = name       # 前面加双下划线表示私有变量，不能外部访问、修改
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self):
        return self.name
      
    def getHours(self):
        return self.hours
      
    def getQPoints(self):
        return self.qpoints
      
    def gpa(self):
        return self.qpoints/self.hours
      
# >>> student1 = Student('小明', 10, 3)
# >>> student1.hours
# 10
# >>> student1.qpoint
# 3
# >>> student1.getName()

def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)     # √ 像调用函数一样调用类；Student类可以被多个程序、多个对象所使用
  
def main():
    filename = input('Enter name the grade file: ') # 打开输入文件
    infile = open(filename, 'r')
    best = makeStuent(infile.readline())  # 设置文件中第一个学生的记录为best
    
    for line in infile:    # 处理文件剩余行数据
        s = makeStudent(line) # 将每行数据转换为一个记录
        if s.gpa() > best.gpa(): # 如果该学士是目前GPA最高的，记录下来
            best = s
    infile.close()
    
    print(best.getName())  # 打印GPA成绩最高的学生信息
    print(best.getHours())
    print(best.gpa())
    
if __name__ == '__main__':
    main()
    

# 类的一大作用是，打包一团代码，避免spaghetti code 影响可读性。所以需要创建类。
A class is essentially a method for packaging code. 
The idea is to simplify code reuse, make applications more reliable, and reduce the potential for security breaches. 
Well-designed classes are black boxes that accept certain inputs and provide specific outputs based on those inputs.


# Creating the class definition
A class need not be particularly complex. 
In fact, you can create just the container and one class element and call it a class.

class MyClass:
    MyVar = 0

MyInstance = Myclass()  # 创建实例需要加括号
MyInstance.MyVar
0

# Creating class method
class Myclass:
    def SayHello():    # 该mehtod 不需要接收参数
        print('Hello')
        
MyClass.SayHello()    # 可以直接执行，无需创建这个类的一个实例
或者
MyInstance = Myclass  # 创建的是类，无需括号
MyInstance.SayHello()

类方法只能处理类数据。它不知道与该类的实例相关联的任何数据。
您可以将数据作为参数传递，并且该方法可以根据需要返回信息，但是它不能访问实例数据。
因此在创建类方法时，需要小心谨慎，以确保它们本质上是自包含的。

# Creating instance method 上面是类方法，这是实例的方法
instance method 是单个实例的一部分。你通过instance method 来处理类管理的数据。
因此，只有将类中的某个instance method 实例化为一个object 才能使用它

class MyClass:
    def SayHello(self):  # 所有实例方法都要有self参数，区分于类方法。SayHello方法不接受任何特殊参数也不返回任何值，仅仅print.
        print('Hello')

MyInstance = Myclass()  # 将类中的某个instance method 实例化为一个object，需要加括号
MyInstance.SayHello()  

self 指向应用程序用于操作数据的特定实例。
如果没有self参数，该方法将不知道要使用哪个实例的数据。
然而，self不被视为是一个可访问的参数-它的值由Python提供，且作为调用方法的一部分你不能改变它。  

# Constructors “构造函数” __init__()
Constructors 是一种method，一类特殊的method。
Python什么时候调用这个method（constructor/function）？
在类中定义了functions/methods，其中含有constructor，通过它来实例化一个object时。
Python依靠constructor来执行一些任务，如初始化一些instance variable（即赋值）。
Constructors能确保对象在启动时有资源可用。
The name of a constructor 总是相同，为__init__() 。
当必须创建某对象时，构造函数可以接收参数。
当你创建一个没有constructor的类时，Python会自动为你创建一个 default constructor，它不做任何事。
每个类都必须要有一个constructor，即使仅仅作为default constructor来依赖。

class MyClass(object):
    def __init__(self, Name = 'there'):
        self.Greeting = Name
    
    def SayHello(self):
        print("Hello {0}".format(self.Greeting)) # self，顾名思义，调用自身的属性特征（变量）
        
MyInstance = MyClass()    # 创建一个类的实例
MyInstance.SayHello()     # Hello there 采用默认参数

MyInstance2 = MyClass('Amy')    # 可以将__init__()看出隐形的，用于构造类本身的特征。创建实例时直接在类中传入参数'Amy'，相当于设置类自身的属性self.Greeting
MyInstance2.SayHello()   # Hello Amy

MyInstance.Greeting = "Harry"
MyInstance.SayHello()    # Hello Harry

# 类中的变量
变量是存储数据的容器。
使用类时，需要考虑数据是如何存储与管理的。
一个类可以同时含有class variables 和 instance variables。#The class variables are defined as part of the class itself, while instance variables are defined as part of the methods.
class variables 被定义为类自身的一部分；
instance variables 被定义为mehtods的一部分。
# Creating 	class variables
类变量是全局性的，提供给你的的类以某种方式操作数据的全局访问。
大部分情况下，你可以使用constructor来初始化全局变量，使包含已知的值，从而可在之后被调用：

class MyClass:
    Greeting = ''
    def SayHello(self):
        print('Hello {0}'.format(self.Greeting))
        
-------------------------------------    
    
    
print(value,...,sep=' ', end='\n') # print() 打印空行，即换行

# 字典的方法
>>>student = {'小明':'男', '小红':'女'}
>>>tuple(student.keys())    # 结合tuple使用
>>>student.get('小明')      # get
'男'

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
# 若有多个return，第一个return执行即结束： 
def first_return():
    if 2 > 1:
       return 2    
    return None

# 函数调用过程的树状解析：
def main():
    sing('Mike')    -----> def sing(person):
    print()                    print('Happy birthday, dear', person+'.')  # +连接字符串没有空格
                               happy()            -----> def happy():
                                                             print("Happy birthday to you!')
                                                                   
# 文件的基础
 文件：有序的数据序列
 编码：信息从一种形式转换为另一种形式。计算机存储、处理需要一种形式，比如出于节省空间的需求；人阅读、处理是另一种形式，出于汉字、西文的不同需求。
 二进制文件ASCII码：
    照片、音乐、视频、计算机程序等；
    优点：节省空间、表示更精确、采用二进制无格式存储
# 文件的处理： http://www.icourse163.org/learn/BIT-268001#/learn/content?type=detail&id=1003121198&cid=1003698546
1、打开：使硬盘上的文件与程序建立联系 
2、操作：读取、写入、定位、其他
3、关闭：切断程序与文件的联系；写入磁盘，并释放文件缓冲区

例：文件拷贝.py                                                                 
def main():
    f1 = input('Enter a filename').strip() # 用户输入文件名
    f2 = input('Enter a filename').strip()
    
    infile = open(f1, 'r')  # 打开文件
    outfile = open(f2, 'r') 
    
    # 拷贝数据
    countLines = countChars = 0
    for line in infile:  # 当文件很大时，若用infile.readlines() 读入为一个列表会占用很大内存；
        # 逐行处理文件内容
        countLines += 1  # 统计文件有多少行
        countChars += len(line) # 统计文件有多少字符数
        outfile.write(line)
    print(countLines,  'lines end', countChars, 'chars copied') # x行 y个字符
    
    infile.close()
    outfile.close()
    
main()
    
# dir 获得一个对象的所有属性和方法  √ 重点。比如 DataFrame groupby 之后的对象类型是 DataFrameGroupby，该对象的方法有 .agg, max 等等 
a = 'ABC'                                                               
dir(a) 

# collections.defaultdict
https://www.jianshu.com/p/26df28b3bfc8
