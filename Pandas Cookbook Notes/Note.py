# Note 1
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

set()

pd.option.display.max_rows = 10

movie.describe(percentiles=[.01, .3, .99])

movie.min(skipna=False)

.cumsum(axis=1) #累加

.ge(.15)?
.eq()?
