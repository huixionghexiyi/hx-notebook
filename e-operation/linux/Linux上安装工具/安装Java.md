1. 可以使用:`yum install jdk`下载openjdk
2. 自己下载然后上传。
 
在网上有推荐使用`wget`下载链接中的jdk，但是，我们知道在官网下载的时候会要点击一个`i accept`,而下载成功后会出问题，就是没有同意协议。而网上也提供了很多解决方法。试过几个，没有成功，所以自己下载再上传就很好了，或者使用openjdk也基本没有问题。

1. 官网下载jdk。
2. 解压`tar -zxvf jdk*.tar.gz`
3. 将jdk解压后的文件夹放到需要的路径下，或者就在`home`下解压也可以。
4. 配置环境变量

```sh
export  JAVA_HOME=/usr/java/latest/jdk1.8.0_221
export  JRE_HOME=$JAVA_HOME/jre
export  CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export  PATH=$JAVA_HOME/bin:$PATH
```

5. 最后`source /etc/profile`让环境变量生效