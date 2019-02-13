class Parent():
    name = "Parent"
    def __init__(self):
        super().__init__()
        print(f"Parent. init {self.name}")
        
    def level(self):
        print(f"Parent. type:{type(self)}")

class Daughter(Parent):
    def __init__(self):
        super().__init__()
        print(f"Daughter init {self.name}")

    def dance(self):
        print(f"Daughter. I can dance.")

class Son(Parent):
    def __init__(self):
        super().__init__()
        print(f"Son init {self.name}")
    
    def run(self):
        print(f"Son. I can run.")

class Friend():
    name = "Friend"
    f_age = 15
    def __init__(self):
        super().__init__()
        print(f"Friend init {self.name}.")

    def level(self):
        print(f"Friend. type:{type(self)}")
    
    def hi(self):
        self.f_age += 1
        print(f"Friend. say hi to {self.f_age}")

class Me(Daughter, Friend):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.my_name = name
        print(f"Me init {self.name}")

class AnotherMe(Daughter, Friend):
    def __init__(self, name):
        self.name = name
        super().__init__()
        print(f"Me init {self.name}")

class You(Daughter, Son):
    name = ""
    def __init__(self, name):
        super().__init__()
        self.name = name
        print(f"You init {self.name}.")

def test():
    print("Init Me")
    me = Me("me")
    me.level()
    me.hi()
    print(Me.__mro__)
    '''
    Friend init Parent.
    Parent. init Parent
    Daughter init Parent
    Me init me
    Parent. type:<class '__main__.Me'>
    Friend. say hi to 16
    (<class '__main__.Me'>, <class '__main__.Daughter'>, <class '__main__.Parent'>, <class '__main__.Friend'>, <class 'object'>)
    '''

    print("\nInit AnotherMe")
    me = AnotherMe("another_me")
    me.level()
    me.hi()
    print(Me.__mro__)
    '''
    Friend init another_me.
    Parent. init another_me
    Daughter init another_me
    Me init another_me
    Parent. type:<class '__main__.AnotherMe'>
    Friend. say hi to 16    
    (<class '__main__.Me'>, <class '__main__.Daughter'>, <class '__main__.Parent'>, <class '__main__.Friend'>, <class 'object'>)
    '''

    print("\nInit You")
    you = You("you")
    you.level()
    print(You.__mro__)
    '''
    Parent. init
    Son init
    Daughter init
    You init you.
    Parent. type:<class '__main__.You'>
    (<class '__main__.You'>, <class '__main__.Daughter'>, <class '__main__.Son'>, <class '__main__.Parent'>, <class 'object'>)
    '''
test()


#exhausted and confused
#In Init Me case, if remove super().__init__() in Parent init, it wont't run Friend init
#In Init You case, don't know why Parent init without name???
#when call level(), python use dfs to find the function
