                                                                                                                        A
abs(x)                  #返回绝对值
all(iterable)           #可迭代对象所有元素全部非空，返回true
any(iterable)           #元组或列表的任意元素为true，返回true
ascii(object)           #返回可打印的字符串

                                                                                                                        B
bin(x)                  #返回整数int的二进制表示
bool(x)                 #转换参数为布尔类型
bytearray()             #返回一个新字节数组，元素值0<=x<256　　　　　　　　　　　　　　　　　　　　月がきれい
'''class bytearray([source[,encoding[,errors]]])
如果 source 为整数，返回长度为source的初始化数组
如果 source 为字符串，按照指定的encoding将字符串转换为字节序列
如果 source 可迭代，元素必须为[0,255]中的整数
如果 source 为与 buffer 接口一致的对象，则此对象可用于初始化 bytearray
如果没有参数，初始化数组为 0 个元素
'''
bytes()                 #返回一个新的bytes对象，为0<=x<256整数不变序列
'''class bytes([source[,encoding[,errors]]])
如果 source 为整数，返回长度为source的初始化数组
如果 source 为字符串，按照指定的encoding将字符串转换为字节序列
如果 source 可迭代，元素必须为[0,255]中的整数
如果 source 为与 buffer 接口一致的对象，则此对象可用于初始化 bytearray
如果没有参数，初始化数组为 0 个元素
'''

                                                                                                                        C
callable(object)        #检查对象是否可调用
chr(i)                  #参数为十进制或十六进制，返回表示unicode码点为整数i的字符串，参数范围为0~1114111(0x10FFFF)
classmethod(function)   #将函数包装成类方法
'''class C :
    @classmethod
    def f(cls,arg1,arg2,...) : ...
'''
compile()               #编译字符串为字节代码
'''compile(source,filename,mode,flags=0,dont_inherit=False,optimize=-1)
详细参数见52页
'''
complex()               #创建real + imag*j的复数或转化一个字符串或数字为复数
'''class complex([real[,imag]])
real:int、long、float、字符串
imag:int、long、float
'''

                                                                                                                        D
delattr(object,name)    #删除对象的特定属性
dict()                  #创建一个字典
'''class dict(**kwargs)
class dict(mapping,**kwargs)
class dict(iterable,**kwargs)
**kwargs:关键字
mapping:元素的容器
iterable：可迭代对象
'''
dir(object)             #尝试返回参数指明的对象合法属性列表
divmod(a,b)             #结合除数和余数运算，返回商和余数的元组（a//b,a%b）

                                                                                                                        E
enumerate()             #将一个可遍历的序列组合成为可索引序列
'''enumerate(sequence,[start=0])
sequence: 序列、迭代器、或者其他支持迭代的对象
start: 下标起始位置
'''
eval()                  #执行字符串表达式，返回表达式的值
'''eval(expression,globals=None,locals=None)
expression: 表达式
globals: 变量作用域，表示全局命名空间。如果被提供，则必须是一个字典对象
locals: 变量作用域，表示全局命名空间。如果有局部变量，则locals可以是任何映射类型对象。
'''
exec()                  #执行储存在字符串或者文件中的python语句，和eval相比此函数可以执行复杂代码
'''exec(object[,globals[,locals]])
object: 必选参数，表示需要被执行的代码，必须为字符串或code对象。
globals: 可选参数，表示全局命名空间，必须为字典对象
locals: 可选参数，表示当前局部命名空间，可映射任何对象。
'''

                                                                                                                        F
filter()                #过滤序列，返回一个filter类，可以看作迭代器，有惰性运算的特性
'''filter(function,iterable)
实现了__iter__和__next__方法
'''
float([x])              #将整数和字符串转换为浮点数
'''class float([x])
对于一般的对象，float委托给x .__float__()。
如果没有给出参数返回0.0
'''
format()                #格式化字符串的函数
'''format(value[,format_spec])
将value转化为format_spec控制的格式
'''
frozenset()             #返回一个冻结的集合
'''class frozenset([iterable])
'''

                                                                                                                        G
getattr()               #返回对象属性值
'''getattr(object,name[,default])
object: 等效调用object.name
name: 对象属性，必须为字符串
default: 默认返回值
'''
globals()               #以字典类型返回当前位置的全局变量，指定义的模块，而不是调用的模块

                                                                                                                        H
hasattr(object,name)    #指定对象是否包含对应属性
hash(object)            #获取对象的整数哈希值
help([object])          #调用内置的帮助系统
hex(x)                  #将十进制数转换为十六进制数
'''float.hex()方法可获取浮点型的十六进制数
'''

                                                                                                                        I
