def gene(i):
    for k in range(i):
        yield k**2
        print(f"yield:{k}.")

def gene2(i):
    return (k+2 for k in range(i))

def itera(i):
    return [k+2 for k in range(i)]

def test():
    res = []
    res.extend(gene(3))
    print(res)
    
    x = gene(1)
    print(type(x))
    print(next(x))
    try:
        print(next(x))
    except StopIteration:
        print("end of iteration.")
    except:
        print("other exception.")

    y = gene2(3)
    print(type(y))
    print(next(y))

    z = itera(3)
    print(type(z))
    print(z)
test()

# generator can only be iterated once
# once exhaust the generator, next(gene) will throw exception("Exception has occurred: StopIteration")
# after python 3.0, gene.next() become gene.__next__(), and it is encouraged to use next(gene)
# use () to construct generator, use list comprehension to construct list