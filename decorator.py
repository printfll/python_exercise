def impl_decorator(func):
    def inside():
        return f"here is inside.{func()}.finish inside."
    return f"here is impl_decorator.{inside()}.finish impl_decorator."

def dec():
    return "helloworld"

def dec3(func):
    def wrap3(arg1, arg2):
        print(f"here is dec3:{arg1}, {arg2}. {func.__name__}")
        func(arg1, arg2)
        print("finish dec3")
    return wrap3

def dec2(func):
    def wrap2(arg1, arg2):
        print(f"here is dec2:{arg1}, {arg2}. {func.__name__}")
        func(arg1, arg2)
        print("finish dec2")
    return wrap2

@dec3
@dec2
def dec1(arg1, arg2):
    print(f"helloworld:{arg1}, {arg2}.")

def test():
    print(impl_decorator(dec))
    #here is impl_decorator.here is inside.helloworld.finish inside..finish impl_decorator.
    dec1("a","b")
    # here is dec3:a, b. wrap2
    # here is dec2:a, b. dec1
    # helloworld:a, b.
    # finish dec2
    # finish dec3


test()
