# qingning_signin

# Fork 到自己的仓库后完成下面的步骤（主要是完善自己的信息）然后点击 Star 就ok了

每日体温打卡


# 图文结合请查看readme.pdf

# data_person.json数据和headers.json的获取

1.进入登录网站：https://wxyqfk.zhxy.net/?yxdm=10623#/login

2.F12开发者模式 ——> Network（网络） ——> F5(刷新页面) ——> checkinUser文件 ——> header(标头)

3.输入账号登录

4.按要求将内容输入到 data_person.json 和 header.json文件

![image-20210203210741448](images\image-20210203210741448.png)

![image-20210203210940247](images\image-20210203210940247.png)

![image-20210203211127061](images\image-20210203211127061.png)



# 修改源代码：

1. Id  和 UID 每个人的唯一标识，需要在daka.py文件修改

![image-20210203212751592](images\image-20210203212751592.png)

2. 获取方法：

   登录后进入体温上报页面，打开开发者模式（F12)![image-20210203212852100](images\image-20210203212852100.png)

链接：https://wxyqfk.zhxy.net/?yxdm=10623#/temperatureReport



​	   任意修改/填报一次体温找到SaveTem文件，下划可以看到自己的ID和UID修改daka.py



![image-20210203213144168](images\image-20210203213144168.png)





# 如果你了解sever酱：

链接：http://sc.ftqq.com/



尝试着在**print语句**下，加入代码自动推送微信消息，提醒你是否打卡成功

只需要加一行像这样的代码：

```python
import requests
url="https://sc.ftqq.com/XXXXXXX.send?text=主人服务器又挂掉啦~"
# xxxx是你sever酱的秘钥，官网有说明
requests.post(url)

```



![image-20210203222611812](images\image-20210203222611812.png)
