# `1. IoC（Inversion of Control）控制反转`

在内存中创建好一些常用的对象，注入到需要使用到的地方即可。

在application.yml中配置好Bean所在的位置即可。

## `1.1 基本Annotation`

- 修饰`class`：
  - `@Configuration`：修饰`Spring`的配置类，表示这是`Spring的入口`
  - `@ComponentScan`：修饰`Spring`的配置类，表示该配置类扫描当前类所在package及其子package中所有标注`@Component`，并根据`@Autowried`进行装配。
  - `@Component`：修饰`class`，表示这是一个`Bean。`
  - `@Order`：修饰`Bean`
    - 参数`value`为`int`，表示Spring加载`Bean`的顺序。
  - `@Scope`：修饰`Bean`，调整Bean的生命周期。配合`ConfigurableBeanFactory`中的变量使用

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


## 1.3 工厂模式创建Bean（`FactoryBean`）

实现`spring`中接口`FactoryBean`，其中 `getObject`是用来创建真正的Bean的， `getobjectType`可以指定创建的Bean的类型。

## `1.4 Resource类`

`class`位置：`org.springframework.core.io.Resource`

可以使用以下两种方式引入一个`Resource`文件：
- ` @Value("classpath:/logo.txt")`
- `@Value("file:/path/to/logo.txt)`

资源通常放到 `src/main/resources`中。

## `1.5 注入配置`

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
## `1.3 按照条件装配`

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

## `2.1 基本Annotation`

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

## `2.2 使用注解`


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
## `2.3 原理与坑`

Spring是通过`CGLIB`实现代理类。通过创建被代理类的子类，重写所有没有 `final`的方法。并且不会初始化继承的字段。还是不太清楚。需要抽时间重新看一遍2020年7月9日


# `3. Spring操作数据库`

基本上的第三方库都实现了 `jdbc`标准接口。所以有统一的标准访问数据库。一般有一下几步：

- 创建全局连接池 `DataSource`,表示连接池。
- 从`DataSource`创建 `Connection`实例
- 通过Connection实力创建PreparedStatement实例
- 执行SQL，若是查询，则通过ResultSet读取结果集，修改则获得int结果

其中我们需要使用 `try...finally`释放资源，涉及到十五的代码需要正确提价或回滚事务。

## `3.1 CURD操作`

除了spring基础包以外，还需要用到一下几个包：
1. 连接池：`HikariCP`
2. 数据库：`mysql-connector-java 8.0.16`
3. JDBC的实现：`spring-jdbc`

对于spring-jdbc中主要使用 `JdbcTemplate`来实现`curd`操作，常用方法有：

```java
int jdbcTemplate.update()

T jdbcTemplate.execute(ConnectionCallback<T> action)

T jdbcTemplate.execute(String sql, PreparedStatementCallback<T> action)

T jdbcTemplate.queryForObject(String sql, Object[] args, RowMapper<T> rowMapper)

T jdbcTemplate.query()
```

## `3.2 操作事务`

在Config中添加注解 `EnableTransactionManagement`，在需要事务的方法上添加 `Transactional`（当然这个方法所在的对象需要通过spring管理的）

### `默认情况`

，当抛出 `RuntimeExcetion`时，Spring的声明式事务就会自动回滚，所以在执行中判断程序需要回滚时，只需要抛出 `RuntimeException`。

```java
@Transactional
public buyProducts(Integer id){
    ...
    if(store < num){
        throw new IllegalArgumentExcetion("No enough products.");
    }
    ...
}
```

### `针对其他额外异常回滚事务`

```java
// 添加异常的类对象作为参数
@Transactional(rollbackFor = {RuntimeException.class, IOException.class})
public buyProducts(long productId, int num) throws IOException {
    ...
}
```
> 建议：如果项目中有自定义的一套一场体系，则从 RuntimeException
中派生，这样就不用给`Transactional`添加参数了

## `3.3 事务传播`

> 

现在有个需求：在注册的时候，注册用户可以获得100积分，那么方法大致如下：

```java
@Component
public class UserService {
    @Autowired
    BonusService bonusService;

    @Transactional
    public User register(String email, String password, String name) {
        // 插入用户记录:
        User user = jdbcTemplate.insert("...");
        // 增加100积分:
        bonusService.addBonus(user.id, 100);
    }
}
```
现在增加积分的时候抛出异常需要回滚。是回滚 `addBonus`呢，还是`register`一起回滚呢。

通常，我们希望联通register一同回滚，这里就要涉及到事务的集中传播级别：`REQUIRED`是默认传播级别：**如果当前没有事务，则创建一个事务；若有，则加入到当前事务中。**


