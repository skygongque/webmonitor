# webmonitor
用于判断某挂号网站是否有剩余的号，如果有发邮件通知

    #备注：邮箱提醒需要用到stmp服务，填写账号和授权码

# how to use
运行环境：
1.windows 7，python3.7 ,pip3

2.把python3和pip3配置在环境变量中

3.出现model未定义的错误是可用'pip3'安装相应的库，比如安装requests和bs4的代码如下。

    pip3 install requests bs4
    
## 2019.1.21版本
1.每隔一段时间请求网站服务器，把符合要求的项目（属性值为kyy即可预约的信息写入text），不符合的项目只在屏幕打印输出
2.新版本文件名为guahao_spider.py，还未加入发送邮件通知（有需要的可以自己加很简单的）
