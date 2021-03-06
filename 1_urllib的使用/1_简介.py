"""
爬虫: 网络蜘蛛, 就是从互联网上去拿取数据. 通过URL, 去获取我们想要的资源.
作用: 获取数据. 收集信息.
获取数据的途径:
    从网上买数据库.
    通过爬虫, 自己从网上获取.
合法性:
    灰色, 但信息是完全公开的, 是合法的.

反爬虫:
    爬虫 V/S 反爬虫
    合法检测: 请求校验(useragent, referer, 接口+签名, 等等)
    小黑屋: IP/用户限制请求频率或者直接拦截.
    投毒: 不拦截, 而是返回虚假数据, 进行误导
    ...
选择一门语言:
    爬虫可以使用各种语言去写, 例如c++, java, python
    选择python是因为包, 库, 框架非常完全. 非常方便, 利于爬虫开发

基本流程:
    目标数据
    来源地址
    结构分析
    构思
    编码

    基本手段:
        破解请求限制
            请求头设置
            控制请求频率
            IP代理
            签名/加密参数, 从html/cookie/js分析.
        破解登录授权:
            请求时带上用户cookie信息
        破解验证码:
            简单的验证码可以使用试图读取验证码第三方库
        解析数据:
            HTML, DOM解析:
                正则匹配,
                使用第三方库解析HTML DOM, 类似jquery库
        数据字符串:
            正则匹配
            JSON/XML对象进行解析
    python爬虫:
    涉及的模块包:
        请求: urlib, requests
        多线程: threading
        正则: re
        json解析: json, jsonpath
        html dom解析: beautiful soup
        lxml: xpath
        操作浏览器: selenium


"""