id(object)              #获取对象的整数内存地址
input([prompt])         #获取输入信息
int()                   #将一个字符串或者数字转换为整型
'''class int(x=0)
class int(x,base=10)
参数x为字符串或数字，参数base为进制数
'''
isinstance()            #判断对象是否为一个已知的类型，功能类似于函数type(),
'''isinstance(object,classinfo)
classinfo: 直接或者间接类名、基本类型或者他们的元组
与classinfo类型相同返回true
'''
issubclass()            #判断参数class是否为类型参数classinfo的子类
'''issubclass(class,classinfo)
class:类，表示需要检查类型对象
classinfo: 类，表示需要对比类型对象
如果class参数是classinfo参数的类型对象或者classinfo类对象的直接、间接、虚拟子类的实例
返回true
'''
iter()                  #生成迭代器
'''iter(object[,sentinel])
object:支持迭代的集合对象
sentinel: 如果传递了第二个参数，则蚕食object必须是一个可调用对象，如函数。
此时iter对象创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用object
'''
len(s)                  #返回参数s的长度或项目个数
list(seq)               #将元组seq转换为列表
locals()                #以字典类型返回当前位置的全部局部变量
'''对于函数、方法、lambda、类，以及实现了__call__方法的类实例，都会返回true
当locals()在函数代码块中调用时会返回自由变量，但是在类代码块中时不会
'''

                                                                                                                        M
map()                   #根据提供的函数对指定序列做映射
'''map(function,iterable,...)
function: 含有两个参数的函数
iterable: 一或多个序列
第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表。
最终会返回一个迭代器，对iterable的每个项应用function，并yield结果。
如果传递多个iterable参数，function必须接受所有参数，并应用到iterables并行提取的项中。
如果有多个iterable，迭代器则在最短的iterable耗尽时停止。
'''
max()                   #返回给定参数最大值
'''max(iterable,*[,key,default])
max(arg1,arg2,*args[,key])
默认数值型参数取值大者，字符型参数取字母表排序靠后者。
命令参数key为一个函数，用来指定取最大值的方法。
命名参数default用来指定最大值不存在时返回的默认值。
函数max()至少传入两个参数，但是只有传入一个参数的例外，此时参数必须为可迭代对象，返回的是可迭代对象的最大元素。
'''
min()                   #功能与max函数全部相反
memoryview(obj)         #返回给定参数的内存查看对象
'''所谓内存查看对象，指的是对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许python代码访问。
在python内置对象中，支持缓冲区协议的对象有bytes和bytearray。
'''

                                                                                                                        N
next()                  #返回迭代器的下一个项目
'''next(iterator[,default])
iterator: 可迭代对象
default: 可选参数，用于设置没有下一个对象时返回的默认值。未设置时，无下一个元素会返回stopiteration错误
函数next()通过调用__next__()方法从迭代器中检索下一个项目。
'''

                                                                                                                        O
oct(x)                  #将一个整数转换为八进制字符串，如果x不是int对象，则必须定义返回整数的__index__()方法
open()                  #打开文件
'''open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
mode:
r:只读方式打开文件。文件指针放在开头。只读为默认模式。
rb:二进制方式打开文件用于只读，文件指针放在开头，默认模式。
r+:读写，文件开头。
rb+:二进制，读写，文件开头
w：只写入，文件已存则覆盖，文件不存在，创建新文件
wb:二进制只写入，文件存在则覆盖，文件不存在，创建新文件
w+:读写，文件存在则覆盖，不存在则创建新文件
wb+:二进制读写，文件存在则覆盖，不存在则创建
a:打开文件用于追加，文件存在则指针放到文件末尾，不存在则创建
ab:二进制追加
a+:读写追加
ab+:二进制读写追加
'''
ord(c)                  #chr()的逆函数，返回unicode字符c对应的整数值

                                                                                                                        P
