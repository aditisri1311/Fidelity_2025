import os
print(os.listdir("C:/DBMS"))
for dirpath, dir, file in os.walk("."):
    print(dirpath, dir,file)
for i in file:
    if i.endswith(".py"):
        print(i)
#Python is not flexibe with threads
