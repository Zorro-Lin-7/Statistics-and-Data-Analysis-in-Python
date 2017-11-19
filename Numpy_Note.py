# 参考资料：Python数据分析与展示, 北京理工大学, 嵩天

# IPython 的常用 % 魔术命令
%reset   # 删除当前命名空间中的全部变量或名称
%who     # 显示IPython当前命名空间中已定义的变量
%time statement   # 给出代码的执行时间,statement 表示代码语句
%timeit    # 多次执行代码，计算综合平均执行时间
%run demo.py
%magic   # 显示所有魔术命令
%hist    # 历史记录

# Numpy 基础
## ndarray对象的属性
.itemsize    # 数组中每个元素的大小，以字节为单位

ndarray的元素类型：
问：Python语法仅支持整数、浮点数、复数3种，为什么Numpy更细分，如int8, int32 ?
答：科学计算设计的数据多，对存储和性能要求高；
    对元素类型精细定义，有助于Numpy 合理使用存储空间并优化性能；
    有助于程序员对程序规模有合理评估。
    
ndarray数组可以有非同质对象构成，类型为Obeject，无法发挥Numpy优势，要尽量避免。如
x = np.array([[0, 1, 2, 3],
              [9, 8]])    # 列表元素的长度不一样也为非同质

## ndarray 维度、类型的变换               
np.array(list/tuple)
np.arange()  # 默认元素类型为np.int64，下面几种方式默认为np.float64，除非指定
np.ones(tuple, dtype=) ## 生成全是1的数组，shape为tuple类型
np.zeros(tuple, dtype=)
np.full(tuple, val=)
np.eye(val) # 正方的n*n 单位矩阵，对角线为1，其余为0

np.ones_like(a)  # 根据a的shape生成
np.zeros_like(a)
np.full_like(a, val)

np.linspace(start, stop, num= ,endpoint=True) # 等间距数组，右闭区间
np.concatenate  # 合并数组

# 元素级运算：Numpy的设计理念是把数组当作一个数来运算
## 几个不熟的函数：
np.rint(x)    # 对每个元素四舍五入
np.modf(x)    # 将各元素的小数和整数部分分离返回
np.sign(x)    # 返回各元素符号1(+)、0（0）、-1(-)
np.maximum(x,y)
np.minimum(x,y)

# 存储、导出导入
## 以下两个用于csv，csv只能存取一维或二维数组
np.savetxt(frame,    # 文件、string或产生器，可以是.gz	或.bz2的压缩文件
           array,
           fmt='%.18e',  
           delimiter=None)  # 默认空格
           
np.loadtxt(frame,
           dtype=np.float,
           delimeterNoen,
           unpack=False)
           
例：np.savetxt('a.csv', a, fmt='%d', delimeter=',')

# 任意维度的存取：二进制文件，作备份用。
np.save(fname, # .npy为扩展名，压缩扩展名为.npz
        array)

np.load(fname)

# 随机数函数子库 np.random.*
.rand()    # [0,1), 均匀分布
.randn()   # 标准正态分布
.rando(low[high,shape])     # 整数

# 例：
np.random.seed(10)
a = np.random.rand(3, 4, 5) # a.shape = 3x4x5

若要复现：
np.random.seed(10)
b = np.random.rand(3, 4, 5) # a == b

.uniform(low,high,size)    # 均匀分布
.normal(loc,    # 均值     # 正态分布
        scale,  # 标准差
        size)    
.poisson(lam,   # 随机事件发生的概率
         size)

# 统计函数
ptp(a) # 计算最大与最小值的差

# 梯度函数：常用于声音、图像处理，用于发现声音、图像的边缘，其变化不平缓的地方可以容易发现
np.gradient(f) # 梯度：连续值之间的变化率，即斜率。如y=[a,b,c], b的梯度:（c-a)/2, a的梯度：(b-a)/1; c的梯度：(c-b)/1

# 图像的数组表示及变换
from PIL import Image
a = np.array(Image.open('../xihu.jpg'))  # 图变成数组
print(a.shape, a.dtype)
b = [255, 255, 255] -a                   # 原图色彩变换
im = Image(fromarray(b.astype('uint8'))  # 数组变成图
im.save('../change_color.jpg')




-------
概念理清：
【数据的】维度（feature）：
一个数据：3.14，表达一个含义
一组数据：3，4，5，3.14 表达一个或多个含义
	维度：一组数据的【组织】形式
		一维数据：采用线性方式组织，对应列表、数组、集合等概念；
			列表：数据类型可以不同：3,'abc', 4, 3.14
			数组：数据类型相同
		二维数据：由多个一维数据构成，是一维数据的组合，如表格。
		多维数据：由一维或二维扩展，如2张表添加时间维度，一张2016，一张2017	
        高维数据：（嵌套）字典，json
        
【数组的】维度（feature values)：
shape = (2,3) 是2维 # 分别对应从外到内，从行到列
shape = (2,3,4) 是3维
shape = (2,3,4,5) 是4维 

图像数据化，RGB：各取值范围在[0，255],
图像是由像素组成的二维矩阵，每个元素是一个RGB值如(1,2,255)，
图像是一个三维数组，分别是高度、宽度、像素RGB值。即3各特征