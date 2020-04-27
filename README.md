#### scrapy批量下载seaborn案例文件/分门别类/自定义文件夹+原文件名
##### 1，seaboen是matplotlib的"改良版"，常用于数据分析中的可视化报告，图表的案例文件有很多，下载后的文件，必须分门别类以利区分和归纳，比如用来绘制柱状图(barplot)有哪些源码文件，绘制箱线图(boxplot)有哪些文件，密度图案例(distplot)的源文件等，最终下载回来的是完整的案例，以及所有案例对应的源文件，并以案例名称作为文件夹的名称，以下是此项目执行后的结果图:
![img1](https://github.com/ziliang-wang/seaborn/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427145919.png)
##### 2，关键代码，在pipelines.py自定义1个继承自FilesPipeline的类，并改写3个方法:
![img2](https://github.com/ziliang-wang/seaborn/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427151120.png)
###### a，在get_media_requests()的实例方法里，分别取出文件来源的url并逐一发出请求，并透过负责传输的meta参数来传递用来构造文件名的title字段
###### b，item_completed()是下载完成后的处理函数，参数results是一个嵌套2元元组的列表结构，即嵌套元组的列表，元组内的第一个元素表示下载成功或失败，第二个元素为文件的路径信息，若某一项下载失败，抛出异常并删除该项，同时显示"No such file"，即raise DropItem('No such file')
###### c，file_path()方法，用来组合文件夹与文件名的结构，透过/符号来区分文件夹与文件
##### 3，settings.py中的配置
![img3](https://github.com/ziliang-wang/seaborn/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200427153608.png)
