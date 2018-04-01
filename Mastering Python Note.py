# 搜索关键字：应该写成；√；例；


第二章的学习目标是: to learn What code is beautiful and Why certain decisions have been made in Python style guide.


Common pitfalls p149
----------------------------------
## Scope matters

{----定义函数时，参数犯错：

def spam(key, value, list_=[], dict_={}):
    list_.append(value)
    dict_[key] = value
    
    print('List: %r' % list_)
    print('Dict: %r' % dict_)
    
Spam('key 1', 'value 1')
Spam('key 2', 'value 2')
    
应该写成：
def spame(key, value, list_=None, dict_=None):  # 自定义函数时，避免mutalbel object 作 default parameters
    if list_ is None:    # is 的用法：is True; is None. 而非 == True 来判断。
        list_ = []
    
    if dict_ is None:
        dict_ = {}
        
    list_.append(value)
    dict_.[key] = value
    
    print('List: %r' % list_)
    print('Dict: %r' % dict_)
    
----}

{----同样的问题发生定义类时，混淆 类属性和 实例属性：

class Spam(object):
    list_ = []  # 公共变量
    dict_ = {}
    
    def __init__(self, key, value):
        self.list_.append(value)
        self.dict_[key] = value
        
        print('List: %r' % self.list_)
        print('Dict: %r' % self.dict_)
        
Spam('key 1', 'value 1')
Spam('key 2', 'value 2')
        
应该写成：

class Spam(object):
    def __init__(self, key, value):
        self.list_ = [key]    # 将mutalbe object 初始化在__init__ method 中，避免在实例间共享
        self.dict_ = {key: value}
        
        print('List: %r' % self.list_)
        print('Dict: %r' % self.dict_)

----}

{----类之间的继承会疏忽的混用问题：

class A(object):
    spam = 1
    
class B(A):
    pass

A.spam    
B.spam  # 也为1，父类属性会被子类继承，除非覆写

A.spam = 2
B.spam # 为2，也会继承父类的改动。

但我们只想改变A.spam，B.spam不变呢？应该写成：

永远不要改动类属性，只对实例属性做改动。

-----}

{----定义函数时，全局变量与局部变量问题

spam = 1
def eggs():
    spam += 1    # 任何包含"spam = "的语句会变量变成local variable。尽管global 范围里赋值过，但此处仍无值。也建议尽量避免global variables
    print('Spam: %r' % spam)

eggs()    # 会报错

应该写成：

def eggs():
    spam = 1
    print('Spam: %r' % spam)

----}

## Overwriting and/or creating extra built-ins”
{----变量名不要与内建变量名冲突，用加下划线

list = [1, 2, 3]

应该写成：

list_ = [1, 2, 3]

----}

## Modifying while iterating
{----当迭代一个mutable objects，如list，dicts，sets，你无法改动它们，会发生RuntimeError:

dict_ = {'spam': 'eggs'}
list_ = ['spam']
set_ = {'spam', 'eggs'}

for key in dict_:
    del dict_[key]
    
for item in list_:
    list_.remove(item)

for item in set_:
    set_.remove(item)
    
应该写成：

dict_ = {'spam': 'eggs'}
list_ = ['spam']
set_ = {'spam', 'eggs'}

for key in list(dict_): # 使用list最方便的
    del dict_[key]
    
for item in list(list_):
    list_.remove(item)

for item in list(set_):
    set_.remove(item)
    
----}

## 捕捉异常：python2 与python3 的不同-垃圾回收、性能问题等未求甚解
{----很多人习惯python2，python3 兼容python2 的语法，故可用:
try:
    ....
except (ValueError, TypeError) as e:
    print('Exception: %r' % e)


def spam(value):
    try:
        value = int(value)
    except ValueError as exception: # 这里会报错，因为python3 将as 后面的变量 变为了local variable
        print('We caught an exception %r' % exception)
    
    return exception
    
spam('a')
spam('10') # 没有异常的话应当不报错

应该写成：

def spam(value):
    exception = None    # 若后面要用到该变量，则需要在try/except语块前声明
    try:
        value = int(value)
    except ValueError as e:
        exception = e   # python3 内部实际上会执行 finally: del exception，因此需要认为保存。至于内存漏洞等细节，此处不谈
        print('We caught an exception %r' % exception)
    
    return exception

spam('10')
spam('a')

----}

