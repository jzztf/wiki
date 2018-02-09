## javascript first try

- 放置JavaScript code的三个地方
  - body标签之间
  ```html
  <body>
  <script type="text/javascript">
    document.write("hello world!");
  </script>
  </body>
  ```
  - head标签之间
  ```html
  <head>
  <script type="text/javascript">
    document.write("hello world!");
  </script>
  </head>
  ```
  - ".js"文件引入
  ```html
  <script type="text/javascript" src="main.js"></script>
  ```

## javascript basics

- 注释-comment
  - 单行注释
  ```javascript
  //单行注释
  ```
  - 多行注释
  ```javascript
  /*多行注释
  多行注释*/
  ```

- 变量-variable

  - 命名规则
    - 字母，下划线或美元符号（$）开头
    - 区分大小写
    - 不用关键字，

- 全局变量-global variable

  - 本地变量
    - 在区块内或函数内的变量
  - 全局变量
    - 可以应用到所有作用域

- 数据类型-data type

  - 原生数据类型
    - 字符串-string
    - 数字-number
    - 布尔值-boolean
    - undefined
    - null
  - 非原生数据类型
    - 对象-Object
    - 数组-Array
    - 正则表达式-RegExp

- 操作符-operators

  - 算术运算符-arithmetic operators
  | 运算符  | 描述                   | 例子                    |
  | ---- | -------------------- | --------------------- |
  | +    | 加/addition           | 10+20 = 30            |
  | -    | 减/subtraction        | 20-10 = 10            |
  | *    | 乘/multiplication     | 10*20 = 200           |
  | /    | 除/division           | 20/10 = 2             |
  | %    | 取余/modulus/remainder | 20%10 = 0             |
  | ++   | 自加/increment         | var a=10;a++;now a=11 |
  | --   | 自减/decrement         | var a=10;a--;now a=9  |

  - 比较运算符-comparsion operators

  | 运算符  | 描述                               | 例子              |
  | ---- | -------------------------------- | --------------- |
  | ==   | 等于                               | 10==20 = false  |
  | ===  | 相同/identical(equal or same type) | 10===20 = false |
  | !=   | 不等于                              | 10!=20 = true   |
  | !==  | 不同/not identical                 | 20!==20 = false |
  | >    | 大于                               | 20>10 = true    |
  | >=   | 大于或等于                            | 20>=10 =true    |
  | <    | 少于                               | 20<10 = false   |
  | <=   | 少于或等于                            | 20<=10 = false  |

  - 位运算符-bitwise operrators

  | 运算符  | 描述                            | 例子                        |
  | ---- | ----------------------------- | ------------------------- |
  | &    | 和/and                         | (10==20 & 20==33) = false |
  | `|`  | 或/or                          | (10==20                   |
  | ^    | -/xor                         | (10==20 ^ 20==33) =false  |
  | ~    | 非/not                         | (~10) = -10               |
  | <<   | bitwise left shift            | (10<<2) = 40              |
  | >>   | bitwise right shift           | (10>>2) = 2               |
  | >>>  | bitwise right shift with zero | (10>>>2) = 2              |

  - 逻辑运算符-logical operators

  | 运算符  | 描述   | 例子                         |
  | ---- | ---- | -------------------------- |
  | &&   | 逻辑和  | (10==20 && 20==33) = false |
  | `||` | 逻辑或  | (10==20                    |
  | ！    | 逻辑非  | !(10==20) = true           |

  - 赋值运算符-assignment operators

  | 运算符  | 描述                      | 例子                          |
  | ---- | ----------------------- | --------------------------- |
  | =    | 赋值/assign               | 10+10 = 20                  |
  | +=   | 加赋值/add and assign      | var a=10;a+=20; now a = 30  |
  | -=   | 减赋值/subtract and assign | var a=10;a-=20; now a = -10 |
  | *=   | 乘赋值/multiply and assign | var a=10;a*=20; now a = 200 |
  | /=   | 除赋值/divide and assign   | var a=10;a/=20; now a=0.5   |
  | %=   | 取余赋值/modulus and assign | var a=10;a%=20; now a = 0   |

  - 特殊运算符-special operators

  | 运算符        | 描述                   |
  | ---------- | -------------------- |
  | (?:)       | 条件运算符，返回值基于给出的条件     |
  | ,          | 逗号允许在一个生命中使用多个表达式    |
  | delete     | 删除对象的一个属性            |
  | in         | 检测对象是否有相关属性          |
  | instanceof | 检测对象是否是给出类型的实例       |
  | new        | 添加新的对象               |
  | typeof     | 检测对象类型               |
  | void       | 丢弃表达式的返回值            |
  | yield      | 通过生成器的迭代器检查生成器中返回的内容 |

- if条件句-if statement

```javascript
//if条件句语法
if(expression){
  code}
//if...else
if(expression2){
  code}
else{
  code}
//if...else if...
if(expression3){
  code}
else if(expression4){
  code}
```
- switch语句-switch

```javascript
switch(expression){
  case value1:
  code;
  break;
  case value2:
  code2;
  break;
  default:
  code3;}
```

- 循环-loop

  - for循环

  ```javascript
  for(initialization;condition;increment)
  {
    code;
  }
  ```

  - while循环

  ```javascript
  while(condition)
  {
    code;
  }
  ```

  - do-while循环

   ```javascript
   do{
     code;
   }while(condition);
   ```

  - for-in 循环 
    用于迭代对象属性

  ```javascript
  ...
  ```

- 函数-function

  优点：

  - 代码重用；
  - 更少的代码

```javascript
function functionName() {
code;
}
//带参数和返回值的实例
function add(a,b) {
  var sum = a + b;
  return sum;
}
```

## javascript objects

  - 通过字面量对象创建对象

  对象字面值是封闭在花括号对({})中的一个对象的零个或多个”属性名:值”列表。

  ```javascript
  object = {property1:value1,property2:value2,...};
  //实例
  var emp = {id:102,name:john,age: 24}；
  document.write(emp.id + "<br />" + emp.name + "<br />" + emp.age);
  //通过点号可获取相关属性的值
  ```

    2. 直接创建实例

  ```javascript
  var objectName = new Obeject();
  //实例
  var emp = new Obeject();
  emp.id = 102;
  emp.name = "john";
  emp.age = 24;
  document.write(emp.id + "<br />" + emp.name + "<br />" + emp.age);
  //此法同方法一得到的结果相同
  ```

    3. 使用对象构造器

  ```javascript
  function emp(id,name,age){
  this.id = id;
  this.name = name;
  this.age = age;
  };
  e = new emp(102,"john",24);
  document.write(e.id + "<br />" + e.name + "<br />" + e.age);
  ```

  说明：可以定义方法，但是要添加和方法名相同的属性，下面看例子

  ```javascript
  function emp(name,age){
  this.name = name;
  this.age = age;

  this.grow = grow;
  function grow(number){
  this.age = number;
  }
  }

  e = emp("john", 2);
  document.write(name + ": " + age);
  e.grow(1); 
  document.write(name + ": " + age);
  ```

- 数组-array

  1. 通过数组字面量创建数组

  ```javascript
  var arrayname = [value,value2,value3];
  ```

  2. 直接创建数组

  ```javascript
  var arraname = new Array();
  ```

  3. 数组构造器创建数组

  ```javascript
  var emp = new Array("john","ben",mick");
  for(i=0;i<emp.length;i++){
  document.write(emp[i] + "<br />")
  ```

- 字符串- string

  1. 字符串字面量

  ```javascript
  var stringname = "string name";
  ```

  2. 字符串对象

  ```javascript
  var stringname = new String("string name");
  ```

  **字符串方法：**

  ```javascript
  //charAt(index)-返回给定元素的索引
  var str = “I love JavaScript!”
  document.write(charAt(0))//结果为“I”
  //cancat(str)-合并两个字符串（concat==concatenates）
  var str2 = "I am john, "
  var str3 = str2.concat(str);
  document.write(str3)//结果：“I am john, I love JavaScript!”
  //indexOf(str)-获取给定元素的索引
  document.(str.indexOf("love"));//返回2
  //lastIndexOf(str)-返回给定字符串最后一个字符的索引
  document.str.lastIndeOf("I");//返回11
  //toLowerCase()-返回给定字符串的大写
  document.write(str.toUpperCase());//返回大写
  //toUpperCase()-返回给定字符串的小写
  document.write(str.toLowerCase());//返回小写
  //slice(beginIndex,endIndex)-切片，返回给定索引之间的字符串
  document.write(str.slice(2,6));//返回love
  //trim()-整理字符串两端的空白
  var str4 = " hello javascript  ";
  document.write(str4.trim());//返回“hello javascript”
  ```

- 日期-date

```javascript
//构造日期的四种方式
var date = new Date();
var date = new Date(milliseconds);
var date = new Date(dateString);
var date = new Date(year,month,day,hours,minutes,seconds,milliseconds);
```

**日期对象的方法：**

    - getFullYear(): 获取四位数的年份
    - getMonth(): 获取0-11索引值，可将获取值加1，得到相应月份
    - getDate(): 获取1-31日期
    - getDay(): 获取0-6索引值，可结合星期数组获取星期几
    - getHours(): 获取24小时时间
    - getMinutes(): 获取分钟
    - getSeconds(): 获取秒数
    - getMilliseconds(): 获取毫秒


- 数学-math

  - Math.sqrt(n): 返回给定数值的平方根（square root）
  - Math.random(): 返回0-1的一个随机数
  - Math.pow(m,n): 返回一个幂次m的n次方
  - Math.floor(n): 返回给定数值的一个向下取整数
  - Math.ceil(n): 返回一个给定数值的一个向上取整数
  - Math.round(n): 返回一个四舍五入
  - Math.abs(n): 返回一个绝对值


- 数字-number

```javascript
var n=new Number(value);
```

  **常数：**

| 常数                | 描述             |
| ----------------- | -------------- |
| MIN-VALUE         | 最小值            |
| MAX-VALUE         | 最大值            |
| POSITIVE_INFINITY | 返回无穷大          |
| NEGATIVE-INFINITY | 返回无穷小          |
| NaN               | "not a number" |

  **数值的方法：**

  - toExponential(x)-把对象的值转换为指数计数法
  - toFixed(x)-把数字转换为字符串，结果小数点后有指定位数的数字
  - toPrecision(x)-将数字格式化为指定长度
  - toString()-将数值转为字符串
  - valueOf-将其他类型的值转为数值


- 布尔值-boolean

一个对象的布尔值：`true`or`false`

```javascript
Boolean b=new Boolean(value);
```

**布尔对象属性：**
  - constructor:返回对创建此对象的 Boolean 函数的引用
  - prototype:使您有能力向对象添加属性和方法。

**布尔对象的方法：**
  - toSource(): 作为字符串返回布尔对象的源
  - toString(): 将布尔值转成字符串
  - valueOf(): 将其他类型转成布尔值

## javascript BOM

- 浏览器对象-BOM: browser objects
- window对象-window object

window对象是浏览器对象而不是javascript对象；如果html页面包含了fram或iframe浏览器将为每个窗口创建对象

**window对象方法：**

  - alert():显示带有一段消息和确认按钮的警告框
  - confirm(): 显示带有一段消息及确认按钮和取消按钮的对话框
  - prompt(): 显示可提示用户输入的对话框
  - open(): 打开一个新的浏览器窗口或查找一个已命名的窗口
  - close(): 关闭浏览器窗口
  - setTimeout():以指定的毫秒数后调用函数或计算表达式
  - setInterval():按照指定的周期来调用函数或计算表达式

- history对象-history object

JavaScript历史对象会返回一个用户访问过的URLs数组，使用时可以为`window.history`也可以为`history`

**属性和方法：**

  - 属性-length：返回URLs数组的长度
  - 方法-forward()：加载后面的页面
  - 方法-back()：加载前面的页面
  - 方法-go()：加载某一个页面（-1为前一个，1为后一个）

- navigator对象-navigator object

navigator对象包含浏览器的信息，使用`window.navigator`也可以使用`navigator`

**navigator对象属性：**

  - appCodeName：浏览器代码名
  - appMinorVersion：返回浏览器的次级版本
  - appName：返回浏览器的名称
  - appVersion：返回浏览器的平台和版本信息
  - browserLanguage：返回当前浏览器的语言
  - cookieEnable：返回指明浏览器是否启用cookie
  - cpuClass：返回系统浏览器的CPU等级
  - onLine：返回指明系统是否处于脱机模式
  - platform：返回运行浏览器的操作系统平台
  - systemLanguage：返回OS使用的默认语言
  - userAgent：返回由客户机发送服务器的user-agent头部的值
  - userLanguage：返回OS的自然语言设置

**navigator对象方法：**

  - javaEnabled()：检测java是否启用
  - taintEnabled()：检测是否启用数据污点 (data tainting)。

- screen对象-screen object

包含客户端显示屏幕的信息，可以使用`window.screen`也可以使用`screen`

**screen 属性：**

  - width：返回屏幕宽度
  - height：返回屏幕高度
  - avaiWidth：返回屏幕宽度，除window任务栏之外
  - avaiHeight：返回屏幕高度，除window任务栏之外
  - colorDepth：返回目标设备调色板的比特深度
  - pixelDepth：返回屏幕颜色分辨率

## javsscript DOM

- 文档对象-DOM: document obejct

在html文件加载后就生成了document object，可以使用`window.document`也可以直接使用`document`

**document对象属性：**

  - anchor
  - link
  - form
    - text
    - textarea
    - checkbox
    - radio
    - select
      - option
    - reset
    - button

**document对象方法：**

  - write("string")：将指定字符串写入document
  - writeln("string")：将指定字符串，每次换新行写入document
  - getElementById()：通过ID值获取元素
  - getElementByName()：通过给定name值，获取元素数组
  - getElementByTagName()：通过标签名，获取元素数组
  - getElementByClassName()：通过类名，获取元素数组

**innerHTML属性**

  - innerHTML：设置或返回元素的内容，用法：`element.innerHTML`

## javascript validation

表单和邮件的有效性验证

- form validation
- email vaidation

## javascript events

HTML/DOM 事件

- onclick：鼠标单击
- ondbclick：鼠标双击
- onfocus：聚焦
- onsubmit：提交
- onmouseover：鼠标滑过
- onmouseout：鼠标离开
- onmousedown：鼠标按钮被按下
- onmouseup：鼠标按钮被释放
- onload：页面或图像加载完成
- onunload：页面或图像没有加载完成
- onscroll：鼠标滑轮滑动
- onresized：窗口或框架重新调整
- onreset：重置按钮被点击
- onkeydown：某个按键被按下
- onkeypress：某个按键被按下并松开
- onkeyup：某个按键被松开

参考：
1. <https://www.javatpoint.com/>

2. <http://www.w3school.com.cn/>

   ​