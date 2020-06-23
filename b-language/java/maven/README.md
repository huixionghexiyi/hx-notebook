# Maven
> maven是java的包管理工具，不像python一样，再安装python的时候就会自动安装 `pip`。所以需要手动下载maven。并且Maven不只是包管理工具，还是编译、打包、发布等功能。

##  安装

- 下载：http://maven.apache.org/download.cgi

- 配置环境变量：

windows： 在`Path`中添加：`<path>/maven-3.6-x/bin`

## 基础结构

一个`maven`项目的目录结构是这样的：



```java
a-maven-project
├── pom.xml // 配置文件
├── src
│   ├── main
│   │   ├── java //源码
│   │   └── resources // 资源文件
│   └── test
│       ├── java //测试源码
│       └── resources //测试资源
└── target // 用于存放打包的文件
```


通过一个配置文件`pom.xml`管理包,结构如下：


```xml
<!-- 这个标签可以省略，表示xml的版本和编码格式 -->
<?xml version="1.0" encoding="UTF-8"?> 
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>MavenDemo</groupId>
  <artifactId>MavenDemo</artifactId>
  <version>1.0-SNAPSHOT</version>

  <name>MavenDemo</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    ...
  </build>
</project>
```

主要包含几块内容：

- `guruoId`、`artifactId`、`version`：当前`maven`项目的描述信息，以及其他描述信息
- `properties`：当前`maven`项目的属性，如编码方式，源码的位置，编译后的.class文件的位置
- `dependencies`：依赖的包，在这里面添加
- `build`：构建使用到的插件

其中 `scope`有四种：`compile`、`test`、`runtime`、`provided`，后面有空再补充这些的含义2020年6月12日。

## 构建流程

Maven有两种类型的生命周期（Lifecycle） `default`和`clean`，前者是编译打包发布的功能，后者是清除之前编译的包。

**`defaul`有以下阶段（Phase）：**

- validate
- initialize
- generate-sources
- process-sources
- generate-resources
- process-resources
- compile
- process-classes
- generate-test-sources
- process-test-sources
- generate-test-resources
- process-test-resources
- test-compile
- process-test-classes
- test
- prepare-package
- package
- pre-integration-test
- integration-test
- post-integration-test
- verify
- install
- deploy

如果运行 `mvn package`则从 `validate`阶段运行到 `package`阶段。

**`clean`有以下阶段：**

- pre-clean
- clean （注意这个clean不是lifecycle而是phase）
- post-clean

这个生命周期通常执行 `mvn clean`清空所有class和jar文件。



如果执行 `nvm clean compile`，则表示先清空，在执行 `default`生命周期，知道 `compile`阶段。



除了生命周期（Lifecycle）和阶段（Phase），还有目标（Goal）。

Goal是在阶段中触发的一个或多个操作。

`compile`阶段会执行 `compiler:compile`；`test`阶段会执行 `compiler:testCompile`和 `surefire:test`。



常用的构建指令有：

- mvn clean
- mvn clean compile
- mvn clean test
- mvn clean package

## 插件

前面提到 `lifecycle`、`phase`、`goal`。这三者的关系类似于 `package`、`class`、`method`的关系。

而在执行`mvn compile`的时候，`maven`只是通过这个命令调用`compiler`插件，插件来执行其中的`goal`，每一个`phase`都对应一个插件。如果标准的插件不能满足，那么可以自定义。

自定义插件需包含在`pom.xml`文件中的`<build></build>`标签里：

```xml
<project>
    ...
	<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-shade-plugin</artifactId>
                <version>3.2.1</version>
				<executions>
					<execution>
						<phase>package</phase>
						<goals>
							<goal>shade</goal>
						</goals>
						<configuration>
                            ...
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
</project>
```

其中`comfiguration`中包含的Java程序的入口：

```xml
<configuration>
    <transformers>
        <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
            <mainClass>com.itranswarp.learnjava.Main</mainClass>
        </transformer>
    </transformers>
</configuration>
```

## 模块化管理

前面已经了解了`pom.xml`文件中的标签的具体用法。现在来讲一下，如何使用`maven`来多人开发一个大项目。