# 闭包的late binding

{----Closures闭包是代码中进行局部实现的一个method。
它们可以在不覆写全局范围内的变量的情况下，在局部定义变量，之后再隐藏变量。
问题是，由于性能原因，Python尽可能迟地绑定它的变量。虽然通常很有用，但确实有一些意外的副作用:

eggs = [lambda a: i * a for i in range(3)] 
for egg in eggs:
    print(egg(5))  # 实际输出都是10，而非0，5，10； 由于迟绑定，变量i直到被调用时才从周围环境（就近）调用，而不是当实际定义时就调用。

应该写成：
import functools    # 如前所述，变量需要局部化，一个方法是通过functools.partial 强制立刻绑定

eggs = [functools.partial(lambda a: i * a for i in range(3))]
for egg in eggs:
    print(egg(5))

更好的完全避免绑定问题的方案是 不要引入extra scopes(lambda)，它引入了额外变量。如果i 和a 同时作为参数赋给lambda，不会有问题。

----}

## Circular imports
{----2个.py文件：运行spam.py 会发生circular import 错误
eggs.py:

from spam import spam

def eggs():
    print('This is eggs')
    spam()
    
spam.py:
f

from eggs import eggs

def spam():
    print('This is spam')
    
if __name__ == '__main__':
    eggs()

应该写成：

eggs.py:

import spam  # 我推荐：只使用module import 代替 function import；常建议重构代码，最佳方案要看具体问题。

def eggs():
    print('This is eggs')
    spam.spam()
    
spam.py:
f

import eggs

def spam():
    print('This is spam')
    
if __name__ == '__main__':
    eggs.eggs()

还有其他方案，但并不值得提倡。比如dynamic import----}

## Import collision 导入冲突
{----包名相同，环境变量不清导致

import spam

应该写成:

from . import spam

----当包重名时，只从当前的package中导入，而非 global package。建议多尝试使用虚拟环境}

第三章
时间复杂度（time complexity）,用O标记：一个function，一段代码，花 O(1) 时间，指执行过程只需“走” 1 step。类似的，O(n)即要走n步。n是size of the object，如一个1000元素的list对象，size为1000.
算法：程序执行的步骤。C代码通常比Python快，但如果使用了错误的算法，也无济于事。通常O是一个平均概念，而不是极值概念。

举例说明：遍历一个1000个元素的列表（以确认一个元素是否存在于该列表）要花O(n)，即1000步。做100次，将花100*O(n)=100*1000步。
但若用Dict，确认某个元素是否存在只需O(1)，100*O(1)=100*1=100步。所以，使用字典比列表大约快1000倍。

{----更具体的，“步”即for 循环：√
# O(1):
def o_one(items):
    return 1    # one operation so O(1)
    
# O(n):
def o_n(items):
    total = 0
    for item in items:    # Walks through all items once so O(n)
        total += 1
    return total
    
# O(n**2):
def o_n_squared(items):
    total = 0
    for a in items:    # 2层循环， so O(n**2)
        for b in items:
            total += a * b
    return total

n = 10
items = range(n)
o_one(items) # one operation
o_n(items)  # n = 10 operations
o_n_squared(items)  # n*n = 10*10 = 100 operations
----}