在`UserService.register`在被调用的，如果UserService.register有 `Transactional`的话，就会判断当前是不是存在事务，如果没有就会创建一个事务。于是 `register`就会在事务中执行。而执行到 `BonusServer.addBonus`的时候，会发现当前已经存在事务了。于是加入到当前事务中，相当于将如下两个SQL放到一个事务中执行：

```SQL
INSERT INTO users ...
INSERT INTO bonus ...
```
事务传播级别一共有以下几种类型：
1. `SUPPORTS`：表示如果有事务，就加入到当前事务，如果没有，那也不开启事务执行。这种传播级别可用于查询方法，因为SELECT语句既可以在事务内执行，也可以不需要事务；

2. `MANDATORY`：表示必须要存在当前事务并加入执行，否则将抛出异常。这种传播级别可用于核心更新逻辑，比如用户余额变更，它总是被其他事务方法调用，不能直接由非事务方法调用；

3. `REQUIRES_NEW`：表示不管当前有没有事务，都必须开启一个新的事务执行。如果当前已经有事务，那么当前事务会挂起，等新事务完成后，再恢复执行；

4. `NOT_SUPPORTED`：表示不支持事务，如果当前有事务，那么当前事务会挂起，等这个方法执行完成后，再恢复执行；

5. `NEVER`：和NOT_SUPPORTED相比，它不但不支持事务，而且在监测到当前有事务时，会抛出异常拒绝执行；

6. `NESTED`：表示如果当前有事务，则开启一个嵌套级别事务，如果当前没有事务，则开启一个新事务。

> 如果想自定义事务，则在Transactional声明：`@Transactional(propagation = Propagation.REQUIRES_NEW)`。
> 
> 实际上，Spring将connection实例和TransactionStatus实例绑定到ThreadLocal（当前线程）中，如果spring在当前线程中没有从ThreadLocal中获取到事务，就会重新创建一个Connection连接，同时开启一个事务。所以只有同一线程中才能实现事务传播。

# `4. DAO（Data Access Object）层的编写`

# `5. ORM框架`

## `5.1 Hibernate`
## `5.2 MyBatis`

# `6. Spring MVC使用`

Spring自带的一个 `MVC`框架，通过Spring IoC提供的bean，完成业务逻辑，并且通过 `ModleAndView`对象渲染模板。

需要的依赖包括：

- org.springframework:spring-context:5.2.0.RELEASE ：Spring核心依赖
- org.springframework:spring-webmvc:5.2.0.RELEASE  ：Spring MVC依赖
- org.springframework:spring-jdbc:5.2.0.RELEASE    ：Spring连接Jdbc依赖
- javax.annotation:javax.annotation-api:1.3.2    ： Spring注解依赖
- io.pebbletemplates:pebble-spring5:3.1.2  ：Springmvc需要的渲染模板依赖
- ch.qos.logback:logback-core:1.2.3   ： 日志需要依赖
- ch.qos.logback:logback-classic:1.2.3 ：日志需要的依赖
- com.zaxxer:HikariCP:3.4.2   : 数据库连接池
- mysql:mysql-connection-jdbc:8.0.16  : mysql与java连接的jdbc依赖
- org.apache.tomcat.embed:tomcat-embed-core:9.0.26  ：tomcat相关服务依赖
- org.apache.tomcat.embed:tomcat-embed-jasper:9.0.26  ： tomcat相关服务依赖

```tree
src
├─main
│  ├─java
│  │  └─com
│  │      └─huixiong
│  │          │  AppConfig.java
│  │          │  DatabaseInitializer.java
│  │          │
│  │          ├─entity
│  │          │      User.java
│  │          │
│  │          ├─service
│  │          │      UserService.java
│  │          │
│  │          └─web
│  │                  UserController.java
│  │
│  ├─resources
│  │      jdbc.properties
│  │      logback.xml
│  │
│  └─webapp
│      ├─static
│      │  ├─css
│      │  │      bootstrap.css
│      │  │
│      │  └─js
│      │          jquery.js
│      │
│      └─WEB-INF
│          │  web.xml
│          │
│          └─templates
│                  base.html
│                  index.html
│                  profile.html
│                  register.html
│                  signin.html
│
└─test
    └─java
```

在 AppConfig中需要通过tomcat对象创建一个服务，并且还需要生成两个必要的bean，用于处理静态文件和渲染模板：

