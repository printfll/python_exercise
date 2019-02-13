def reverse(seq):
    seq_typ = type(seq)
    empty_seq = seq_typ()

    if not seq:
        return empty_seq
    reverse_seq = reverse(seq[1:])
    result = reverse_seq + seq[0:1]
    return result

def test_reflect():
    print("reverse [1,2,3,4]:",reverse([1,2,3,4]))
    #reverse [1,2,3,4]: [4, 3, 2, 1]
    print("reverse str(1234):",reverse("1234"))
    #reverse str(1234): 4321
    print(f"dir('1234'):{dir('1234')}")
    '''
    dir('1234'):['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
    '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    '''
    print(f"hasattr('1234', 'strip'):{hasattr('1234', 'strip')}")
    #hasattr('1234', 'strip'):True

def test_inspect():
    a = []
    b = []
    c = a

    print(f"a is list:{a is list}.")    #a is list:False.
    print(f"isinstance(a,list):{isinstance(a,list)}.")    #isinstance(a,list):True.
    print(f"a is b:{a is b}, a is c:{a is c}.") #a is b:False, a is c:True.

test_reflect()
test_inspect()
#reflection: 运行时能够获得对象的类型，e.g.: type(), dir():调用这个方法将返回包含obj大多数属性名的列表, hasattr()
#inspect: library, e.g.:inspect.getmoduleinfo(path)
#is: check the address in memory, which indicates mush be the same object
#isinstance: isinstance(object, class or tuple), e.g: isinstance([1,2], list):True, isinstance([],(dict, list)):True, it will check isinstance([], dict), isinstance([], list) one by one