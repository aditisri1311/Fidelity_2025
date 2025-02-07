#Aditi Srivastava
#aditisrivastava1311@gmail.com
import re

text = """I know a set of email addresses that we can extract using expression1: 
abc.df@somecompany.co.uk, abc@gmail.com, xyz.ab@tpa.com, dfg.gh@dp.cp.net.
But what about 11.234.abc.ghy@tp.edu, let's check."""

pattern = r'\b[a-zA-Z]\d*[\w]*@[a-zA-Z0-9]+\.(com|net|in|uk)\b'
emails = re.findall(pattern, text)
valid_emails = [match.group() for match in re.finditer(pattern, text)]

print(valid_emails)
