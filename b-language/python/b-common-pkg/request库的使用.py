import requests

'''
常见异常
 requests.ConnectionError 网络连接异常：DNS查询失败、拒绝访问等
 requests.HTTPError HTTP错误
 requests.URLRequired URL缺失
 requests.TooManyRedirects 超过最大重定向次数
 requests.ConnectTimeout 从发送url到返回整个过程的超时异常
 requests.Timeout  与远程服务器连接的超时异常
'''
# 构造一个像服务器请求资源的Request对象给服务器 ，并返回一个Response对象
'''
get(url,param,kwargs)
r = requests.get('https://www.baidu.com')
print(type(r)) # 类型Response
print(r.status_code) # 状态码
print(r.text) # 响应体是文本
print(r.encoding) # 响应头charset指定的字段，默认：ISO-8859-1
print(r.apparent_encoding) # 分析内容中的编码方式
print(r.content) # 响应内容的二进制，比如图片
r.encoding = 'utf-8'
r.raise_for_status() # 检查状态值是不是 200，不是就产生HTTPError异常
print(r.text)

r = requests.head(url) # 获取头部信息
headers = r.headers

requests.request(method,url**kwargs) 
# method :一共有7个 GET|HEAD|POST|PUT|PATCH|delete|OPTIONS
**kwargs:
params:即在url中添加键值对
data: 字典，序列，或文件，作为Request的内容
json: 作为内容
headers: 头字段
cookies: 字段或CookieJar，Request的cookie
auth:元组，支持认证功能
files: 字典类型,传输文件  fs = {'file':open('data.xls','rb')}
timeout: 设定超时时间，秒
proxies: 字典类型，设定访问代理服务器，可以增加登录认证
allow_redirects: bool,默认True，是否允许重定向开关
stream: bool,默认True，获取内容立即下载开关
verify: 默认True ，认值SSL证书开关
cert:本地SSL证书路径
'''

def getHTMLText(url):
    try:
        r = requests.post(url)
        r.raise_for_status() # 判断网络连接状态
        r.encoding = r.apparent_encoding
        return r.headers
    except:
        return '产生异常'

def getHeaders(url):
    try:
        r = requests.head(url) # 获取头部信息
        r.raise_for_status()
        return r.headers
    except:
        return '产生异常'

def postForm(url):
    payload = {'key1':'value1','key2':'value2'} # 如果提交的是一个字典，则会提交到form表单中
    payload1 = 'ABC' # 如果提交的是字符串，则放到data中
    try:
        r = requests.post(url,data = payload)
        return r.text
    except Exception as e:
        return e.args

def putForm(url):
    payload = {'key1':'value1','key2':'value2'} # 如果提交的是一个字典，则会提交到form表单中
    payload1 = 'ABC' # 如果提交的是字符串，则放到data中
    try:
        r = requests.put(url,data = payload) # put和post类似，但是会覆盖原先的内容
        return r.text
    except Exception as e:
        return e.args


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    post_url = 'https://httpbin.org/post'
    print(postForm(url))

# scrapy 库，爬取网站

import re 
str1 = "Python's features" 
str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
print(str2.groups())

print(len(set([1,1,1,1,2,3])))