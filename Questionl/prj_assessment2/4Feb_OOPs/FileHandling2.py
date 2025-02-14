file = open("C:/DBMS/NewFile.txt","r")
print(file.tell())
data = file.read(2)
file.seek(0)
print(data)
'''
#To read the no of character in the whole file, read is used.
#To read the no of lines we use readeachline.
x= file.readlines()
print(x)
y= file.readline()
print(y)
file.close
'''
for l in file:
    print