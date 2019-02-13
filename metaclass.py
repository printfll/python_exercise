def echo_bar(self):
    print(f"bar is:{self.bar}.")

def echo_more_bar(self):
    self.bar += 1
    print(f"increase bar:{self.bar}.\n")

def test():
    class1 = type("MyObjectClass",(),{"bar":1})

    print(f"type(class1):{type(class1)}, base(class1):{class1.__bases__}.")   
    #type(class1):<class 'type'>, base(class1):(<class 'object'>,).
    print(f"class1.bar:{class1.bar}")   #class1.bar:1
    obj1 = class1()
    print(f"type(obj1):{type(obj1)}\n") #type(obj1):<class '__main__.MyObjectClass'>

    class2 = type("MySecObjClass",(class1,),{"child":True}) 
    print(f"type(class2):{type(class2)}, base(class2):{class2.__bases__}.")   
    #type(class2):<class 'type'>, base(class2):(<class '__main__.MyObjectClass'>,).
    print(f"class2.bar:{class2.bar}, class2.child:{class2.child}")  #class2.bar:1, class2.child:True
    class2.bar = 2
    obj2 = class2()
    print(f"type(obj2):{type(obj2)}\n") #type(obj2):<class '__main__.MySecObjClass'>

    class3 = type("MyThirdObjClass",(class2,),{"echo":echo_bar})
    print(f"type(class3):{type(class3)}, base(class3):{class3.__bases__}.")   
    #type(class3):<class 'type'>, base(class3):(<class '__main__.MySecObjClass'>,).
    print(f"class3.bar:{class3.bar}, class3.child:{class3.child}, class3 hasattr echo:{hasattr(class3, 'echo')}")
    #class3.bar:2, class3.child:True, class3 hasattr echo:True
    class3.echo_more = echo_more_bar
    obj3 = class3()
    print(f"type(obj3):{type(obj3)}, obj3 hasattr echo:{hasattr(obj3, 'echo')}, obj3 hasattr bar:{hasattr(obj3, 'bar')}")
    #type(obj3):<class '__main__.MyThirdObjClass'>, obj3 hasattr echo:True, obj3 hasattr bar:True
    obj3.echo()
    #bar is:2.
    obj3.echo_more()
    #increase bar:3.

    metaclass = type("MyMetaClass",(type,),{})
    print(f"type(metaclass):{type(metaclass)}, base(metaclass):{metaclass.__bases__}.")
    #type(metaclass):<class 'type'>, base(metaclass):(<class 'type'>,).
    metaclass2 = type("MyMetaClass2",(),{"__metaclass__":metaclass})
    print(f"type(metaclass2):{type(metaclass2)}, base(metaclass2):{metaclass2.__bases__}.")
    #type(metaclass2):<class 'type'>, base(metaclass2):(<class 'object'>,).
    metaobj = metaclass2() 
    print(f"type(metaobj):{type(metaobj)}")
    #type(metaobj):<class '__main__.MyMetaClass2'>

test()

'''
class is also an object, so we can assign class to other variable
在Python的世界中，object是父子关系的顶端，所有的数据类型的父类都是它；type是类型实例关系的顶端，所有对象都是它的实例的。它们两个的关系可以这样描述：- object是一个type，object is and instance of type。即Object是type的一个实例。
>>> list.__bases__
(<type 'object'>,)
>>> list.__class__
<type 'type'>

we can't create instance of metaclass, because metaclass.base is not the object, so if we run metaobj=metaclass(), it will throw exception.
'''


