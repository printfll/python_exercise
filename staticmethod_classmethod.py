def common_foo(x):
    print(f"common_foo:{x}.")

class A():
    x = 15
    y = 20
    def foo(self, x):
        print(f"foo:{x}, self:{self}.")
    
    @staticmethod
    def static_foo(x):
        print(f"static_foo:{x}.")
    
    @classmethod
    def class_foo(cls, x):
        print(f"class_foo:{x}, cls:{cls}.")
    
def test():
    a = A()

    A.static_foo(A.x)   #static_foo:15
    A.x = 17
    A.class_foo(A.x)    #class_foo:17, cls:<class '__main__.A'>.

    common_foo(a.x) #common_foo:17.
    a.foo(a.x)  #foo:17, self:<__main__.A object at 0x000001A93CEF5EB8>.
    a.x = 12    
    a.static_foo(a.x)   #static_foo:12.
    a.x = 13
    a.class_foo(a.x)    #class_foo:13, cls:<class '__main__.A'>.

test()

# static method doesn't pass object or class by default, we can call obj.static_method(), cls.static_method(), obj.class_method(), cls.class_method(), obj.instance_method(), but we can't call cls.instance_method(), e.g: we can't call A.foo(x)