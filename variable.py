class A():
    total = 0
    job = "eng"
    lists = []
    def __init__(self, name):
        self.name = name
        A.total += 1
    
def test():
    a = A("a")
    a.job = "teacher"
    print(f"a.name:{a.name}, total:{a.total}, job:{a.job}.")
    #a.name:a, total:1, job:teacher.
    print(f"A.total:{A.total}, A.job:{A.job}.")
    #A.total:1, A.job:eng.
    b = A("b")
    b.job = "cooker"
    print(f"b.name:{b.name}, total:{b.total}, job:{b.job}.")
    #b.name:b, total:2, job:cooker.
    print(f"a.name:{a.name}, total:{a.total}, job:{a.job}.")
    #a.name:a, total:2, job:teacher.
    print(f"A.total:{A.total}, A.job:{A.job}.")
    #A.total:2, A.job:eng.

    a.lists.append("a")
    print(f"a.lists:{a.lists}.")    #a.lists:['a'].
    b.lists.append("b")
    print(f"b.lists:{b.lists}.")    #b.lists:['a', 'b'].
    print(f"A.lists:{A.lists}.")    #A.lists:['a', 'b'].

test()

#A.total and A.job is class variable, a.name is instance variable, a.job change inference to new string(since string is immutable), while A.lists is mutable, so we always change on same list.