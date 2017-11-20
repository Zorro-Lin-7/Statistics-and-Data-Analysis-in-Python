# http://python.jobbole.com/87136/

import seaborn as sns
import matplotlib.pyplot as plt
# sns.set(style='white', color_codes=True)

# 同时画直方图、散点图
sns.jointplot(x='', y='', data=, size=)

# 通过这个曲线图可以看出不同特征值时的分布密度
sns.FaceGrid(data, hue='status',size=)   # hue通常是分类特征，如y
   .map(sns.kdeplot, 'overdue_day')
   .add_legend()
   
# 修改参数dige_kind
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")

#  pairplot显示不同特征之间的关系
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)
# 修改参数dige_kind
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")

# ======= Matplotlib 基础 =========

plt.plot(x,    
         y, 
         format_string, # 控制曲线的格式,由颜色、风格、标记组成
         **kwargs)      # 扩展函数：第二组或更多(x,y,format_string)；
						#         markerfacecolor='blue' 标记颜色，可用于区分连线的颜色
                        #         markersize=20          标记尺寸      
#例1:
plt.plot([3,1,4,5,2])         # 默认线图
plt.ylabel('Grade')
#plt.savefig('test', dpi=600)  # PNG文件，每个英寸包含600个像素点（很高了）

#plt.axis([-1, 10, 0, 6])    # 横轴[-1, 10], 纵轴[0, 6]
#plt.grid(True)

plt.show()

#例2:
a = np.arange(10)
plt.plot(a, a*1.5, 'go-',
         a, a*2.5, 'rx',
         a, a*3.5, '*', # 未指定颜色和划线标记，系统会自动给出其他颜色，不划线
         a, a*4.5, 'b-.')
# 中文显示：
# 方式一：全局设置
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 20


# 方式二：局部设置
plt.xlabel('横轴：时间', 
           fontproperties='SimHei', # 指定字体
           fontsize=20) # 字体大小

# 文本显示函数：
plt.xlabel('横轴：时间',fontproperties='SimHei', fontsize=20, color='green')
plt.ylabel()
plt.title(r'正弦波$y=cos(2\pi x)$') # 支持Latex 数学公式
plt.text()  # 任意位置增加文本

plt.annotate(      # 在图形中增加带箭头的注解
    r'$\mu=100$',  # 文本
    xy=(2, 1),     # 箭头指向的位置
    xytext=(3, 1.5), # 文本所在的位置
    arrowprops=dict(facecolor='black',  # 箭头属性
    shrink=0.1,
    width=2)) 

#pyplot的绘图区域
plt.subplot(nrows, ncols, plot_number)

#例：
plt.subplot(3,2,4)  # 定义3行2列，第4个绘图区；逗号可省略
plt.plot([1,2,3,4])
plt.show()

##更复杂的子绘图区域： gridspec子类
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(3, 3) # 设定3x3网格

ax1 = plt.subplot(gs[0, :]) # 选中网格，确定选中的行列网格数
ax2 = plt.subplot(gs[1, :-1]


