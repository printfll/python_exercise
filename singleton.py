class SingletonA():
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not SingletonA.__instance:
            SingletonA.__instance = object.__new__(cls, *args, **kwargs)
        return SingletonA.__instance

a = SingletonA()
b = SingletonA()
print(f"a:{a}, b:{b}")
# a:<__main__.SingletonA object at 0x000001ADF490CE48>, b:<__main__.SingletonA object at 0x000001ADF490CE48>

