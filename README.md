# 统计学的Python实现
学过了国外高校的经典教材《Statistics for Business and Economics》，但统计学的理论掌握仍然停留在纸面上，很容易淡忘。理论总是枯燥的。

刷过了《Python for Data Analysis 》，但这本书更偏向于工具书，代码比较孤立，缺乏应用场景。那么多函数、方法，也是敲过就忘。包括一些包的官方文档。

浏览过的，将二者结合的博客、教程，要么太浅不深入，要么不贴合应用。（天下乌鸦一般黑，老外的书名也很标题党。）
专门适用于统计学的R语言，以及相关的好内容可能有，但《R in action》 浏览了下，暂时分不出精力，还是先专精好Python吧。

后来总算找到一个Statistics in Python 的教程，非常棒，更当得起‘Python for Data Analysis’这个名头。因为自身学习需求，在此梳理及融会所学的统计学理论、应用、代码实现。
涉及的包：Numpy/ Pandas/ Scipy/ Sklearn

## 目录
### [1-初始数据探索](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/14-%E5%88%9D%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%8E%A2%E7%B4%A2.ipynb)
* 原则：从少到多，快速启动，迭代优化
* 阅读、观察数据（维度、变量类型、数量、统计汇总、缺失值）
* 变量探索
    * 约减
    * 转换transform
    * 缺失值、异常值
    * 创建新变量
* 泰坦尼克案例实践

### [2-数值数据预处理](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/16-%20%E6%95%B0%E5%80%BC%E6%95%B0%E6%8D%AE%E9%A2%84%E5%A4%84%E7%90%86.ipynb)
* 归一化 ：量纲处理 preprocessing.scale()，无关分布
* 分布偏斜的处理：将偏态分布转换为正态分布
* 变量相关系数：
    * 两变量间（线性）相关关系的度量： 皮尔逊（积矩）相关系数
    * scatter_matrix
    * 注：这里讨论的相关性，限于两个单独的变量；
        * 而后面 假设检验 所讨论的“相关性”，基于样本与总体、样本与样本，限于（样本/总体）均值、比例
* 缺失值插补 : sklearn.preprocessing.Imputer

### [3-合并数据](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/18-Mering%20Data%20%E5%90%88%E5%B9%B6%E6%95%B0%E6%8D%AE.ipynb)
* pandas.merge()

### [4-频数表（交叉表、列联表）](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/19-%E9%A2%91%E6%95%B0%E8%A1%A8%EF%BC%88%E4%BA%A4%E5%8F%89%E8%A1%A8%E3%80%81%E5%88%97%E8%81%94%E8%A1%A8%EF%BC%89.ipynb)
* pandas.crosstab(index= ,
                columns= ,
                     margins= )

* 取比例，整个df 沿行横着除以某列：df.div(axis=0)
* 高维表

### [5-用 Pandas 绘图](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/20-%E7%94%A8%20Pandas%20%E7%BB%98%E5%9B%BE.ipynb)
* 直方图 Histgram
* 箱线图 Boxplot
* 概率密度函数曲线 Density
* 条形图 Barplot
* 散点图 Scatter
* 线形图 Line

### [6-描述性统计](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/21-%E6%8F%8F%E8%BF%B0%E6%80%A7%E7%BB%9F%E8%AE%A1.ipynb)
* 中心的衡量：均值、中位数
* 离散程度的衡量：方差、标准差、绝对中位差
* 分布的偏斜衡量：偏度、峰度

### [7-概率分布](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/22-%E6%A6%82%E7%8E%87%E5%88%86%E5%B8%83.ipynb)
* 离散分布：二项、泊松、几何
* 连续分布：均匀、正态、指数

*  stats.distribution.rvs()
*  stats.distribution.cdf()
*  stats.distribution.ppf()
*  stats.distribution.pdf()
*  stats.distribution.pmf()

### [8-点估计与置信区间](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/23-%E7%82%B9%E4%BC%B0%E8%AE%A1%E4%B8%8E%E5%8C%BA%E9%97%B4%E4%BC%B0%E8%AE%A1.ipynb)
* 点估计
* 抽样分布与中心极限定理，及作图
* 置信区间及作图；边际误差公式：
    * 总体标准差σ已知：z-critical value
    * 总体标准差σ未知：t-critical value; t 分布
* stats.distribution.interval()

### [9-假设检验与 T-test（数值变量）](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/24-%E5%81%87%E8%AE%BE%E6%A3%80%E9%AA%8C%20%E5%92%8C%20T-test%EF%BC%88%E6%95%B0%E5%80%BC%E5%8F%98%E9%87%8F%EF%BC%89.ipynb)
* 假设检验基础概念
* 什么情况下用T-test：
    * One-Sample T-test:
            stats.ttest_1samp() Calculates the T-test for the 【mean】 of ONE group of scores.
    * Two-Sample T-test:
            stats.ttest_ind()  Calculates the T-test for the 【means】 of TWO INDEPENDENT samples of scores.  
    *  paired T-test:     
            stats.ttest_rel()  Calculates the T-test on TWO RELATED samples of scores

### [10-卡方检验：拟合优度、独立性检验（分类变量）](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/25-%E5%8D%A1%E6%96%B9%E6%A3%80%E9%AA%8C%EF%BC%9A%E6%8B%9F%E5%90%88%E4%BC%98%E5%BA%A6%E3%80%81%E7%8B%AC%E7%AB%8B%E6%80%A7%E6%A3%80%E9%AA%8C%EF%BC%88%E5%88%86%E7%B1%BB%E5%8F%98%E9%87%8F%EF%BC%89.ipynb)
* 拟合优度检验：检验的对象是【2个分布】，（过程）只涉及1个变量，但1个分类变量涉及不同水平
    * stats.chisquare(f_obs=observed,f_exp=expected)   
        --The chi square test tests the null hypothesis that the categorical data has the given frequencies.
                    
* 独立性检验：检验的对象是【2个变量】（的相关性），（过程）在同一分布中，2个变量的不同水平两两比较
    * stats.chi2_contingency()      
        --Chi-square test of independence of variables in a contingency table

### [11-方差分析ANOVA](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/26-%20%E6%96%B9%E5%B7%AE%E5%88%86%E6%9E%90.ipynb)
* ANOVA与前面讨论的检验的区别
* scipy.stats.f_oneway()         
* statsmodels.stats.multicomp.pairwise_tukeyhsd()   事后检验 Tukey's test.

### [12-线性回归](https://github.com/Zorro-Lin-7/Statistics-and-Data-Analysis-in-Python/blob/master/Statistics%20in%20Python/27-%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92.ipynb)
