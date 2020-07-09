# Spring

1. IoC容器


## `IoC（Inversion of Control）容器`

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

## `Resource`

`class`位置：`org.springframework.core.io.Resource`

` @Value("classpath:/logo.txt")`

资源通常放到 `src/main/resources`中。

## 注入配置


# 