pow(x,y[,z)            #计算x的y次方，并根据z对结果取模，如果y为负，z必须省略
print()                 #あ、これ、わたしわさける。
'''print(*objects,sep=' ',end='/n',file=sys.stdout,,flush=False)
objects: 表示可以一次性输出复数个对象，当数出多个对象时，需要用逗号分隔
sep:间隔多个对象，默认为空格
end:设定结尾，默认为换行符/n
file:要写入的文件对像
flush:设置输出是否使用缓存，默认为false，如果为true，输出流将被强制刷新
'''
property()              #返回一个property属性
'''class property([fget[,fset[,fdel[,doc]]]])
fget；获取属性值的函数
fset:设置属性值的函数
fdel:删除属性值的函数
doc:属性描述信息
property是一个类，作用是用来包装类的属性，这个属性可以根据实际，控制fget函数来实现可读，控制fset函数实现可写，控制fdel函数实现可删除
'''

                                                                                                                        R
range()                 #创建一个整数列表，一般用在for循环中
'''range(stop)
range(start,stop[,step])
'''
repr(object)            #转换为供解释器读取的形式，返回参数可打印的字符串
reversed(seq)           #返回一个反转的iterator迭代器，seq为要转换的序列(可以是tuple.string,list,range类型)，seq必须具有__reversed__()方法或支持序列协议的对象
round(number[,ndigits]) #返回浮点函数x的四舍五入值，4.15.54

                                                                                                                        S
set()                   #创建一个无序不重复元素集
'''class set([iterable])
可进行关系测试，还可以计算交集、差集和并集等
执行set()返回一个新的set()对象，元素可以从itreable中获得
'''
setattr()               #对应函数getattr()，用于设置属性值，该属性不一定是存在的
'''setattr(object,name,value)
name: 字符串，表示对象属性，可以是一个已经存在的属性的名字，也可以是一个新属性的名字
'''
slice()                 #实现切片对象，主要用在切片操作函数里的参数传递操作
'''class slice(stop)
class slice(start,stop[,step])
函数slice可以返回一个slice对象，表示由索引range(start,stop,step)指出的集合。
参数start和参数step默认为none
切片对象具有只读属性，它们仅仅返回参数的值或者他们的默认值
在使用扩展的索引语法时同样会产生切片对象
如：a[start:stop:step]或a[start:stop:step]
'''
sorted()                #对所有可迭代的对象进行排序操作,返回一个新的 list
sorted(iterable,key=None,reverse=False)
itereable: 可迭代对象
key: 带有一个参数的函数，用于从列表的每个元素中提取比较的关键字： key=str.lower默认值时none直接比较元素，该参数用于指定可迭代对象中的一个元素进行排序
revers: 排序规则，为布尔值，false为默认，表示升序
staticmethod(function)  #返回函数的一个静态方法，静态方法不接受隐式的第一个参数即实例名称self
'''要想声明静态方法，请使用惯用式：
class C:
    @staticmethod
    def f(arg1,arg2,...):...

@staticmethod形式是一个函数装饰器，可以在类或者实例中调用，除了他的类型，实例其他内容都将被忽略
'''
str()                   #返回object的str版本，参数str是一个内置的字符串类
'''class str(object='')
class str(object=b'',encoding='utf-8',errors=='strict')
'''
sum(iterable[,start])   #将start以及iterable元素从左到右相加
'''iterable: 可迭代对象，如列表，元素通常为数字
start: 指定相加的参数，默认值为零，不允许为字符串

对于某些情况，有很好的方法替代函数sum(),
连接字符串序列的首选快速方法是调用.join(sequence)
以扩展精度添加浮点值，请使用math.fsum()
要连接一系列可迭代对象，请使用itertools.chain()
'''
super()                 #调用父类（超类）的一个方法，能够返回一个代理对象
'''super([type[,object-or-type]])
type: 类
object-or-type: 类，一般是self
函数super()委托方法给父类或者type的同级类，这对于访问类中被覆盖的继承方法很有用
除了跳过type本身之外，搜索顺序与getattr()所使用的顺序相同
'''

                                                                                                                        T
type()                  #如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
'''class type(object)
class type(name,bases,dict)
name: 类的名称
bases: 基类的元组
dict：字典，类内定义的命名空间变量
当函数type()只有一个参数object时，返回object的类型，返回值是一个类型对象，通常与object.__class__返回的类型相同

isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
'''

                                                                                                                        V
vars([object])          #返回参数对象object的属性和属性值的字典

zip([iterable,...])     #将可迭代对象作为参数，将对象中对应的元素打包成多个元组，返回有这些元组所组成的列表
'''如果各个迭代器的元素个数不一致，则返回列表的长度与最短的对象相同
利用*号操作符，可以将元组解压为列表
'''

__import__()            #动态加载指定的类和函数
'''__import__(name[,globals[,locals[,fromlist[,level]]]])
参数name表示模块名，
如果一个模块经常变化，就可以使用此函数，此函数相当于import module语句
'''


文件操作的经典做法
采用with来保证文件的自关闭
with open('Python\\NOTE.txt', 'w', encoding='utf-8') as f:
    f.write('ZHE ')
with open('NOTE.txt', 'r', encoding='utf-8') as f:
    f.readlines()
注意文件路径的绝对或相对
书写相对路径时，当前文件夹也要书写