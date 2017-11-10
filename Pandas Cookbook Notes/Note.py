# Note 1

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



# Chapter 2
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




# My practices
# 新增一行：
df.loc['行名']= 

# Note 3

## 探索性数据分析EDA
数据可以分为连续型变量和类别型变量。连续型数据一定值数值型的，分类变量是离散型的。

###汇总统计：类别变量；转置操作；
df.describe(include=[np.object, pd.Categorical]).T  # 转置操作可以增强可读性，当列很多时

### Data Dictionaries很重要，合作必需。

## 改变数据类型，节省内存
df.col.memory_usage(deep=True)             # 每列占用的内存
df['clo2'] = df['col2'].astype(np.int8)                 # 只有0/1 2个值的，可以转化为8-bit integer

### object -> categorical，当该列有比较低的基数(number of unique values)
df.select_dtypes(include=['object']).nunique()   # 查看唯一值的个数，< 1%可以考虑转换类型
df['col3'] = df['col3'].astype('category')

