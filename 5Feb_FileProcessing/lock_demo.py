from threading import *
import time
l = Semaphore(5) #Lock()
def wish(name):
    l.acquire()
    for i in range(5):
        print("Good Morning", end="")
        time.sleep(2)
        print(name)
    l.release()
t1= Thread(target= wish, args = ("Rahul", ))
t2= Thread(target= wish, args= ("Steve", ))
t1.start()
t2.start()