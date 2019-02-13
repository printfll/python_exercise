class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print("EXISTS")
            return A._dict['key']
        else:
            print("NEW")
            return super(A, cls).__new__(cls)

    def __init__(self):
        print("INIT")
        A._dict['key'] = self
        print(f"Finish init , id:{id(self)}.")

a1 = A()
a2 = A()
a3 = A()

'''
NEW
INIT
Finish init , id:2054804168488.
EXISTS
INIT
Finish init , id:2054804168488.
EXISTS
INIT
Finish init , id:2054804168488.
'''