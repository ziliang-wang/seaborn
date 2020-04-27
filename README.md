#### scrapy批量下载seaborn案例文件/分门别类/自定义文件夹+原文件名
##### seaboen是matplotlib的"改良版"，常用于数据分析中的可视化报告，图表的案例文件有很多，下载后的文件，必须分门别类以利区分和归纳，比如用来绘制柱状图(barplot)有哪些源码文件，绘制箱线图(boxplot)有哪些文件，密度图案例(distplot)的源文件等，最终下载回来的是完整的案例，以及所有案例对应的源文件，并以案例名称作为文件夹的名称，以下是此项目执行后的结果图:
![img1](https://github.com/ziliang-wang/seaborn/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427145919.png)
##### 1，关键代码,在pipelines.py自定义1个继承自FilesPipeline的类，并改写3个方法:
![img2](https://github.com/ziliang-wang/seaborn/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427151120.png)
###### a，
###### b，
