# Http

浏览器和服务器通信需要经历如下步骤：

1. 建立TCP链接
2. 发送Http请求（request）
3. 接受http响应（reponse）
4. 渲染响应中的内容



本质上`request`和`response`都是一个字符串，每一行通过`\r\n`分割，如何处理都交给浏览器和服务器。当然这个字符串是有一定给则的。

## 请求（`request`）

```java
GET / HTTP/1.1
Host: www.sina.com.cn
User-Agent: Mozilla/5.0 
Accept: */*
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8
```

真实传递过来的是一个 `GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nUser-Agent: Mozilla/5.0 \r\nAccept: */*\r\nAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8\r\n\r\n`这样的字符串，末尾连续2个 `\r\表示结束请求头。

`GET`请求是没有请求体的，`POST`请求有：

```
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

username=hello&password=123456
```

当然`POST`可以是任意格式的编码，只需要在`Content-Type`中指定就好了（由于请求头结束是 `\r\n\r\n`，所以会多一个空行）：

```
POST /login HTTP/1.1
Content-Type: application/json
Content-Length: 38

{"username":"bob","password":"123456"}
```



## 响应（response）

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 21932
Content-Encoding: gzip
Cache-Control: max-age=300

<html>
    ...
</html>

响应就是一个响应头和响应体。

`request header`和`resonse header中包含了许多信息，浏览器和服务器都会解析这些东西。当然第一行并不是`request header`或`resonse header`。而是请求的状态。状态有很多，头也有很多。

## 请求状态

在整个`request`中，第一行是请求的状态，而状态通过空格分隔为三个数据 `请求的方式 资源的路径 HTTP版本`

请求方式有：`GET`、`POST`、`UPDATE`、`DELETE`

资源的路由：`/`表示项目的根路由

HTTP版本：`HTTP/1.0`、`HTTP/1.1`(通常都是这个)

## 响应状态

在整个`response`中，第一行是响应的状态，也是通过空格分隔三个数据：`HTTP版本 状态码 响应说明`

HTTP版本和请求的版本一样

状态码：`1xx`、`2xx`、`3xx`、`4xx`、`5xx`

响应说明：略，有空补充，2020年6月14日

## 请求头（request header）

有空补充，2020年6月14日

## 响应头（response header）

有空补充，2020年6月14日

