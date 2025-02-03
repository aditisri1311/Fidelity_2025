def f1(a):
    def f2():
        print (a)
    return f2()
f1(10)