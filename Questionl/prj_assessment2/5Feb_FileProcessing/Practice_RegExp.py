import re
str= "aditi13@gmail.com"
l = re.findall(r"\A[a-z]{1}[^@$#\s]*\d{1}[^@$#\s]*\d{1}[^@$#\s]*@[a-z]+.com$", str)
print(l)