当然，如果仅仅靠前面的`pom.xml`中的标签是没法实现模块化的。接下来，我们会引入一些新的标签：

- `modules`：这里面的子标签`module`会被依次编译
- `parent`：继承一个`pom.xml`文件

**案例：**

我们有如下一个项目：

```java
single-project
├── pom.xml
└── src
```

项目太大，很难多个人协同开发。因为人们可能同时修改一个文件，而互相不知道。我们可以将其拆分为三个部分，三个人，一个人负责一个模块的内容，别去懂别人模块的内容就好了。

```
mutiple-project
├── pom.xml
├── module-a
│   ├── pom.xml
│   └── src
├── module-b
│   ├── pom.xml
│   └── src
└── module-c
    ├── pom.xml
    └── src
```

当然，比如各个模块都需要有测试依赖，以`maven`项目的`properties`标签相同。所以，为了简化每个模块的配置文件，将共同的统一抽离出来，于是项目结构编程如下：

```
multiple-project
├── pom.xml
├── parent
│   └── pom.xml
├── module-a
│   ├── pom.xml
│   └── src
├── module-b
│   ├── pom.xml
│   └── src
└── module-c
    ├── pom.xml
    └── src
```

其中`parent`项目中，只有一个`pom.xml`文件，只是为了写共同的配置。

`parent/pom.xml`:

```java
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itranswarp.learnjava</groupId>
    <artifactId>parent</artifactId>
    <version>1.0</version>
    <packaging>pom</packaging>

    <name>parent</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <java.version>11</java.version>
    </properties>

    <dependencies>
	...
    </dependencies>
</project>
```

注意，这里的 `packaging`标签中的值是`pom`，因为不包含任意的java代码。

`module-a/pom.xml`:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.itranswarp.learnjava</groupId>
        <artifactId>parent</artifactId>
        <version>1.0</version>
        <relativePath>../parent/pom.xml</relativePath>
    </parent>

    <artifactId>module-a</artifactId>
    <packaging>jar</packaging>
    <name>module-a</name>
</project>
```

这里通过`relativePath`标签指定要继承的pom的路径。并且重写了`artifactId`、`packaging`、`name`。

如果`module-b`依赖`module-a`则可以这样写：

`module-b/pom.xml`:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.itranswarp.learnjava</groupId>
        <artifactId>parent</artifactId>
        <version>1.0</version>
        <relativePath>../parent/pom.xml</relativePath>
    </parent>

    <artifactId>module-b</artifactId>
    <packaging>jar</packaging>
    <name>module-b</name>
    <dependencies>
        <dependency>
            <groupId>com.itranswarp.learnjava</groupId>
            <artifactId>module-b</artifactId>
            <version>1.0</version>
        </dependency>
    </dependencies>
</project>
```

`./pom.xml`:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itranswarp.learnjava</groupId>
    <artifactId>build</artifactId>
    <version>1.0</version>
    <packaging>pom</packaging>
    <name>build</name>

    <modules>
        <module>parent</module>
        <module>module-a</module>
        <module>module-b</module>
        <module>module-c</module>
    </modules>
</project>
```

## mvnw

**mvnw(Maven Wrapper)**，这相当于一个虚拟的`maven`环境。一些项目是需要固定版本的`maven`环境的。

```powershell
# 安装mvn wrapper
mvn -N io.takari:maven:0.7.6:wrapper
# 创建mvn环境
mvn -N io.takari:maven:0.7.6:wrapper -Dmaven=3.6.3
```

其中 `0.7.6`是`mvnw`的版本，`3.3.3`是指定的`maven`的安装版本。

安装后，会在目录中生成对应的文件：

```java
my-project
├── .mvn
│   └── wrapper
│       ├── MavenWrapperDownloader.java
│       ├── maven-wrapper.jar
│       └── maven-wrapper.properties
├── mvnw
├── mvnw.cmd
├── pom.xml
└── src
    ├── main
    │   ├── java
    │   └── resources
    └── test
        ├── java
        └── resources
```

## 发布自己的`artifact`

略...