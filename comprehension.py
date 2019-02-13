def list_comprehension(seq):
    res = [x**2 for x in seq if x>0]
    return res

def set_comprehension(seq):
    res = {x for x in seq if x%2==0}
    return res

def dict_comprehension(seq):
    res = {i:x for i,x in enumerate(seq) if x%3==2}
    return res

def test():
    seq = [i for i in range(-10,11)]
    print(f"original seq:{seq}.")
    #original seq:[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    print(f"list_comprehension:{list_comprehension(seq)}.")
    #list_comprehension:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    print(f"set_comprehension:{set_comprehension(seq)}.")
    #set_comprehension:{0, 2, 4, 6, 8, 10, -10, -8, -6, -4, -2}.
    print(f"dict_comprehension:{dict_comprehension(seq)}.")
    #dict_comprehension:{0: -10, 3: -7, 6: -4, 9: -1, 12: 2, 15: 5, 18: 8}.

    id_matrix = [[1,0,0],
             [0,1,0],
             [0,0,1]]
    new_arr = [i for row in id_matrix for i in row]
    print(f"new_arr is {new_arr}.")
    #new_arr is [1, 0, 0, 0, 1, 0, 0, 0, 1].

test()