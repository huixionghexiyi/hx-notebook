> `==`比较的是两个对象的值是不是相同的，如果两个对象是引用类型，那么比较的就是引用所指向的内存地址。而 `equals`是`Object`类的一个方法，目的是解决两个不同对象内容相同，但是使用 `==` 依然不相等的问题。 `hashCode`则是在 `equals`的基础上，判断 `Map`中的key与value的对应关系。


# `==`&`equals`


例如：

```java
String s1 = new String("a");
String s2 = new String("a");
s1 == s2; // false
```
s1和s2两个引用指向的是两个不同的String实例，也就是说所指向的内存是不同的。但是我们看到s1和s2的值是相同的，这不满足我们的需求。所以，需要使用 `equals`。需要`class`实现 `equals`方法。 `String`中的 `equals`方法是这样实现的：

```java
    public boolean equals(Object anObject) {
        if (this == anObject) { // 先比较是不是同一个实例对象。
            return true;
        }
        if (anObject instanceof String) { // 判断是不是继承自String,由于传参是Object类型的所以都会满足，这样写的目的可能是为了避免未来出现不能转换为Object的参数。
            String anotherString = (String)anObject;//转换为String类型
            int n = value.length; // 获取当前value的长度
            if (n == anotherString.value.length) { // 先比较长度
                char v1[] = value; 
                char v2[] = anotherString.value;// 要比较的字符串的长度
                int i = 0;
                while (n-- != 0) { //逐个比较字符
                    if (v1[i] != v2[i])
                        return false;
                    i++;
                }
                return true;
            }
        }
        return false;
    }
```

我们知道了 `equals`的目的后，自己写一个来练习一下，在此之前，需要知道重写 `equals`的几个原则：

- 自反性（Reflexive）：对于非`null`的`x`来说，`x.equals(x)`必须返回`true`；
- 对称性（Symmetric）：对于非`null`的`x`和`y`来说，如果`x.equals(y)`为`true`，则`y.equals(x)`也必须为`true`；
- 传递性（Transitive）：对于非`null`的`x`、`y`和`z`来说，如果`x.equals(y)`为`true`，`y.equals(z)`也为`true`，那么`x.equals(z)`也必须为`true`；
- 一致性（Consistent）：对于非`null`的`x`和`y`来说，只要`x`和`y`状态不变，则`x.equals(y)`总是一致地返回`true`或者`false`；
- 对`null`的比较：即`x.equals(null)`永远返回`false`。

案例：

```java
public class Student(){
    private String name;
    private int age;
    @Override
    public boolean equals(Object o){
        if(o instanceof Student){ // 判断是不是Student的实例
            Person p = (Person)o; // 强制转换类型
            boolean nameEquals = false; // 定义字段存储name是否相等
            if(this.name == null && p.name == null){ // 如果name都为空
                nameEquals = true;
            }
            if(this.name == null){ // 如果this的name为空
                nameEquals = this.name.equals(p.name);
            }
            return nameEquals && this.age == p.age; // 综合name和age的结果
        }
    }
}
```
总结一下，编写的步骤为：

1. 确定要比较的对象的字段，哪些字段相等就认为这两个对象相等。
2. 判断对象的类型。
3. 引用类型比较值，注意为 `null`的情况。
4. 基本类型用 `==` 比较就行。
5. 综合比较结果。


# `equals`&`hashCode`

在实现了`Map`接口的类中，`key`可以为任意对象，如果传入的key不是同一对象，且没有重写 `equals`方法，那么将不能取到同一个 `value`。

所以，我们通常用 `String`作为key。

那么，我们如何通过一个key找到value呢？答案是通过`hashCode`计算得到 `value`的索引。

`String`类中 `hashCode`的实现：
```java
    public int hashCode() {
        int h = hash;
        if (h == 0 && value.length > 0) {
            char val[] = value;
            for (int i = 0; i < value.length; i++) {
                h = 31 * h + val[i];
            }
            hash = h;
        }
        return h;
    }

```
在 `HashMap`中，通过调用 `key`的 `hashCode`方法计算求得 `h`。这个 `h`就是在 `HashMap`中的索引。

如果两个不同的对象的 `hashCode`求得的 `h`值相同的话。

通常如果要实现 `hashCode`都需要实现 `equals`方法。并且，需要满足：

1. 两个对象通过`equals`方法返回`true`，则两个方法的`hashCode`必须相等。
2. 若两个对象 `equals`方法返回 `false`，则 `hashCode`尽量不要想等。
