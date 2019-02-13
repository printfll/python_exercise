def test():
    name = "bob"
    age = 15
    habits = ["sing","run"]
    old_style = "my name is %s, i'm %d years old, I like %s" %(name, age, habits)
    print(f"old_style:{old_style}.")
    new_style = "my name is {}, i'm {} years old, I like {} ".format(name, age, habits)
    print(f"new_style:{new_style}.")
    latest_style = f"my name is {name}, i'm {age} years old, I like {habits}"
    print(f"latest_style:{latest_style}.")

    tuple_obj = ("sing","let it go")
    print("my name is %s, my habit is %s"%(name, tuple_obj))
    #my name is bob, my habit is ('sing', 'let it go')
    try:
        print("only tuple: my habit is %s"%(tuple_obj))
    except Exception as e:
        print(f"error:{e}")
        #error:not all arguments converted during string formatting
    print("correct way only tuple:my habit is %s"%(tuple_obj,))
    #correct way only tuple:my habit is ('sing', 'let it go')
    print("only list: my habit is %s"%(habits))
    #only list: my habit is ['sing', 'run']

test()

#old_style can't only pass tuple like %(tuple), it will raise TypeError, you need to pass like %(tuple,). It is a one-element array(that's why we can pass list like %(list)).
#new_style comes after python3.0
#f-string comes after python3.6