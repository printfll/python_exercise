def immutable_ref(a):
    print(f"immutable_ref before:{a}, id:{id(a)}")
    a = "aaa"
    print(f"immutable_ref after:{a}, id:{id(a)}")

def immutable_ref_2(a):
    print(f"immutable_ref_2 before:{a}, id:{id(a)}")
    a = [1,2,3]
    print(f"immutable_ref_2 after:{a}, id:{id(a)}")

def mutable_ref(a):
    print(f"mutable_ref before:{a}, id:{id(a)}")
    a.append("append")
    print(f"mutable_ref after:{a}, id:{id(a)}")

def test():
    a = ["a","b","c"]
    print(f"before test:{a}, id:{id(a)}")
    immutable_ref(a)
    print(f"after test immutable_ref:{a}, id:{id(a)}")
    immutable_ref_2(a)
    print(f"after test immutable_ref_2:{a}, id:{id(a)}")
    mutable_ref(a)
    print(f"after test mutable_ref:{a}, id:{id(a)}")

test()

#python pass reference-to-object by value, and some object are immutable(string, tuple, numbers), so when we want to change these objects, it actually creates new object, and the reference refers to the new obj. Meanwhile, some object are mutable, like dict, list, set, when we change them, the object in memory changes