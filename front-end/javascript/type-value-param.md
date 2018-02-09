# 类型,值和变量

- 能够表示并操作的值的类型称作数据类型(type),编程语言最基本的特性就是能够支持多种数据类型
- js的数据类型分为
  - 原始数据类型(primitive type)
    - 数字
    - 字符串
    - 布尔值
    - null
    - undefined
  - 对象类型(object type)
    - 对象(object)是属性(property)的集合,每个属性都有"名-值"队组成
    - 全局对象(global object)
    - 特殊的对象:数组(Array)_带编号的值的有序集合
    - 普通对象:"名-值"对的无序集合
    - 特殊对象:函数
      - 如果使用"new"运算符新建一个对象,我们称之为"构造函数()"
        constructor
      - 每个构造函数定义一类(class)对象--由初始化的对象组成的集合
      - 数组(Array)
      - 函数(Function)
      - 日期(Date)
      - 正则(RegExp)
      - 错误(Error)



内存管理: js有自己的内存管理机制,可以自动对内存进行垃圾回收(garbage collection)

- 数据类型本身可以定义方法, 比如排序
- 从技术上讲, 只有对象才有方法,然而数字,字符串和布尔值也可以拥有方法; unll和undefined是无法拥有方法的值
- js类型可分为原始类型和对象类型
- js类型可分为拥有方法的类型和不能拥有方法的类型
- js类型可分为可变的类型和不可变的类型
- js变量是无类型的(untype),同一个变量可以被赋予任何类型,也可以被重新赋予不同类型的值
- var关键字类声明(declare)变量
- 不在任何函数体内声明的变量为全局变量;函数体内生命的变量只在函数作用内可见

## 8 类型转换

- js取值类型非常灵活,可以根据需要自行转换

  ```javascript
  10 + " objects"		// => 10 objects
  "7" * "4"			// => 28
  var n = 1 - "x"		// =>NaN 字符串转换为数字显示NaN
  ```

### 8.1 转换和相等性

- 因为js可以灵活的类型转换,因此"=="也可以进行相等性运算

```javascript
null == undefined
"0" == 0
0 == False
"0" == False
```

### 8.2 显式类型转换

- 使用可视化的操作,比如Boolean(),Number(),String()或Object()函数

```javascript
Number("3")		// => 3
String(False)	// => "false"
Boolean([])		// => true
Object(3)		// => new Number(3)
```

- 除了null或undefined之外的任何值都具有toString()方法,同String()
- 如果试图将undefined转换为对象,则会抛出TypeError错误
- Object()函数不会抛出异常,仅仅简单返回一个新创建的对象
- `+`运算符会做隐式的类型转换,如果一个操作符是字符串,另一个是数字,则数字会被隐式转换为字符串

```javascript
x + ""		//等价于String(x)
+x			//等价于Number(x)
!!x			//等价于Boolean(x)
```

- js提供了专用函数和方法更加精确的将数字转为字符串

```javascript
//为toString()提供不同的参数,转换为不同的进制数
var n = 17;
binary_string = n.toString(2);		// => "10001"
octal_string = "0" + n.toString(8);	// => "021"
hex_string = "ox" + n.String(16);	// => "ox11"
```

- js用于科学数据
  - toFixed(): 根据传入的参数将制定位数的数字转为字符串
  - toExponential(): 使用指数计数法将数字转为指数形式的字符串,小数点前一位之后依靠传入参数决定
  - toPrecision(): 指定有效位数的数字转为字符串

```javascript
var n = 123456.789;
n.toFixed(0);		// => 123457
n.toFixed(2);		// => 123456.79
n.toFixed(5);		// => 123456.78900
n.toExponential(1);	// => 1.2e+5
n.toExponential(3);	// => 1.235e+5
n.toPrecision(4);	// => 1.235e+5
n.toPrecision(7);	// => 123456.8
n.toPrecision(10);	// => 123456.7890
```

- 其他

  - Number()转换函数传入一个字符串,将字符串转换为整数或浮点数,仅限于十进制数
  - parseInt()只解析整数
  - parseFloat()只解析浮点数

  ```javascript
  parseInt("3 blind mice")		// =>3
  parseFloat("3.14 meters")		// =>3.14
  parseInt("-12.34")				// =>-12
  parseInt("0xFF")				// =>255
  parseInt("-0xff")				// =>-255
  parseFloat(".1")				// =>0.1
  parseInt("0.1")					// =>0
  parseInt(".1")					// =>NaN
  parseFloat("$72.47")			// =>NA
  ```

  ​

## 9 变量声明  

- js程序中,使用一个变量前应当先声明,变量是使用关键字var进行声明
  - `var sum;`声明变量
  - `var i, sum;`声明两个变量
  - `var i=2;`声明和初始化赋值合在一起
  - `var i;i=2;`在初始化赋值前声明的变量值为"undefined"
- 重复的声明合法而无害;遗漏的声明会被报错

## 10 变量作用域

- 一个变量作用域(scope)是程序源代码中定义这个变量的区域
- 全局变量拥有全局作用域,在js代码中任何地方都是有定义的
- 函数内变量声明只在函数体内有定义
- 局部变量优先于全局变量

### 10.1 函数作用域和声明提前

```javascript
var scope = "global";
function f() {
  console.log(scope);  // => "undefined";
  var scope = "local";
  console.log(scope);  // => "local"
}
//在函数体内,所有声明变量都会在函数体顶端提前声明,但并未初始化,
//所以以上代码相当于
var scope = "global";
function f() {
  var scope;
  console.log(scope);  // => "undefined";只声明未初始化
  var scope = "local";
  console.log(scope);  // => "local";声明加初始化过
}
```

### 10.2 作为属性的变量

- 当生命一个js全局变量时,实际上是定义了全局对象的一个属性,当使用var关键字声明一个变量时,创建的这个属性是不可配置的,不可删除的

```javascript
var truevar = 1;
fakevar = 2;
this.fakevar2 = 3;
delete truevar			// => false
delete fakevar			// => true
delete this.fakevar2	// => true
```



### 10.3 作用域链

- 全局变量在程序中始终有定义;局部变量在声明它的函数体以及所嵌套的函数内始终有定义
- 每一个局部变量都可以看作自定义实现的对象的属性;那么每一段代码(全局或函数体)都有其作用域链(scope chain)
- 这个作用域链是一个对象列表或链表,这组对象定义了这段代码"作用域"中的变量
- 如果js需要用到某对象的某个属性(变量)时,就会在作用域链逐行查找;如果没找到就抛出错误(ReferenceError)