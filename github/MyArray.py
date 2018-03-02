#定义一个数组类MyArray，支持数组与数字之间的四则运算，数组之间的加法运算、内积运算和大小比较，数组元素访问和修改，以及成员测试等功能
#定义函数IsNumber对输入字符进行限制,构造函数init,析构函数del,重载运算符+add、重载运算符-sub、重载运算符×mul、重载运算符/truediv、重载floordiv
#重载运算符%mod、重载运算符××pow、直接使用该类对象作为表达式来查看对象的值repr、支持使用print()函数查看对象的值、追加元素append、
#获取指定下标的元素值，支持使用列表或元组指定多少个下标getitem、修改元素值，支持使用列表或元组指定多个下标，同时修改多个元素值setitem、
#支持成员测试运算符in，contains、模拟向量内积dot、重载运算符==，eq、重载运算符<lt

class MyArray():
    '''all element must be number'''
    def __IsNumber(self,n):
        if not isinstance(n,(int,float,complex)):
            return False
        return True
	
    def __init__(self,*args):#构造函数，进行必要的初始化
        if not args:
            self.__values=[]
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('必须输入数字')
                    return
            self.__values=list(args)
	
	def __del__(self):#析构函数
        def self.__value
	
	def __add__(self,n):#重载运算符+
        if not self.__IsNumber(n):
            print(‘+运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item+n for item in self.__value]
        elif isinstance(n,MyArray）：
            if len(n.__value)==len(self.__value):
                c=MyArray()
                return c.__value=[i+j for i,j in zip(self.__value,n.__value)
            else:
                print('数列在使用加法时，数列中包含的数字数量必须保持一致')
        else:
            print('类型错误')
                
	
	def __sub__(self,n): #重载运算符-
        if not self.__IsNumber(n):
            print('-运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item-n for item in self.__value]
	
	def __mul__(self,n): #重载运算符*
        if not self.__IsNumber(n):
            print('*运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item*n for item in self.__value]
        
	
	def __truediv__(self,n):#重载运算符/
        if not self.__IsNumber(n):
            print('/运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item/n for item in self.__value]
        
	def __floordiv__(self,n): #重载运算符//
        if not self.__IsNumber(n):
            print('/运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item//n for item in self.__value]
        
	def __mod__(self,n): #重载运算符%
        if not self.__IsNumber(n):
            print('%运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item%n for item in self.__value]
        
	def __pow__(self,n): #重载运算符**
        if not self.__IsNumber(n):
            print('**运算符必须用于数字之间')
            return
        b=MyArray()
        return b.__value=[item**n for item in self.__value]
        
	def __repr__(self): #直接使用该类对象作为表达式来查看对象的值repr
        return self.__value
        
	def __str__(self): #支持使用print()函数查看对象的值
        return str(self.__value)
        
	def append(self,n): #追加元素append
        b=MyArray()
        b.__value=self.__value.append(n)
        
	def __getitem__(self,index): #支持使用列表或元组指定多少个下标getitem
        lenth=len(self.__value）
        if isinstance(index,int) and 0<=index<lenth:
            b=MyArray()
            return b.__value=self.__value[index]
        elif isinstance(index,MyArray):
            for i in index:
                if isinstance(i,int) and 0<=i<lenth:
                    b=MyArray()
                    return b.__value=self.__value[i]
                else:
                    return 'index error'
        return 'index error'
	
	def __setitem__(self,index,n): #支持使用下标同时修改多个元素值setitem
        lenth=len(self.__value)
        if isinstance(index,int) and 0<=index<lenth:
            if not self.__IsNumber(n):
                print(n,'必须是数字')
                return
            return self.__value[index]=n
        elif isinstance(index,MyArray):
            for i in index:
                if isinstance(i,int) and 0<=i<lenth:
                    if not self.__IsNumber(n):
                        print(n,'必须是数字)
                        return
                    return self.__value[i]=n
        else:
            return 'index error'
	def __contains__(self,n): #支持成员测试运算符in
        if n in self.__value:
            return True
        return False
        
	def dot(self,n): #模拟向量内积
        lenth=len(self.__value)
        if isinstance(n,MyArray):
            if lenth==len(n):
                b=MyArray()
                return b.__value=sum([i*j for i,j in zip(n,self.values)])
            else:
                print('lenth error')
                rerurn
        else:
            print('类型必须保持一致')
            return
	def __eq__(self,n):  #重载运算符==
        if not isinstance(n,MyArray)；
            print('类型必须保持一致')
            return
        if n.__value==self.__value:
            return True
        return False
        
	
	def __lt__(self,n):  #重载运算符<
        if not isinstance(n,MyArray):
            print('类型必须保持一致')
            return
        if n.__value<self.__value:
            return True
        return False
        
if __name__=='__mian__':
    print('此类可以作为modle导入')
	