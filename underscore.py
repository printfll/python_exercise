class A():
    def __init__(self):
        self.__private = "__private"
        self._semiprivate = "_semiprivate"

def test():
    a = A()
    try:
        print(f"a.__private:{a.__private}.")
    except Exception as e:
        print(f"error:{e}.")
        #error:'A' object has no attribute '__private'.
    
    print(f"a._A__private:{a._A__private}")
    #a._A__private:__private
    print(f"a._semiprivate:{a._semiprivate}.")
    #a._semiprivate:_semiprivate.
    print(f"a.__dict__:{a.__dict__}.")
    #a.__dict__:{'_A__private': '__private', '_semiprivate': '_semiprivate'}.

test()

# __name__: python officially define, user is not suggested to use
# _name : can only used by class instance or children class instance, can't get by "from module import *"
# __name : can only use in class, interpreter use _A__private to visit __private, in order not conflict with other __private defination in other class, a._A__private