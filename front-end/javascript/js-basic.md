 [Table of Content]

- [JS基础语法](#JS基础语法)
- [数组](#数组)
- [流程控制语句](#流程控制语句)
- [函数](#函数)
- [事件响应](#事件响应)
- [JS内置对象](#JS内置对象)
- [浏览器对象](#浏览器对象)

## JS基础语法

**JavaScript能做什么？**

1. 增强页面动态效果(如:下拉菜单、图片轮播、信息滚动等)
2. 实现页面与用户之间的实时、动态交互(如:用户注册、登陆验证等)

### 变量

1. 变量命名
   规则：

   - 必须以字母、下划线或美元符号开头，之后可以是字母、数字、下划线 或美元符号。

   - 变量名区分大小写

   - 不允许使用JavaScript关键字和保留字做变量名

     | *关键字*      | break | case    | catch  | default | delete |
     | ---------- | ----- | ------- | ------ | ------- | ------ |
     | do         | else  | finally | for    | if      | in     |
     | instanceof | new   | return  | switch | throw   | try    |
     | typeof     | var   | void    | while  |         |        |

     | *保留字*     | abstract | boolean | byte        | char      | class   |
     | --------- | -------- | ------- | ----------- | --------- | ------- |
     | const     | debugger | double  | enum        | export    | extend  |
     | final     | float    | goto    | implements  | import    | int     |
     | interface | native   | package | private     | protected | public  |
     | short     | static   | super   | sychronized | throw     | transie |
     | volatile  |          |         |             |           |         |

2. 变量声明
   变量声明语法：`var 变量名；`

   ```javascript
   //js变量需在声明后使用；声明多个变量使用逗号隔开。
   var num;
   var num, num2;
   ```

   ​

3. 变量赋值

   ```javascript
   //赋值方法一
   var num;
   num = 10;
   //赋值方法二
   var num = 10;
   //赋值字符串
   var str = "javascript";
   //赋值布尔值
   var num2=true;
   ```

   ​
### 表达式

表达式是指具有一定的值、用操作符把常数和变量连接起来的代数式。**一个表达式可以包含常数或变量。**

```javascript
//串表达式
"java" + "script"
"hello" + char
//数值表达式
2 + 3
3 + num
//布尔表达式
2 > 4
3 < 4
```

1. `+`号操作符
   `+`号操作符不仅能进行数学运算，还能将两个字符串连接起来

2. `++`和`--`
   `++`和`--`分别表示自加1和自减1

3. 比较操作符

   | 符号   | 意义   |
   | ---- | ---- |
   | `>`  | 大于   |
   | `<`  | 小于   |
   | `>=` | 大于等于 |
   | `<=` | 小于等于 |
   | `!=` | 不等于  |
   | `==` | 等于   |

   ​

4. 逻辑“与”操作符
   `&&`两个条件同时满足为真否则为假

5. 逻辑“或”操作符
   `||`两个条件满足其一为真否则为假

6. 逻辑“非操作符”
   `！`逻辑非，取反

7. 操作符优先级

   算术操作符 → 比较操作符 → 逻辑操作符 → "="赋值符号（高→低）

## 数组

数组是一个值的集合，每个值都有一个索引号，从0开始，每个索引都有一个相应的值，根据需要添加更多数值。

1. 创建数组

   ```javascript
   var myarr = new Array();
   //myarr为新创建的数组名
   myarr[0]
   //索引数组中第一个值；如果为空值，则输出undefine。
   new Array(number)
   //new Array()可带参数，规定新建一个几个元素的数组，但是实际情况可以超出
   ```

   ​

2. 数组赋值

   ```javascript
   //方法1
   var myarr = new Array(20, 29, 30, 33);
   //方法2
   var myarr = [20, 29, 30, 33];
   //数组值可为“数字”，“字符串”，“布尔值”等
   ```

   ​

3. 数组添加新元素

   ```javascript
   myarr[4] = 40;
   //使用下一个未使用索引，添加新元素
   ```

   ​

4. 使用数组元素

   ```javascript
   var fourth = myarr[3];
   //第四个元素；索引使用
   ```

   ​

5. 获取数组长度

   ```javascript
   myarr.length
   //获取myarr的长度
   ```

   ​

6. 二维数组

   ```javascript
   //二维数组定义方法1
   var myarr=new Array();  //先声明一维 
   for(var i=0;i<2;i++){   //一维长度为2
      myarr[i]=new Array();  //再声明二维 
      for(var j=0;j<3;j++){   //二维长度为3
      myarr[i][j]=i+j;   // 赋值，每个数组元素的值为i+j
      }
    }
   //二维数组定义方法2
   var myarr = [[0,1,2],[0,1,2,3]];
   //二维数组赋值
   myarr[1][2] = 5;
   ```

   ​

## 流程控制语句

1. if语句

   ```javascript
   //基础语句
   if(条件)
      {条件成立时执行的代码};
   //if...else语句
   if(条件)
      {条件成立时执行的代码}
   else
     {条件不成立时执行的代码};
   //if..else嵌套
   if(条件)
      {条件成立时执行的代码}
   else if(条件2)
     {条件不成立时执行的代码}
   else
     {条件不成立时执行的代码};
   ```

   ​

2. switch语句

   ```javascript
   //进行单一对象选择时使用
   switch(表达式)
   {
   case值1:
     执行代码块 1
     break;
   case值2:
     执行代码块 2
     break;
   ...
   case值n:
     执行代码块 n
     break;
   default:
     与 case值1 、 case值2...case值n 不同时执行的代码
   }
   //switch要配初始值
   //语句结束使用break结束语句
   //结尾要有default默认
   ```

   ​

3. for循环

   ```javascript
   for(初始化变量;循环条件;循环迭代)
   {     
       循环语句 
    }
   ```

   ​

4. while循环

   ```javascript
   while(判断条件)
   {
       循环语句
    }
   //do ...while保证循环至少一次
   do
   {
     循环语句
   }
   while(条件判断)
   ```

   ​

5. break退出循环

   ```javascript
   //for语句；while语句；do...while语句都可以使用break在满足条件时退出循环
   for(初始条件;判断条件;循环后条件值更新)
   {
     if(特殊情况)
     {break;}
     循环代码
   }
   ```

   ​

6. continue继续循环

   ```javascript
   for(初始条件;判断条件;循环后条件值更新)
   {
     if(特殊情况)
     { continue; }
    循环代码
   }
   ```

   ​

## 函数

1. 函数定义

   ```javascript
   function  函数名( )
   {
        函数体;
   }
   ```

   ​

2. 函数调用

   - 在javascript代码内调用
   - 在html中作为点击按钮调用

3. 有参数的函数

   ```javascript
   function 函数名(参数1,参数2)
   {
        函数代码
   }
   ```

   ​

4. 返回值
   在函数中将某一结果返回

   ```javascript
   function add(x,y)
   {
     var sum,x,y;
     sum = x + y;
     return sum;
   };
   ```

   ​

## 事件响应

JavaScript 创建动态页面。事件是可以被 JavaScript 侦测到的行为。 网页中的每个元素都可以产生某些可以触发 JavaScript 函数或程序的事件。

比如说，当用户单击按钮或者提交表单数据时，就发生一个鼠标单击（onclick）事件，需要浏览器做出处理，返回给用户一个结果。

| 事件          | 说明         |
| ----------- | ---------- |
| onclick     | 鼠标单击事件     |
| onmouseover | 鼠标经过事件     |
| onmouseout  | 鼠标移开事件     |
| onchange    | 文本框内容改变事件  |
| onselect    | 文本框内容被选中事件 |
| onfocus     | 光标聚焦       |
| onblur      | 光标离开       |
| onload      | 网页导入       |
| onunload    | 关闭网页       |



1. 鼠标单击事件

   ```html
   <input name="点击我" type="button" value="点击我" onClick="window.open()"/>
   <!--点击按钮时，调用函数window.open()-->
   ```

   ​

2. 鼠标经过事件

   ```html
   <form>
   密码:<input name="password" type="password" >
   <input name="确定" type="button" value="确定" onmouseover="message()"/>
   </form>
   <!--鼠标经过确定按钮调用message()函数-->
   ```

   ​

3. 鼠标移开事件

   ```html
   <form>
     <a href="http://www.imooc.com" onmouseout="message()">点击我</a>
   </form>
   <!--鼠标移开链接调用message()函数-->
   ```

   ​

4. 文本框内容改变事件

   ```html
   <body>
     <form>
     个人简介：<br>
      <textarea name="summary" cols="60" rows="5" onchange="message()">请写入个人简介，不少于200字！</textarea>
     </form>
   </body>
   <!--文本框内容被改变时调用函数message()-->
   ```

   ​

5. 文本框内容被选中事件

   ```html
   <body>
     <form>
     个人简介：<br>
      <textarea name="summary" cols="60" rows="5" onselect="message()">请写入个人简介，不少于200字！</textarea>
     </form>
   </body>
   <!--文本框内容被选中后调用函数message()-->
   ```

   ​

6. 光标聚焦

   ```html
   <body>
   请选择您的职业：<br>
     <form>
       <select name="career" onfocus="message()"> 
         <option>学生</option> 
         <option>教师</option> 
         <option>工程师</option> 
         <option>演员</option> 
         <option>会计</option> 
       </select> 
     </form>
   </body>
   <!--光标聚焦调用函数message()-->
   ```

   ​

7. 光标离开

   ```html
   <body>
     <form>
      用户:<input name="username" type="text" value="请输入用户名！" >
      密码:<input name="password" type="text" value="请输入密码！" onblur="message()">
     </form>
   </body>
   <!--光标从文本框移开调用函数message()-->
   ```

   ​

8. 网页导入

   ```html
   <body onload="message()">
     欢迎学习JavaScript。
   </body>
   <!--body被载入时调用函数message()-->
   ```

   ​

9. 关闭网页

   ```html
   <body onunload="message()">
     欢迎学习JavaScript。
   </body>
   <!--当页面被关闭时调用函数message()-->
   ```

   ​

## JS内置对象

JavaScript 中的所有事物都是对象，如:字符串、数值、数组、函数等，每个对象带有**属性**和**方法**。

- **对象的属性：**反映该对象某些特定的性质的，如：字符串的长度、图像的长宽等；
- **对象的方法：**能够在对象上执行的动作。例如，表单的“提交”(Submit)，时间的“获取”(getYear)等；

javascript提供了多个内建对象，比如 String、Date、Array 等等，使用对象前先定义，如下使用数组对象：

```javascript
//使用new关键字创建对象
var objectName = new Array();
或者
var objectName = [];
//访问对象属性
objectName.porpertyName //比如获取数组长度myarr.length
//使用对象的方法
objectName.methodName() //比如让字符串转换大写str.toUpperCase()
```



1. Date日期对象

   - 日期对象可以存储任意一个日期，并且可以精确到毫秒数（1/1000秒）

   ```javascript
   //创建时间对象
   var Udate = new Date()
   //说明：使用关键字new，Date()的首字母必须大写
   //Udate为日期对象，并有一个初始值——当前电脑时间，也可以自定义
   var d = new Date(2017, 12, 8);
   var d = new Date('Dec 8, 2017');
   //访问日期
   <日期对象>.<方法>
   ```

   - Date对象中处理时间和日期的常用方法

   | 方法名称              | 功能描述              |
   | ----------------- | ----------------- |
   | get/setDate()     | 返回/设置日期           |
   | get/setFullYear() | 返回/设置年份，用四位数表示    |
   | get/setYear()     | 返回/设置年份           |
   | get/setMonth()    | 返回/设置月份，类似于索引对应加一 |
   | get/setHours()    | 返回/设置小时，24小时制     |
   | get/setMinutes()  | 返回/设置分钟数          |
   | get/setSeconds()  | 返回/设置秒钟数          |
   | get/setTime()     | 返回/设置时间，毫秒为单位     |

   - 返回星期的办法：getDay()返回数字0-6，0表示星期天，

   ```javascript
   var mydate=new Date();//定义日期对象
   var weekday=["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];
   //定义数组对象,给每个数组项赋值
   var mynum=mydate.getDay();//返回值存储在变量mynum中
   document.write(mydate.getDay());//输出getDay()获取值
   document.write("今天是："+ weekday[mynum]);//输出星期几
   ```

   - 返回设置时间

   ```javascript
   //计算从1970年1月1日到日期对象所指的日期的毫秒数
   var mydate=new Date();
   document.write("当前时间："+mydate+"<br>");
   mydate.setTime(mydate.getTime() + 60 * 60 * 1000);//设置获取的日期+一小时
   document.write("推迟一小时时间：" + mydate);
   ```

   ​

2. string字符串对象

   ```javascript
   //字符串赋值
   var mystr = "I Love JavaScript"
   //访问字符串对象
   mystr.length
   //使用字符串方法
   mystr.toUpperCase()
   //返回指定位置的字符串,空格也算字符串；
   mystr.charAt(index)//index为索引值
   //返回指定字符串首次出现的位置，返回索引值；字符串没有出现返回-1
   mystr.indexOf(substring, startpos)
   /*说明：substring为检索的字符串，startpos为开始检索位置，可选整数参数，取值范围0-'mystr.length-1'；*/
   //字符串分割
   mystr.split(separator, limit)
   /*说明：split()方法将字符串分割成字符串数组，并返回该数组；separator为必选参数从该指定位置开始分割，limit为可选参数，表示分割的次数；如果separator为""则分割每一个字符*/
   //提取字符串
   mystr.substring(startPos, stopPos)
   /*说明：startPos为一个非负整数，表示提取开始的位置；
   stopPos为可选的非负整数，表示结束为止，如果没有指定咋会提取到结尾；
   返回的内容为stop-start，如果两者相等，则返回空字符串；
   如果start大于stop，则会自动调换*/
   //提取指定数目的字符
   mystr.substr(startPos, length)
   /*说明：startPos提取字串的起始位置，length为可选；
   如果startPos为负数则按照从尾部索引来计算*/

   ```

3. Math对象
   Math对象，提供对数据的数学计算。
   Math 对象是一个固有的对象，无需创建它，直接把 Math 作为对象使用就可以调用其所有属性和方法。这是它与Date,String对象的区别。

   ```javascript

   ```

   - Math对象属性

     | 属性      | 说明                        |
     | ------- | ------------------------- |
     | E       | 返回算数常数e，自然对数的底数（约等于2.718） |
     | LN2     | 返回2的自然对数（约等于0.693）        |
     | LN10    | 返回10的自然对数（约等于2.302）       |
     | LOG2E   | 返回以2为底的e的对数（约等于1.442）     |
     | LOG10E  | 返回以10为底的e的对数（约等于0.434）    |
     | PI      | 返回圆周率                     |
     | SQRTI_2 | 返回2的平方根的倒数（约等于0.707）      |
     | SQRTI2  | 返回2的平方根（约等于1.414）         |

   - Math对象方法(部分)

     | 方法         | 描述           |
     | ---------- | ------------ |
     | abs(x)     | 返回绝对值        |
     | max(x,y)   | 返回x和y中的最高值   |
     | min(x,y)   | 返回x和y中的最低值   |
     | random()   | 返回0-1之间的随机数  |
     | round()    | 把数四舍五入为最近数   |
     | toSource() | 返回该对象的源代码    |
     | valueOf()  | 返回Math对象的原始值 |
     | ceil(x)    | 向上取整数        |
     | floor()    | 向下取整         |

     ```javascript
     //向上取整数
     Math.ceil(x)
     Math.ceil(0.1)//向上取整就是1
     Mathceil(-1.2)//向上取整就是-1
     //向下取整
     Math.floor(x)
     Math.floor(0.1)//向下取整就是0
     Math.floor(-1.2)//向下取整就是-2
     //四舍五入
     Math.round(x)
     Math.round(5.4)//取整5
     Math.round(5.5)//取整6；该方法采取向上取整
     //取随机数
     Math.random()//0-1取随机数
     (Math.random())*10//0-10取随机整数
     ```

     ​

4. Array数组对象
   数组对象是一个对象的集合，里边的对象可以是不同类型的。数组的每一个成员对象都有一个“下标”，用来表示它在数组中的位置，是从零开始的

   ```javascript
   //定义空数组
   var 数组名 = new Array()
   //定义n个空元素的数组
   var 数组名 = new Array(n)
   //定义数组时，直接初始化数据
   var 数组名 = [<元素1>,<元素2>,<元素3>...]
   //数组元素使用
   数组名[下标] = 值
   //数组的属性,返回数组长度
   数组名.length
   //数组的方法

   ```

   - 数组的方法

     | 方法              | 描述                             |
     | --------------- | ------------------------------ |
     | concat()        | 连接两个或更多的数组，并返回结果               |
     | join()          | 把数组的所有元素放入一个字符串，元素通过指定的分隔符进行分割 |
     | pop()           | 删除并返回数组的最后一个元素                 |
     | push()          | 向数组的末尾添加一个或更多元素并返回新的长度         |
     | reverse()       | 颠倒数组中的元素的顺序                    |
     | shift()         | 删除并返回数组的第一个元素                  |
     | slice()         | 从某个已有的数组返回选定的元素                |
     | sort()          | 对数组进行排序                        |
     | splice()        | 删除元素，冰箱数组添加新元素                 |
     | toSource()      | 返回该对象的源代码                      |
     | toString()      | 把数组转换成字符串，并返回结果                |
     | toLocalString() | 把数组转换成本地数组，并返回结果               |
     | unshift()       | 向数组的开头添加一个或更多元素，并返回新的长度        |
     | valueOf()       | 返回数组对象的原始值                     |

     ```javascript
     //concat()连接数组
       var mya1= new Array("I","love");
       var mya2= new Array("JavaScript","!");
       var mya3=mya1.concat(mya2);
       document.write(mya2);
     //join()连接数组元素
     mya3.join(".")//将mya3中的数组用“.”来连接
     //reverse()颠倒数组顺序
     mya3.reverse()
     //slice()选定元素
     arrayObject.slice(start,end)
     /*start为必选值，end可选值；该方法不会修改数组，只会返回子数组；可使用复数从尾部选取元素；string.silce()和array.slice()类似*/
     //sort()数组排序
     arrayObject.sort(方法函数)
     /*方法函数可选，如果不指定按照unicode码顺序排列；*/
     function sortNum(a,b) {
     return a - b;
     //升序，如降序，把“a - b”该成“b - a”
     }
     document.write(myarr.sort(sortNum))

     ```

     ​



## 浏览器对象

1. windows对象
   window对象是BOM的核心，window对象指当前的浏览器窗口。

   | 方法              | 描述                      |
   | --------------- | ----------------------- |
   | **alert()**     | 显示带有一段消息和一个确定按钮的警告框     |
   | **prompt(**)    | 显示可提示用户输入的对话框           |
   | **confirm()**   | 显示带有一段消息以及确认按钮和取消按钮的对话框 |
   | open()          | 打开一个新的浏览器窗口或查找一个已命名的窗口  |
   | close()         | 关闭浏览器窗口                 |
   | print()         | 打印当前窗口的内容               |
   | focus()         | 把键盘焦点给于一个窗口             |
   | blur()          | 把键盘焦点从顶层窗口移开            |
   | moveBy()        | 可相对窗口的当前坐标把它移动到指定的像素    |
   | moveTo()        | 把窗口的左上角移动到一个指定的坐标       |
   | resizeBy()      | 按照指定的像素调整窗口的大小          |
   | resizeTo()      | 把窗口的大小调整到指定的宽度和高度       |
   | scrollBy()      | 按照指定的像素值来滚动内容           |
   | scrollTo()      | 把内容滚动到指定的坐标             |
   | setInterval()   | 每隔指定的时间执行代码             |
   | setTimeout()    | 在指定的延迟时间来执行代码           |
   | clearInterval() | 取消setInterval()设置       |
   | clearTimeout()  | 取消setTimeout()的设置       |
   |                 |                         |

   计时器：一次性计时器；间隔性计时器

   ```javascript
   //语法
   setInterval(代码，交互时间)；
   /*参数说明：
   代码是要调用的函数或要执行的代码串；
   交互时间指周期性执行或调用表达式之间的时间间隔，以毫秒计（1s=1000ms）
   返回值：
   一个可以传递给clearInterval()从而取消对“代码”的周期性执行的值
   */
   //调用函数"clock()"例子
   setInterval("clock()",1000)
   或者
   setInterval(clock,1000)
   //取消设定
   var i=setInterval(代码，交互时间);
   clearInterval(i);
   //语法
   setTimeout(代码，交互时间)
   //取消设定
   var i=setTimeout(代码，交互时间)；
   clearTimeout(i);

   ```

2. history对象
   history对象记录了用户曾经浏览过的页面URL，并且可以实现浏览器前进与后退类似的导航功能；**注意:从窗口被打开的那一刻开始记录，每个浏览器窗口、每个标签页乃至每个框架，都有自己的history对象与特定的window对象关联。**

   ```javascript
   //语法：
   window.history.[属性|方法]
   //注意：Window可以省略
   ```

   history对象属性和方法

   | 属性        | 描述                  |
   | --------- | ------------------- |
   | length    | 返回浏览器历史列表中的URL数量    |
   | **方法**    | **描述**              |
   | back()    | 加载history列表中上一个URL  |
   | forward() | 加载history列表中下一个URL  |
   | go()      | 加载history列表中某个具体的页面 |

   说明：`go()`取值“-1”，“1”分别相当于`back()`和`forward()`

3. location对象
   location用于获取或设置窗体的URL，并且可以用于解析URL

   ```javascript
   //语法
   location.[属性|方法]
   ```

   location对象属性
   ![location对象.jpg](http://upload-images.jianshu.io/upload_images/6540347-c24219e70e8f4994.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

   | 属性        | 描述                   |
   | --------- | -------------------- |
   | hash      | 设置或返回从#号开始的URL（锚)    |
   | host      | 设置或返回主机名和当前URL的端口号   |
   | hostname  | 设置或返回当前URL主机名        |
   | href      | 设置或返回完整的URL          |
   | pathname  | 设置或返回当前URL的路径部分      |
   | port      | 设置或返回当前URL的端口号       |
   | protocol  | 设置或返回当前URL的协议        |
   | search    | 设置或返回从问号开始的URL（查询部分） |
   | **方法**    | **描述**               |
   | assign()  | 加载新的文档               |
   | reload()  | 重新加载当前文档             |
   | replace() | 用新的文档替换当前文档          |

   ​

4. navigator对象
   Navigator 对象包含有关浏览器的信息，通常用于检测浏览器与操作系统的版本。
   **对象属性：**

   | 属性          | 描述                         |
   | ----------- | -------------------------- |
   | appCodeName | 浏览器代码的字符串表示                |
   | appName     | 返回浏览器的名称                   |
   | appVersion  | 返回运行浏览器的平台和版本信息            |
   | platform    | 返回运行浏览器的操作系统               |
   | userAgent   | 返回由客户机发送服务器的user-agent头部信息 |

   userAgent可以用来判断使用什么浏览器

   ```javascript
   function validB(){ 
     var u_agent = navigator.userAgent; 
     var B_name="Failed to identify the browser"; 
     //大于-1表示找到想对应信息
     if(u_agent.indexOf("Firefox")>-1){ 
         B_name="Firefox"; 
     }else if(u_agent.indexOf("Chrome")>-1){ 
         B_name="Chrome"; 
     }else if(u_agent.indexOf("MSIE")>-1&&u_agent.indexOf("Trident")>-1){ 
         B_name="IE(8-10)";  
     }
       document.write("B_name:"+B_name+"<br>");
       document.write("u_agent:"+u_agent+"<br>"); 
   } 
   ```

   ​

5. screen对象
   screen对象用于获取用户的屏幕信息。

   ```javascript
   //语法
   window.screen.属性
   ```

   **对象属性：**

   | 属性          | 描述                           |
   | ----------- | ---------------------------- |
   | availHeight | 窗口可以使用的屏幕的高度，单位像素            |
   | availWidth  | 窗口可以使用屏幕的宽度，单位像素             |
   | colorDepth  | 用户浏览器表示的颜色位数，通常为32位（每个像素的位数） |
   | pixelDepth  | 用户浏览器表示的颜色位数，通常为32位（每个像素的位数） |
   | height      | 屏幕高度，单位像素                    |
   | width       | 屏幕宽度，单位像素                    |

   ​

6. ​

## DOM对象

文档对象模型DOM（Document Object Model）定义访问和处理HTML文档的标准方法。DOM 将HTML文档呈现为带有元素、属性和文本的树结构（节点树）。

HTML文档可以说是节点构成的集合，DOM节点有：元素节点、文本节点和属性节点。

- 元素节点：<html>、<body>、<p>等都是元素节点，即标签。
- 文本节点：向用户展示的内容，如<li>...</li>中的JavaScript、DOM、CSS等文本。
- 属性节点：元素属性，如<a>标签的链接属性href="http://www.imooc.com"。

**节点属性：**

| 方法        | 说明                   |
| --------- | -------------------- |
| nodeName  | 返回一个字符串，为内容是给定节点的名字  |
| nodeType  | 返回一个整数，这个数值代表给定节点的类型 |
| nodeValue | 返回给定节点的当前值           |

**遍历节点数：**

| 方法              | 说明                       |
| --------------- | ------------------------ |
| childNodes      | 返回一个数组，这个数组由给定元素节点的子节点构成 |
| firstChild      | 返回第一个子节点                 |
| lastChild       | 返回最后一个子节点                |
| parentNode      | 返回一个给定节点的父节点             |
| nexSibling      | 返回给定节点的下一个子节点            |
| previousSibling | 返回给定节点的上一个子节点            |

**DOM操作：**

| 方法                     | 说明                        |
| ---------------------- | ------------------------- |
| createElement(element) | 创建一个新的元素节点                |
| createTextNode()       | 创建一个包含着给定文本的新文本节点         |
| appendChild()          | 指定节点的最后一个节点列表之后添加一个新的子节点  |
| insertBefore()         | 将一个新节点插入到一个给定元素节点的给定子节点前面 |
| removeChild()          | 从一个给定元素删除一个子节点            |
| replaceChild()         | 把一个给定父元素里的一个子节点替换为另外一个节点  |



1. getElementsByName()方法
   返回带有指定名称的**节点对象的集合**

   ```javascript
   //语法
   document.getElementsByName(name)
   /*注意：
   1. 由于文档中name属性可能不唯一，所以该方法返回一个数组
   2. 和数组类似，该数组具备数组的特性，可以有方法length和访问
   */
   ```

2. getElementsByTagName()方法
   返回带有指定标签名的**节点对象的集合**。返回元素的顺序是它们在文档中的顺序。

   ```javascript
   //语法：
   document.getElementsByTagName()
   /*说明：
   1.tagname是标签的名称，如p、a、img等
   2.和数组一样有类似特性*/
   ```

   **例子：**

   ```html
   <form>
     请选择你爱好:<br>
     <input type="checkbox" name="hobby" id="hobby1">  音乐
     <input type="checkbox" name="hobby" id="hobby2">  登山
   </form>
   <script>
     var hobby = document.getElementsByTagName("input");
     //hobby是一个带有"input"标签的节点对象的集合
     var type = hobby[0].type;
     var name = hobby[0].name;
     var id = hobby[0].id;
   </script>
   <!--如上
   type = checkbox
   name = hobby
   id = hobby1
   -->
   ```

   ​

3. getAtrribute()方法

   通过元素节点的属性名称获取属性的值

   ```javascript
   //语法
   elementNode.getAttribute(name)
   //"elementNode"可以通过getELementById(),getElementByTagName()获得的元素节点
   //"name"要想查询的元素节点的属性名字
   ```

4. setAttribute()方法
   setAttribute() 方法增加一个指定名称和值的新属性，或者把一个现有的属性设定为指定的值。

   ```javascript
   //语法
   elementNode.setAttribute(name,value)
   //name为属性的名称，value为属性的值；同getAttribute()通过获得的元素节点进行设置
   ```

5. 节点属性

   在文档对象模型 (DOM) 中，每个节点都是一个对象。DOM 节点有三个重要的属性 ：

   - nodeName : 节点的名称
   - nodeValue ：节点的值
   - nodeType ：节点的类型

   | 节点     | nodeName  | nodeValue      | nodeType |
   | ------ | --------- | -------------- | -------- |
   | **属性** | 节点的名称为只读  | 节点的值           | 节点的类型只读  |
   | 元素节点   | 同节点的标签名   | undefined/null | 1        |
   | 属性节点   | 节点的属性名    | 属性的值           | 2        |
   | 文本节点   | #text     | 文本自身           | 3        |
   | 文档节点   | #document | ---            | 9        |
   | ---    | ---       | ---            | 注释：8     |

6. 访问子节点childNodes

   访问选定元素节点下的所有子节点的列表，返回的值可以看作是一个数组，他具有length属性。

   ```javascript
   //语法
   elementNode.childNodes
   //注意：如果选定的节点没有子节点，则改属性返回不包含节点的NodeList
   //ie和其他浏览器存在兼容问题，ie中空白也算一个节点
   ```

   访问第一个子节点和最后一个子节点

   ```javascript
   //第一个子节点
   firstChild
   //最后一个子节点
   lastChild
   ```

   ​

7. 访问父节点

   获得指定节点的父节点

   ```javascript
   //语法
   elementNode.parentNode
   //注意：父节点只能有一个
   //访问祖节点
   elementNode.parentNode.parentNode
   ```

   ​

8. 访问兄弟节点

   - nextSibling 属性可返回某个节点之后紧跟的节点（处于同一树层级中）

   ```javascript
   //语法
   nodeObject.nextSibling
   //zhuyi，则返回null
   ```

   - previousSibling 属性可返回某个节点之前紧跟的节点（处于同一树层级中）。

   ```javascript
   //语法
   nodeObject.previousSibling
   //如果没有此节点，则返回null
   //通过判断type是否为1确定是不是空白字符节点
   ```

9. 插入节点appendChild()

   ```javascript
   //语法
   appendChild(newnode)
   //例子
   var otest = document.getElementById("test");  
   //创建一个新元素
   var newnode = document.createElement("li");
   //将创建的元素添加新内容
   newnode.innerHTML = "PHP"
   otest.appendChild(newnode);
   ```

   ​

10. 插入节点insetBefore()

  insertBefore() 方法可在已有的子节点前插入一个新的子节点。

  ```javascript
  //语法
  insertBefore(newnode,node)
  //参数
  /*newnode:要插入新的节点；node:在此之前插入节点*/
  //例子
  var otest = document.getElementById("test");  
  var newnode = document.createElement("li");
  newnode.innerHTML = "PHP"
  //使用子节点
  otest.insertBefore(newnode,otest.childNodes[1])
  ```

  ​

11. 删除节点removeChild()

    removeChild() 方法从子节点列表中删除某个节点。如删除成功，此方法可返回被删除的节点，如失败，则返回 NULL。

    ```javascript
    //语法
    nodeObject.removeChild(node)
    //node为必选
    ```

    ​

12. 替换元素节点replaceChild()

    replaceChild 实现子节点(对象)的替换。返回被替换对象的引用。

    ```javascript
    //语法
    node.replaceChild(newnode,oldnew)
    /*注意：
    newnode和oldnew都为必需；
    newnode必须提前创建；*/
    ```

    例子：

    ```javascript
    function replaceMessage(){
    //创建一个新的元素节点
      var newnode = document.createElement("i");
      var text = document.getElementById("oldnode").innerHTML;
    //创建一个新的文本节点
      var newnodeText = document.createTextNode(text);
    //将文本节点和元素节点结合
      newnode.appendChild(newnodeText);
    //定义旧节点
      var oldnode = document.getElementById("oldnode");
    //替换节点
      oldnode.parentNode.replaceChild(newnode,oldnode);
    } 
    ```

    ​

13. 创建元素节点createElement

    createElement()方法可创建元素节点。此方法可返回一个 Element 对象。

    ```javascript
    //语法
    document.createElement(tagName)
    /*tagName：字符串值，用来指明创建元素的类型；要结合appendChild()和insertBefore()一起使用*/
    ```

    ​

    ```html
    <script type="text/javascript">
      //创建按钮
       var body = document.body; 
       var input = document.createElement("input");  
       input.type = "button";  
       input.value = "创建一个按钮";  
       body.appendChild(input); 
      //使用setAttribute设置属性
       var body= document.body;             
       var btn = document.createElement("input");  
       btn.setAttribute("type", "text");  
       btn.setAttribute("name", "q");  
       btn.setAttribute("value", "使用setAttribute");  
       btn.setAttribute("onclick", "javascript:alert('This is a text!');");       
       body.appendChild(btn);  
    </script> 
    ```
