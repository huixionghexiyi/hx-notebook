# java

1. Linux环境变量配置

```sh
export JAVA_HOME=<java_path>
export PATH=.:$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

2. Windows环境变量配置

```sh
JAVA_HOME: 
<java_path>

CLASSPATH:
.;%JAVA_HOME%\lib\dt.jar;

PATH: 
%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin
```
