def print_args(*args):
    for i, value in enumerate(args):
        print(f"print_args: the {i}th element is {value}")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"print_kwargs: key:{key}, value:{value}")

def print_combine(fruit, *args, **kwars):
    print(f"print_combine: fruit:{fruit}, args:{args}, kwars:{kwars}")

def test():
    lists = ["apple","banana", "pear","peach"]
    dics = {"red":"apple", "yellow":"banana", "green":"pear", "pink":"peach"}
    print_args(*lists)
    # print_args: the 0th element is apple
    # print_args: the 1th element is banana
    # print_args: the 2th element is pear
    # print_args: the 3th element is peach
    print_kwargs(**dics)
    # print_kwargs: key:red, value:apple
    # print_kwargs: key:yellow, value:banana
    # print_kwargs: key:green, value:pear
    # print_kwargs: key:pink, value:peach
    print_combine("grape", *lists, **dics)
    #print_combine: fruit:grape, args:('apple', 'banana', 'pear', 'peach'), kwars:{'red': 'apple', 'yellow': 'banana', 'green': 'pear', 'pink': 'peach'}
    print_combine(**dics)
#   TypeError: print_combine() missing 1 required positional argument: 'fruit'



test()

# named_parameter must appear before *args, *args must appear before **kwargs