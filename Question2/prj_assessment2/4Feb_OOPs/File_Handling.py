'''file = open("test.txt", "r")
#When we open the file, the cursor will come to the beginning of the file.'''
# file = open("test.txt", "w")
#When the file is not there, the file will be created and if it is there then it will be overwritten.
file = open("c://dbms//Test.txt.txt", "r") #enter the 

data1 = file.read(2) #2character he
data2 = file.read()
print(data1)
print(data2)
file.close
#readline k liye while loop chala sakte hai
