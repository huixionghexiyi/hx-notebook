监控的节点相当于某个文件夹

根据`README.md`和`安装.md`文档了解配置文件和大致的目录结构。



## 单实例
>单实例配置，不需要和其他zookeeper服务器通信，所以不需要有`initLimit`、`syncLimit`、`Service.x`参数。

1. 编写`conf/zoo.cfg`：
```shell
tickTime=2000
dataDir=/var/lib/zookeeper/zk1/data
# 如果没有下面字段则日志也放到data下
dataLogDir=/var/lib/zookeeper/zk1/log
clientPort=2181
```
2. 启动`zookeeper`服务：
这个文件的名字可以任意，但是默认是使用的zoo.cfg。启动服务命令如下：
```shell
# 下面两个命令等价
./bin/zkServer.sh start
./bin/zkServer.sh start ./conf/zook.cfg
# 其他配置文件开启服务命令
./bin/zkServer.sh start ./conf/zook1.cfg
```
3. 客户端连接服务`zookeeper`服务：
因为是单实例，所以客户端就是连接本地。
```shell
# 默认端口就是2181，下面两命令等价
./bin/zkCli.sh -server
./bin/zkCli.sh -server 127.0.0.1:2181
```
连接之后，会出现：
```shell
# 类似于命令行
[zk: localhost:2181(CONNECTED) 0] 
```
客户端和服务端就建立了可操作连接，后面的操作就是当前客户端和服务端的设置了，和单实例多实例没有关系。

- [常用命令](#常用命令)


### 多实例

1. conf/zoo.cfg参数配置:
```shell
tickTime=2000
dataDir=/var/lib/zookeeper/zk1/data
# 如果没有下面字段则日志也放到data下
dataLogDir=/var/lib/zookeeper/zk1/log
clientPort=2181
# 多实例中必须配置这两个参数
initLimit=5
syncLimit=2
# 配置其他的zookeeper服务器
server.1=zoo1:2888:3888
server.2=zoo2:2888:3888
server.3=zoo3:2888:3888
```
2. 启动`zookeeper`服务：
>同单实例
3. 客户端连接服务`zookeeper`服务：
>同单实例

---

#### 常用命令：
[参考文章](https://www.cnblogs.com/leeSmall/p/9563547.html)
```shell
# 在zookeeper命令行中输入
# 查看帮助
help
# 展示所有节点
ls /
# 创建节点:-e 临时节点、-s 顺序节点、不带-s -e 默认是持久节点。
create /zk_test_node
# 查看节点数据
get /zk_test_node
# 设置节点参数
set /zk_test_node junk
# 删除节点
delete /zk_test_node
```

#### 节点参数：
- cZxid = #创建节点时zk内部自己分配的id
- Ctime = #创建节点的时间
- mZxid = #修改的id
- mtime = 修改的时间
- pZxid = 子节点最后一次被修改的id
- cVersion = 0  #拥有的子节点被改的话，该值随着改变
- dataVersion = 0 #数据版本
- aclVersion = 0 # 访问控制权限的版本
- ephemeralOwner = 0X0 #临时节点还是持久节点 临时节点值不为0（值为当前会话id），持久节点值永远为0
- dataLength = 3 #数据长度
- numChildren = 0 #子节点个数
