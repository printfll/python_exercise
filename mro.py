class Parent():
    name = "Parent"
    def __init__(self):
        super().__init__()
        print(f"Parent. init {self.name}")
        
    def check(self):
        print(f"Parent. type:{type(self)}")

class Daughter(Parent):
    def __init__(self):
        super().__init__()
        print(f"Daughter. init {self.name}")
    def check(self):
        print(f"Daughter. type:{type(self)}")

class Son(Parent):
    def __init__(self):
        super().__init__()
        print(f"Son. init {self.name}")
    def check(self):
        print(f"Son. type:{type(self)}")

class Friend():
    name = "Friend"
    def __init__(self):
        super().__init__()
        print(f"Friend. init {self.name}.")

    def check(self):
        print(f"Friend. type:{type(self)}")

class Me(Daughter, Friend):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.my_name = name
        print(f"Me. init {self.name}")

class AnotherMe(Friend, Son):
    def __init__(self, name):
        self.name = name
        super().__init__()
        print(f"AnotherMe. init {self.name}")

class You(Daughter, Son):
    name = ""
    def __init__(self, name):
        super().__init__()
        self.name = name
        print(f"You. init {self.name}.")

def test():
    print("Init Me")
    me = Me("me")
    me.check()
    print(Me.__mro__)
    '''
    Friend. init Parent.
    Parent. init Parent
    Daughter. init Parent
    Me. init me
    Daughter. type:<class '__main__.Me'>
    (<class '__main__.Me'>, <class '__main__.Daughter'>, <class '__main__.Parent'>, <class '__main__.Friend'>, <class 'object'>)
    '''

    print("\nInit AnotherMe")
    another_me = AnotherMe("another_me")
    another_me.check()
    print(AnotherMe.__mro__)
    '''
    Parent. init another_me
    Son. init another_me
    Friend. init another_me.
    AnotherMe. init another_me
    Friend. type:<class '__main__.AnotherMe'>
    (<class '__main__.AnotherMe'>, <class '__main__.Friend'>, <class '__main__.Son'>, <class '__main__.Parent'>, <class 'object'>)
    '''

    print("\nInit You")
    you = You("you")
    you.check()
    print(You.__mro__)
    '''
    Parent. init
    Son. init
    Daughter. init
    You. init you.
    Daughter. type:<class '__main__.You'>
    (<class '__main__.You'>, <class '__main__.Daughter'>, <class '__main__.Son'>, <class '__main__.Parent'>, <class 'object'>)
    '''
test()


#exhausted and confused
#In Init Me case, if remove super().__init__() in Parent init, it wont't run Friend init
#In Init You case, don't know why Parent init without name???
#when call check(), python use dfs to find the function
