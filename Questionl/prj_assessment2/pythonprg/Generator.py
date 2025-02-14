import sys
l1 =[i for i in range (100)]
g =(i for i in range (100))
print(sys.getsizeof(l1))
print(sys.getsizeof(g))