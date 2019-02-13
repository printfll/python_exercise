class SingletonA():
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not SingletonA.__instance:
            SingletonA.__instance = object.__new__(cls, *args, **kwargs)
        return SingletonA.__instance

a = SingletonA()
b = SingletonA()

print(f"a:{a}, b:{b}")


