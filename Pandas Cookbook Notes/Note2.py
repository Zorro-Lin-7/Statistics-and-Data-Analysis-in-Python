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