## List
{----List，大部分方法的时间复杂度很低，比如append，get，set，len，为O(1)；但可能不曾留意remove 和insert 是O(n)，
所以，要从1000个元素中删除1个，Python将遍历1000个项。其内部原理如下：

# remove
def remove(items, value):
    new_items = []  
    found = False # if not found = True，为了更像英文一样可读，所以设为False
    for item in items:
        if not found and item == value: # 跳过第一个找到的value
            found = True    # 只删除第一个找到的value，之后循环再找到时，if not found = Fasle 了
            continue # √ 跳过当前循环块中的剩余语句，进入下一轮
        new_time.append(item)  # 其他元素复制到新的列表
    
    if not found:  # if not found = True = if not False ， 为了更像英文一样可读，所以设为False
        raise ValueError('list.remove(x): x not in list') # √ 挂起Error
        
    return new_items	
        
# insert
def insert(items, index, value)	:
    new_item = [] 
    for i, item in enumerate(items):
        if i == index:
            new_items.append(value)
        new_items.append(item)
    return new_items
    
----这2个方法都需要copy the entire list，当list很大时，就会变得笨重。

----当要删除很多项时，filter 和 列表解析式会快很多，通过合理构造，只需copy一次：
举例来说：
删除从items里删除primes：

primes = set((1, 2, 3, 5, 7)) # size: m = len(primes) = 5
items = list(range(10))    # size: n = len(items) = 10

# Classic solution
for prime in primes:
    items.remove(prime) # remove 里copy一次（一个for循环），共2个for循环; O(m*n) = 5*10 = 50
    
# List comprehension
[item for item in items if item not in primes] # O(n*1)= 10*1 = 10

# Filter 最快
list(filter(lambda item: item not in primes, item)) # O(n*1) = 10

----}


{----min, max, in 也是O(n)，但对这类查找类型可以想见其结构不一定是最优的。代码实现如下：

def in_(items, value):
    for items in items:   
        if item == value: # 如果第一个就是，那么时间复杂度为O(1)；若不存在，则会执行完整个for，为O(n)
            return True
    reuurn False
    
def min_(items):
    current_min = items[0]
    for item in items[1:]:
        if current_min > item:
            current_min = item
    return current_min
    
def max_(items):
    current_max = items[0]
    for item in items[1:]
        if current_max < item:
            current_max = item
    return current_max
    
in_(range(5), 3)
min_(range(5))
max_(range(5))
        
----}

## Dict - 无序但快速映射
{----字典的平均复杂度，像方法get，set，del，如我们期望的，为O(1)，但偶尔不是。
字典的工作原理是，将key通过Hash function转换为hash值，存到hash table中。但会有2个问题。
1，items 会按hash值来排列，大部分是随机的；2，hash collisions，那么get等操作的复杂度将为O(n)。
Hash collisions 并不总发生，但会发生，当一个大字典执行效率低于平均时，那就是需要检查的问题所在。

例，最简单的Hash function/algorithm：返回一个数的首位数字 √

def most_significant(value)：
    while value >= 10:
        value //= 10
    return value
    
most_significant(12345)
most_significant(99)
most_significant(0)

至此，我们可以通过该Hasing method，即上面的函数，用a list of lists(列表为元素的列表)来枚举一个字典。
我们的Hasing method 只返回0-9，所以我们的list只需要10个buckets。
下面添加一些值，看看具体怎么work:

def add(collection, key, value):
    index = most_significant(key) # 字典的key 与列表的index 相联系
    collection[index].append((key, value)) 
    
def contains(collection, key):   # collection 中是否含有某个key
    index = most_significant(key)
    for k, v in collection[index]:
        if k == key:
            return True
    return False

# Create a collection of 10 lists
collection = [[], [], [], [], [], [], [], [], [], []]

# Add some items, using key/value pairs
add(collection, 123, 'a')
add(collection, 456, 'b')
add(collection, 789, 'c')
add(collection, 101, 'd')
>>>collection
[[],
[(123, 'a'),(101, 'd')],   # index = 1
[],
[],
[(456, 'b')], # index = 4
[],
[], 
[(789, 'c')], # index = 7
[],
[]]

# Check if the [contains] works correctly
contains(collection, 123) # True
contrain(collection, 1)  # False

以上代码并不全等同dict 的内部实现，但相当相似。比如要得到key=789的item (789:'c')，取index=7 的item 7即可，类似于dict.get(7)，
这里只需检索index=7 (10 个中找1个）， 而不是key=789。
大部分情况是n=1的O(1)，但如果找(101,'d')，则为O(n)。这就是一个hash collision.

此外，删除字典中的items 并不会改变dict 所占的内存。copying and iterating 整个字典仍将花费O(m)，m是字典的最大size，
而不是n--删除操作后的项数。因此，如果添加1000项到字典，再删除999项，iterating 和 copying操作仍将走1000 steps。
唯一的解法是recreating 该字典，其内部会执行copy 和 insert 操作。
注意，插入操作期间的重新创建 is not guarantedd，且依赖内部可用的空插槽数。

----}