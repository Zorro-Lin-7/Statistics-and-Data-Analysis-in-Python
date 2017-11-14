########### Note 1

# Jupyter 索引操作：
[](#)

pd.set_option('max_columns',8,'max_rows',10)
movie.get_dtype_counts()
Series.to_frame()

# 集合（字典）的运算：
&, |, +, -

# 选取列，用 df[''] 比df.column_name 可读性更分明；后者操作更便捷
 .quantile(.2)   等分
 .quantile([.2, .5, .7])

# 分布占比
director.value_counts(normalize=True)

# Series是否含缺失值
.hasnans	

# 链式方法，为了提升可读性，建议写成多行，若反斜杠换行比较麻烦，可以使用小括号包裹整个语句。
person.drive('store')\
      .buy('food')\
      .drive('home')\
      .prepare('food')\
      .cook('food')\
      .serve('food')\
      .eat('food')\
      .cleanup('dishes') 
# 链式也有缺点，比如debug很困难，难以追溯错在哪儿。
person1 = person.drive('store')
person2 = person1.buy('food')
person3 = person2.drive('home')
      
# 填充缺失值并转换数据类型：
data.fillna(0)\
    .astype(int)\
    .head()
    
# 缺失值统计：pandas将False／True 作0/1 计算
df.isnull()\
  .sum()    # 统计缺失值数量
df.isnull()\
  .mean()   # 统计缺失值占比


# 索引index操作
df.set_index('column_name',drop=True)
df.reset_index()  # Rangeindex

# 指定更改某个列名、行名
indexes_renamed = {'a':'b'} # a 改为b
columns_renamed = {'c': 'd'}
df.rename(index=indexes_renamed,
          columns=columns_renamed)
          
# 列的位置序号：
df.columns.get_loc('column_name')
df.insert() # 插入某列



########### Chapter 2
#拿到一个数据集后，可能需要重新排“列”——离散、连续；含缺失、无缺失；数值、非数值；等等。
# 排列规则并无标准，比如：
# 1、区分一列是离散或连续  需要自己一个一个去看
# 2、在离散或连续列中，再细分组
# 3、 重要的组放前面，其中类别列放连续值列前面


# 选取多列——[[]]
# tuple 的逗号可省略：
#>>> tuple1 = 1,2,3,'a','b'
#>>> tuple2 = (1,2,3,'a','b')
#>>> tuple1 == tuple2
#     True

## .select_dtypes()
movie.get_type_counts()
movie.select_dtypes(include=['int'])
movie.select_dtypes(include=['number'])
movie.select_dtypes(include=['object'])

## .filter 只检查列名，不涉及具体的数据值
movie.filter(like='facebook',axis=0)
movie.filter(regex='\d', axis=0)



pd.option.display.max_rows = 10

movie.describe(percentiles=[.01, .3, .99])

movie.min(skipna=False)

# 参数axis=1，可以想象新增1列；axis=0,新增1行；

.cumsum(axis=1) #累加

pd.set_option('precision',n) # 显示时，保留小数位数
# 保留2位小数：地板除
df // 0.01 / 100

# 2个df是否一致，不能用==，因为NA无法比较，用df1.equals(df2)

################## Note 3

## 探索性数据分析EDA
数据可以分为连续型变量和类别型变量。连续型数据一定值数值型的，分类变量是离散型的。

###汇总统计：类别变量；转置操作；
df.describe(include=[np.object, pd.Categorical]).T  # 转置操作可以增强可读性，当列很多时

### Data Dictionaries很重要，合作必需。

## 改变数据类型，节省内存
df[['col1','col2']].memory_usage(deep=True)        # 每列占用的内存;必须设置deep=True才能准确提取每个值的内存，尤其Object类型；
df['clo2'] = df['col2'].astype(np.int8)                 # 只有0/1 2个值的，可以转化为8-bit integer

### object -> categorical，当该列有比较低的基数(number of unique values)
df.select_dtypes(include=['object']).nunique()   # 查看唯一值的个数，< 1%可以考虑转换类型
                                                 #注：object类型不像其他数据类型，并不是列中的每个值都是同一类型；它像一个catchall，可能包罗各种类型。
df['col3'] = df['col3'].astype('category')

#注：Python3 采用Unicode编码，每个字符占4 bytes；Pandas 一列内存>100 bytes，则超出的每个字符占5 bytes
#注：如果某数值列含有缺失值，该列类型必是 float64; Integer 数据类型会自动变为 float，如果它有了缺失值，
#    也因此，无法 .astype(np.int8)——ValueError: Cannot convert non-finite value (NA or inf) to integer.
# RangeIndex 是占内存最小的数据类型，若变成Int64Index，内存需求放大巨多：
>>> df.index = pd.Int64Index(df.index)

## 选择A值top100的行，A值top100且B值button5 的行
df.nlargest(100,'A',keep=False)  # 但该参数可能有问题，可能未修复。
df.nlargest(100,'A').nsmallest(50,'B')

## 多级排列再筛选
df_sorted = df.sort_values(['A','B','C'],ascending=[False,True,False]).head()

# 累计更大值、累加、累乘
df['A'].cummax()
df['A'].cumsum()

########## Note 4
 ## 混用数值和labels进行切片，以前的版本可用.ix实现，现在的.iloc 或.loc 已无法实现：
 >>> df.loc[:5, 'A':'Z'] # 会报错
 >>> col_start = df.columns.get_loc('A')
 >>> col_end = df.columns.get_loc['Z'] + 1
 >>> df.iloc[:5, col_start:col_end] #先用.get_loc 将labels转换成integer，再用.iloc；
 >>> df.loc[:, 'A':'Z'][:5] # 虽然能用链式连用.loc .iloc 来实现，但非常不建议。简单的尚可。

## 加速计算：用.iat .at 代替 .iloc .loc 

 ## index 是字母，非数值的，排序后，能用.loc 按字母顺序切片，像查字典一样
>>> df = df.sort_index()
>>> df.loc['Ax': 'Az']
 # 可以用 df.index.is_monotonic_ 来检查是否顺排
 
 ########## Note 5
 
 (df['A'] > 100).mean()  # 计算 > 100 的值的占比 ，该方法错误。因为 >100的结果输出是True／False ，而A中本身含有会被当作False的NaN
 df['A'].dropna().gt(100).mean()   # 需要排除 Nan导致的False个数不准确
 
 ## 可以同时比较1个df中的2列：
 a = df[['A','B']].dropna()
(a['A'] > a['B']).mean()
 
 and: &
 or: |
 not: ~
 
 ## 多布尔条件筛选：条件另创建变量，再合并这些变量。代码更规范整洁
 criteria1 = df['A'] > 1
 criteria2 = df['B'] == 'abc'
 criteria3 = ((df['C'] < 100) | 
              (df['C'] > 200))
 
 criteria_final = criteria1 & criteria2 & criteria3
 criteria_final.head()
 df[criteria_final]
 
 cols = ['A','B','C']
 df.loc[criteria3, cols]
 
 ## Python中，非0整数、非空字符串、非空序列都可为布尔值True
 
 # 更快地检索：
 ## 按index检索 比布尔检索快3倍左右，但重置一列为index可能抵消。若不用重置index，可以考虑index检索。
 df[df['A'] == 'a']
 df2 = df.set_index('A')
 df2.loc['a']
 
 ## 当index唯一或顺排，index selection performance 大幅提升
 ## 原理：未排序且含有重复值时，pandas需要检验index的每个值以正确选择，排序后，pandas利用binary search 算法提高性能；
 ##      值唯一时，pandas通过hash table实现快速检索，每个索引坐标以近乎相同的耗时被查找，无论它的长度。
 df1
 df2 = df1.set_index('A')
 df2.index_is_monotonic     # 检查是否单调; is_unique 检查是否唯一
 df3 = df2.sort_index()     # index 排序
 
 %timeit df1[df1['A'] == 'z']
 %timeit df2.loc['z']
 %timeit df3.loc['z']
 
 ## 拼接多列，作为新索引
 df.index = df['Country'] + ', ' + df['city']
 df = df.sort_index()
 
 >>> %%timeit
 >>> crit1 = df['Country'] == 'China'
 >>> crit2 = df['City'] == 'Beijing'
 >>> df[crit1 & crit2]
 
 >>> %timeit df.loc['China, Beijing']    # 速度快1个量级
 
 
 
##################### My practices
# 新增一行：
df.loc['行名']= 

# 查最大（小）值的索引——元素在列表中的索引（位置）
t = [1,2,3,4,5]
t.index(max(t))

s = pd.Series(t)
s.idxmax()
s.idxmin()

df['col'].argmax()

# 一列Series 或 index是否有单调性，即排过序，包括字母：
s.is_monotonic_decreasing or s.is_monotonic_increasing
