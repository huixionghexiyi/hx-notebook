# 入门
雅虎内部很多大型系统基本都需要依赖一个类似的系统进行分布式协调。但是这些系统往往存在分布式单点问题。

解决办法：开发一个通用的无单点问题的分布式协调框架，一遍开发人员将尽力集中在处理业务逻辑上。

设计的目标是将复杂且容易出错的分布式一致性服务封装起来，购成一个搞笑可靠的原语集，并以一系列简单以用的接口提供给用户使用。

是一个典型的分布式一致性解决方案，分布式应用程序可以基于Zookeeper是实现数据发布/订阅、负载均衡、命名服务、分布式协调/通知、集群管理Master选举、分布式锁和分布式队列等功能。

最常用的功能是担任服务生产者和消费者的`注册中心`(提供发布订阅服务)。服务生产者将自己提供的服务注册到zookeeper中心，服务的消费者在进行服务调用的时候先到zookeeper中查找服务，获取生产者的详细信息后，再去调用服务生产者的内容和数据。

### 为什么使用奇数台服务器？
zookeeper容错是指，如果宕掉n个zookeeper服务器知否，剩下的个数必须大于宕掉的个数的话整个zookeeper才依然可用。所以容错相同，奇数台才是合理的。

###　重要概念
1. 本身就是一个分布式程序，只要半数以上存活，就能正常服务
2. 为了保证高可用，最好以集群形态部署zookeeper，那么只要集群中大部分机器可用，zookeeper就仍然可用。
3. zookeeper将数据保存在内存中，这也保证了高吞吐和低延迟。(但内存限制了能够存储的容量不太大，此限制也保持znode中存储的数据量较小的进一步原因)。
4. 高性能的，在读多于写的应用程序中尤其高性能，因为写会导致所有的服务器间同步状态。(读多于写是协调服务的典型场景)
5. 底层其实值提供两个功能：1.管理(存储、读取)用户程序提交的数据。2.为用户程序提供数据节点监听服务。 

### 其他重要概念
包括：Session、Znode、版本、Watcher、ACL

1. 会话
session指的是zookeeper服务器与客户端会话。首先，客户端会和服务器建立一个TCP长连接，从第一次连接建立开始，会话的生命周期就开始了。客户端通过心跳检测与服务保持出有效的会话，也能够像zookeeper服务发送请求并接收响应，同时还能够通过该链接接收来自服务器的watch事件通知。

session的`sessionTimeout`值用来设置一个客户端会话超时时间。当由于各种原因(服务器压力过大、网络故障、客户端主动断开连接等)导致客户端与服务器断开连接时，只要在`sessionTimeout`规定的时间内连接到集群中的任意一台服务器，那么之前的连接依然有效。

2. Znode

通常，在谈到分布式的时候节点指的是集群中的每一台机器。在zookeeper中，节点分为机器节点和数据节点，数据节点称为znode。

而znode可以分为持久节点和临时节点两类。`持久节点`：一旦被创建除非主动移除，否则一直保存在zookeeper上。`临时节点`：生命周期和会话绑定在一起。会话一旦失效，所有的临时节点都会移除。

另外，zookeeper允许用户为每个数据节点增加一个特殊属性`SEQUENTIAL`，一旦节点被标记这个属性，那么在节点被创建的时候zookeeper会自动在节点声明后增加一个整数，这个整数是一个由父节点维护的自增数字。

3. 版本

我们知道Znode作为数据节点，会在内存中存储数据。对于每个节点zookeeper会维护一个叫做Stat的数据结构，Stat记录znode的三个版本，分别是`version(当前znode版本)`、`cversion(当前znode子节点版本)`、`aversion(当前znode的ACL版本)`。

4. Watcher
事件监听，zookeeper中一个很重要的特性。zookeeper允许用户指定节点注册一些Watcher，并且在一些特定事件触发的时候，zookeeper服务端会将事件通知到感兴趣的客户端上去，该机制是zookeeper实现分布式协调服务的重要特性。

5. ACL
采用ACL(AccessControlLists)策略来进行权限控制，类似于UNIX文件系统的权限控制。Zookeeper定义了如下5种权限：
- create:创建子节点的权限
- read:获取节点数据和子节点列表的权限
- write:更新节点数据的权限
- delete:删除子节点的权限
- admin:设置节点ACL的权限

### 特点
- **顺序一致性**：从同意客户端发起的事务请求，最终会严格地按照顺序被应用到zookeeper中去。
- **原子性**:所有事务请求的处理结果在整个集群中所有机器上的应用情况是一致的，也就是说，要么整个集群的机器中所有的机器都成功应用了某一事务，要么都没有应用。
- **单一系统映像**：无论客户端连到哪一个zookeeper服务器上，其看到的服务端数据模型都是一致的。
- **可靠性**：一旦一次更改请求被应用，更改的结果就会被持久化，直到下一次更改覆盖。

### 设计目标
1. 简单的数据模型
2. 可构建集群
3. 顺序访问
4. 高性能

### 集群角色介绍
Leader:主节点，负责协调和写
Follower：从节点，负责读和选举新Leader，同步数据
Slave：负责读操作，同步数据

### zookeeper &ZAB协议&Paxos算法

1. 协议&Paxos算法
2. ZAB协议介绍
3. ZAB协议两种基本的模式：崩溃恢复和消息广播

### 数据模型

znode是zookeeper上最小的数据单元，每个znode上都可以存储数据，并且可以拥有自己的子节点。节点存储的方式类似于Linux的文件系统，最大节点是`/`。
事务ID，每一个事务请求都有会分配一个事务ID，用`zxid`表示，通常是一个64位的数字，每一个zxid对应一个操作。

每个znode有两部分组成：
- stat 状态信息，包含所有数据节点的状态信息
- data 数据内容