```java
@EnableWebMvc
public class AppConfig{


    public static void main(String[] args){
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(Integer.getInteger("port",8080));
        tomcat.getConnector();
        Context context = tomcat.addWebapp("",new File("src/main/webapp").getAbsolutePath());
        WebResourceRoot resources = new StandardRoot(context);
        resources.addPreResources(new DirResourceSet(resources,"/WEB-INF/classes",new File("target/classes").getAbsolutePath(),"/"));
        context.setResources(resources);
        tomcat.start();
        tomcat.getServer().await();
    }

        /**
     * 该bean并不是必须的，这里创建默认的WebMvcConfigurer，覆写addResourceHandlers
     * 为了让Spring Mvc 自动处理静态文件，并映射/static/**
     *
     * @return
     */
    @Bean
    WebMvcConfigurer createWebMvcConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addResourceHandlers(ResourceHandlerRegistry registry) {
                registry.addResourceHandler("/static/**").addResourceLocations("/static/");
            }
        };
    }

    /**
     * viewResolver 通过prefix和suffix来查找view
     * 该方法使用了pebble引擎来渲染模板，指定模板文件存放在/WEB-INF/templates/路径下
     * @param servletContext
     * @return
     */
    @Bean
    ViewResolver createViewResolver(@Autowired ServletContext servletContext) {
        PebbleEngine engine = new PebbleEngine.Builder().autoEscaping(true)
                .cacheActive(false)
                .loader(new ServletLoader(servletContext))
                .extension(new SpringExtension())
                .build();
        PebbleViewResolver viewResolver = new PebbleViewResolver();
        viewResolver.setPrefix("/WEB-INF/templates/");
        viewResolver.setSuffix("");
        viewResolver.setPebbleEngine(engine);
        return viewResolver;
    }
}

```
> 配置web.xml:
```xml
<!DOCTYPE web-app PUBLIC
        "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
        "http://java.sun.com/dtd/web-app_2_3.dtd" >
<!--
该配置会初始化参数contextClass
指定使用注解配置的 AnnotationConfigWebApplicationContext，
配置文件的位置参数 contextConfigLocation指向AppConfig的完整类名，
将servlet映射到 /* ，即处理所有的URL
-->
<web-app>
    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextClass</param-name>
            <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
        </init-param>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>com.huixiong.AppConfig</param-value>
        </init-param>
        <load-on-startup>0</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/*</url-pattern>
    </servlet-mapping>
</web-app>

<!--
上述配置可以看作一个样本配置。
servlet使用这个配置，首先初始化Spring MVC的DispatcherServlet，
在DispatcherServlet启动时，
会根据AppConfig创建一个类型是WebApplicationContext的IoC容器，
初始化所有Bean，绑定到ServletContext上。

因为DispactherServlet持有Ioc容器，能从IoC容器中获取所有@Controller的Bean，
所以，DispactherServlet接收到所有HTTP请求后，根据Controller方法配置的路径，
就可以正确地把请求转发到指定方法，根据ModelAndView决定如何渲染页面。

-->

```
## `6.1 Spring MVC常见注解`

- Controller
- @RequestMapping
- GetMapping
- PostMapping
- RequestParam

## `6.2 DelegatingFilterProxy`

由于Servlet和SpringIoC容器并不知道双方的存在，所以我在web.xml中的FilterSpring不知道，而如果被`Spring IoC`管理，那Servlet并不知道，所以不会起作用。

所以 `DelegatingFilterProxy`就是用来干这个的，让双方都知道`filter`的存在。

## `6.3 InterSeptor`

> Filter是拦截Servlet，在Spring框架中就是拦截 `DispatcherServlet`，而InterSeptor是拦截`DispatcherServlet`下的Controller。好处是，InterSeptor是Spring中管理的，注入非常简单。

需要实现 `HandlerInterceptor`，其中包含的常用方法有：

- preHandle：进入Controller之前
- postHandle：正确访问controller之后
- afterCompletion：无论是否正确访问controller都调用

## `6.4 CORS`

当使用A站要访问B站的API的时候，如果B站没有返回一个 `Access-Control-Allow-Origin: http://a.com`的头的话，浏览器就不允许A站访问B站的API（这个头的值包含完整的A站的访问路径）。

所以决定权完全在B站手中。

通常给A站返回一个头有一下几种方式：

1. 使用`@CrossOrigin(origins = {"http://a.com:8080"})`注解在RestController上。
2. 使用 `CorsRegistry`，在WebMvcConfigurer添加(推荐用法)：

```java
    @Bean
    WebMvcConfigurer createWebMvcConfigurer(@Autowired HandlerInterceptor[] interceptors) {
        return new WebMvcConfigurer() {
            // ...
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/**")
                        .allowedOrigins("http://local.huixiong.com:8080")
                        .allowedMethods("GET","POST")
                        .maxAge(3600);
            }
        };
    }

```

## `6.5 国际化`
## `6.6 异步处理`
## `6.7 WebSocket`
