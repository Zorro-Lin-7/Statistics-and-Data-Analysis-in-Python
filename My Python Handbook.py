print(value,...,sep=' ', end='\n')

input() # 产出的是string, 若输入数字，需要 int(input())

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

