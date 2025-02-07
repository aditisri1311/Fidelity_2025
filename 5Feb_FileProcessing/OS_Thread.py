from threading import *
import time
def f1():
    for i in range(1, 11):
        time.sleep(1)
        print(2**i)
def f2():
    for i in range(1,10):
        time.time(1)
btime= time.time()
f1()
print(time.time() - btime)