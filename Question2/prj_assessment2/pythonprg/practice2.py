def f1(fun):
    def wrapper():
        print("hello")
        fun()
        print("end")
    return wrapper
@f1 
def f2():
    print("Fidelity")
f2()

        