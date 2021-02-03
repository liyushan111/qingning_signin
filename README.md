# data_person.json数据和headers.json的获取

1.进入登录网站：https://wxyqfk.zhxy.net/?yxdm=10623#/login

2.F12开发者模式 ——> Network（网络） ——> F5(刷新页面) ——> checkinUser文件 ——> header(标头)

3.输入账号登录

4.按要求将内容输入到 data_person.json 和 header.json文件

![image-20210203210741448][base64](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203210741448.png)

![image-20210203210940247](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203210940247.png)

![image-20210203211127061](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203211127061.png)



# 修改源代码：

1. Id  和 UID 每个人的唯一标识，需要在daka.py文件修改

![image-20210203212751592](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203212751592.png)

2. 获取方法：

   登录后进入体温上报页面，打开开发者模式（F12)![image-20210203212852100](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203212852100.png)

链接：https://wxyqfk.zhxy.net/?yxdm=10623#/temperatureReport



​	   任意修改/填报一次体温找到SaveTem文件，下划可以看到自己的ID和UID修改daka.py



![image-20210203213144168](C:\Users\CHOU\AppData\Roaming\Typora\typora-user-images\image-20210203213144168.png)
