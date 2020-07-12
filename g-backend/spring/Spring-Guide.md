# `1. IoC（Inversion of Control）控制反转`

在内存中创建好一些常用的对象，注入到需要使用到的地方即可。

在application.xml中配置好Bean所在的位置即可。

## `基本Annotation`

- 修饰`class`：
  - `@Configuration`：修饰`Spring`的配置类，表示这是`Spring的入口`
  - `@ComponentScan`：修饰`Spring`的配置类，表示该配置类扫描当前类所在package及其子package中所有标注`@Component`，并根据`@Autowried`进行装配。
  - `@Component`：修饰`class`，表示这是一个`Bean。`
  - `@Order`：修饰`Bean`
    - 参数`value`为`int`，表示Spring加载`Bean`的顺序。
  - `@Scope`：修饰`Bean`，调整Bean的生命周期。配合`ConfigurableBeanFactory`中的变量使用

  - `@`
- 修饰`field`：
  - `@Autowired`：修饰Bean中的字段，即将修饰的字段注入一个对象。（同时可以修饰参数）
    - 参数`required`为`false`，表示如果找不到该字段的对象就忽略。
- 修饰`method`：
  - `@Bean`：在`Spring`配置类中，修饰方法，返回一个对象，任然为`Singleton`。
    - 参数`value`为`String`表示这个`Bean`名称。
  - `@Qualifier`：不给`Bean`配置`value`参数时，配置该注解的参数也可指定名称。
  - `@Primary`：当有多个同类型的`Bean`的时候，添加该注解的`Bean`作为默认`Bean`（即注入的时候没有选择名称）
  - `@PostConstruct`：修饰的方法会在 在注入字段之后 ，创建一个`Bean`之前调用。
  - `@PreDestory`：在销毁一个`Bean`之前。


## 工厂模式创建Bean（`FactoryBean`）

实现`spring`中接口`FactoryBean`，其中 `getObject`是用来创建真正的Bean的， `getobjectType`可以指定创建的Bean的类型。

## `Resource`类

`class`位置：`org.springframework.core.io.Resource`

可以使用以下两种方式引入一个`Resource`文件：
- ` @Value("classpath:/logo.txt")`
- `@Value("file:/path/to/logo.txt)`

资源通常放到 `src/main/resources`中。

## 注入配置

### 方式一

java开发中的常用配置文件是： `.properties`（key=value形式）结尾的文件。spring提供一种注解来读取配置文件。

将注解`@PropertySource("app.properties")`添加到`@Configuration`配置类上。

```java
@Configuration
@ComponentScan
@PropertySource("app.properties") // 表示读取classpath的app.properties
public class AppConfig {
    @Value("${app.zone:Z}")
    String zoneId;

    @Bean
    ZoneId createZoneId(@Value("${app.zone:Z}") String zoneId) { // 可以写入方法参数中
        return ZoneId.of(zoneId);
    }
}
```
- "${app.zone}"表示读取key为app.zone的value，如果key不存在，启动将报错；
- "${app.zone:Z}"表示读取key为app.zone的value，但如果key不存在，就使用默认值Z。

### 方式二

让一个`JavaBean`持有，再通过 `#{smtp.port:25}`注入。

```java
// 持有配置参数的javabean
@Component
public class SmtpConfig {
    @Value("${smtp.host}")
    private String host;

    @Value("${smtp.port:25}")
    private int port;

    public String getHost() {
        return host;
    }

    public int getPort() {
        return port;
    }
}
// 使用配置参数的javabean
@Component
public class MailService {
    @Value("#{smtpConfig.host}")
    private String smtpHost;

    @Value("#{smtpConfig.port}")
    private int smtpPort;
}
```
## 按照条件装配

根据条件的不同来装配`Bean`

1. Profile

```java
@Configuration
@ComponentScan
public class AppConfig{
  @Bean
  @Profile("!test") // 表示profile不为 test
  ZondId createZondId(){
          return ZoneId.systemDefault();
    }

    @Bean
    @Profile("test") // 表示profile为 test
    ZoneId createZoneIdForTest() {
        return ZoneId.of("America/New_York");
    }
}
```
在运行的时候加上JVM参数 `-Dspring.profiles.active=test`,指定运行环境为`test`

`-Dspring.profiles.active=test,master` 表示test环境，master分支代码
```java
@Bean
@Profile({ "test", "master" }) // 同时满足test和master
ZoneId createZoneId() {
    ...
}
```
2. Conditional

```java
@Component
@Conditional(OnSmtpEnvCondition.class)
public class SmtpMailService implements MailService {
    // TO-DO
}
```
如果满足 `Conditional`才会创建`Bean`。其中`OnSmtpEnvCondition`类的定义如下：

```java
// 如果环境变量中存在smtp值为true，则创建
public class OnSmtpEnvCondition implements Condition {
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        return "true".equalsIgnoreCase(System.getenv("smtp"));
    }
}
```
其他 `Conditional`：
- @ConditionalOnProperty(name="app.smtp",havingValue="true") ：如果配置文件中有 `app.smtp=true`则创建
- @ConditionalOnClass(name="javax.mail.Transport") :如果存在这个类就创建

# `2. AOP（Aspect Oriented Programming）面向切片编程`

## `基本Annotation`

- 修饰 `class`：
  - `@EnableAspectJAutoProxy`: 添加到配置类上，自动配置AOP
  - `@Aspect`: 表示该类是一个用于AOP的类
- 修饰 `method`：
  - `@Before`: 执行拦截代码，再执行目标代码。（若拦截器异常，目标代码就不执行）
  - `After`：先执行目标代码，再执行拦截代码。（无论目标是否异常，拦截代码都会执行）
  - `@AfterReturning`：先执行目标代码，在执行拦截代码。（目标代码正常，拦截代码才会执行）
  - `@AfterThrowing`：先执行目标代码再执行拦截代码。（只有目标代码抛出异常才执行拦截代码）
  - `@Around`: 可以完全按控制目标代码是否执行。再目标代码前后都会执行。（可以说包含了上面所有功能）
  - `@Transactional`: 

## 使用注解


### 方式一：使用execute
`execute`表示织入完成路径的方法
```java
@Aspect
@Component
public class SecurityAspect {
    @Before("execution(public * com.huixiong.service.*.*(..))")
    public void check() {
        if (SecurityContext.getCurrentUser() == null) {
            throw new RuntimeException("check failed");
        }
    }
    @Around("execution(public * com.huixiong.service.)")
}
```
### 方式二： 使用@annotation的方式

`@annotation`表示只织入添加了该注解的方法。
```java
@Aspect
@Component
public class MetricAspect {
    @Around("@annotation(metricTime)")
    public Object metric(ProceedingJoinPoint joinPoint, MetricTime metricTime) throws Throwable {
        String name = metricTime.value();
        long start = System.currentTimeMillis();
        try {
            return joinPoint.proceed();
        } finally {
            long t = System.currentTimeMillis() - start;
            // 写入日志或发送至JMX:
            System.err.println("[Metrics] " + name + ": " + t + "ms");
        }
    }
}
```
## 原理与坑

Spring是通过`CGLIB`实现代理类。通过创建被代理类的子类，重写所有没有 `final`的方法。并且不会初始化继承的字段。还是不太清楚。需要抽时间重新看一遍2020年7月9日


# `Spring操作数据库`

基本上的第三方库都实现了 `jdbc`标准接口。所以有统一的标准访问数据库。一般有一下几步：

- 创建全局链接池 `DataSource`,表示连接池。
- 从DataSource